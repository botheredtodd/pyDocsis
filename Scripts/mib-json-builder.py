import argparse
import re
from pathlib import Path
from typing import List, Optional
import json
import os

class RawMibItem:

    def __init__(self, name: str, parent: str, index: int, mib_name: str, syntax=None):
        self.name: str = name
        self.parent: str = parent
        self.index: int = index
        self.mib_name: str = mib_name
        self.syntax = syntax


class RawMib:

    def __init__(self, mibname: str, syntax=None):
        self.name: str = mibname
        self.items: List[RawMibItem] = []
        self.syntax = syntax

    def add_item(self, name: str, parent: str, index: int, syntax=None):
        if name in [item.name for item in self.items]:
            # print(f"Warning: {name} already in {self.name}, updating instead of adding.")
            self.update_item(name, parent, index, syntax)
        else:
            # print(f"adding item {name} to {self.name}")
            self.items.append(RawMibItem(name, parent, index, self.name, syntax))
    def update_item(self, name: str, parent: str, index: int, syntax):
        for item in self.items:
            if item.name == name:
                item.parent = parent
                item.index = index
                item.syntax = syntax
                return

class Node:
    def __init__(self, name, oid, mib_name=None, syntax=None):
        self.name = name
        if not mib_name:
            mib_name = "(unknown MIB)"
        self.mib_name = mib_name
        self.oid = oid
        self.subnodes = []
        self.syntax = syntax

    def add_subnode(self, name, number, mib_name=None, syntax=None):
        subnode = Node(name, self.oid + "." + str(number), mib_name, syntax)
        if subnode not in self.subnodes:
            self.subnodes.append(subnode)
            self.subnodes.sort(key=oid_sort_func)
            return subnode
        else:
            print("Warning: subnode already exists, updating instead of adding.")
            for node in self.subnodes:
                if node == subnode:
                    node.syntax = syntax
                    return node


def oid_sort_func(node):
    """Returns the last number in node's OID for sorting the subnodes"""
    try:
        return int(node.oid.split(".")[-1])
    except:
        return 0


def find_node(node, name):
    """Finds a node based on its name, returns Node"""
    if node.name == name:
        return node
    for subnode in node.subnodes:
        found_node = find_node(subnode, name)
        if found_node:
            return found_node
    return None


def find_item_in_all_mibs(all_mibs: List[RawMib], item_name: str):
    for mib in all_mibs:
        for item in mib.items:
            if item.name == item_name:
                return item
    return None


def add_item(mibtree: Node, all_mibs: List[RawMib], item: RawMibItem):
    """Adds the item in the MIB tree, recursively creating the parent
    items as well if needed."""
    # if item.syntax:
    #     print(f"Syntax for additem is {item.syntax}")
    node = find_node(mibtree, item.name)
    if node:
        if item.syntax != node.syntax:
            print(f"Warning: {item.name} already exists in {item.mib_name} with a different syntax.")
            node.syntax = item.syntax
        return True
    parent_item = find_item_in_all_mibs(all_mibs, item.parent)
    if not parent_item:
        return False
    result = add_item(mibtree, all_mibs, parent_item)
    if result:
        parent_node = find_node(mibtree, parent_item.name)
        parent_node.add_subnode(item.name, item.index, item.mib_name, item.syntax)
        return True
    return False


def print_list(node):
    if node.syntax:
        print("{} = {}::{} Allowed Values: {}".format(node.oid, node.mib_name, node.name, node.syntax))
    else:
        print("{} = {}::{}".format(node.oid, node.mib_name, node.name))
    for subnode in node.subnodes:
        print_list(subnode)

def make_pyDocsis_Dict(node, retval=None):
    if not retval:
        retval = {}
    if node.syntax:
        retval[node.oid] = {"name": f"{node.mib_name}::{node.name}", "syntax": node.syntax}
    else:
        retval[node.oid] = {"name": f"{node.mib_name}::{node.name}", "syntax": None}
    for subnode in node.subnodes:
         make_pyDocsis_Dict(subnode, retval)
    return retval

root_mib = RawMib("(root)")
root_mib.add_item("iso", "", 1)
all_mibs: List[RawMib] = [ root_mib ]
all_mib_files: dict = {}
missing_imports = {}
missed_mibs = []


def load_mib_by_name(mib_name: str):
    if mib_name not in all_mib_files:
        global missed_mibs
        if mib_name not in missed_mibs:
            print(f"MIB '{mib_name}' not found")
            missed_mibs.append(mib_name)
        return False
    mib = None
    name_waiting = None
    prev_line = None
    more_needed = False
    imported_items = []
    parsing_imports = False
    syntax = None
    description = None
    global all_mibs
    imports = {}
    in_syntax = False
    in_description = False
    underline = None
    with open(all_mib_files[mib_name]) as input_file:
        for line in input_file:
            line = line.strip()
            cols = line.split()
            if "TEXTUAL-CONVENTION" in line:
                underline = None
            if len(cols) > 0:
                if cols[0] == "SYNTAX":
                    syntax = " ".join(cols[1:])
                    if "{" in line:
                        # print("Syntax has more lines")
                        in_syntax = True
                    continue
            if in_syntax:
                syntax += " " + line
                if line.endswith("}"):
                    # print(f"Found {syntax} in multi-line syntax")
                    # print(f"Found {syntax} in {underline}")
                    in_syntax = False
                continue
            if len(cols) > 0:
                if cols[0] == "DESCRIPTION":
                    description = " ".join(cols[1:])
                    if line.endswith("\""):
                        in_description = False
                    else:
                        in_description = True
                    continue
            if in_description:
                description += " " + line
                if line.endswith("\""):
                    in_description = False
                continue
            if name_waiting:
                if "::=" not in line:
                    continue
                # if syntax:
                #     print(f"Found {syntax} in {name_waiting}")
                name = name_waiting
                name_waiting = None
                match = re.search(r"::=\s*\{\s*([\w-]+)\s+([0-9]+)\s*\}", line)
                parent = match[1]
                number = match[2]
                # Added to the tree later below
            elif parsing_imports:
                words = re.split(r"[, ]+", line)
                i = 0
                while i < len(words):
                    if words[i] != "FROM":
                        if words[i]:
                            imported_items.append(words[i])
                    else:
                        imported_from = words[i+1]
                        i += 1
                        if imported_from.endswith(";"):
                            parsing_imports = False
                            imported_from = imported_from[:-1]
                        for item in imported_items:
                            imports[item] = imported_from
                        imported_items = []
                    i += 1
                continue
            elif line == "" or line.startswith("--"): # or line.find(",") >= 0:
                continue
            elif (
                len(cols) == 2 and cols[1] in [
                    "OBJECT-IDENTITY",
                    "OBJECT-TYPE",
                    "MODULE-IDENTITY",
                    "NOTIFICATION-TYPE",
                ]) or (
                len(cols) == 3 and cols[1] == "OBJECT" and cols[2] == "IDENTIFIER"
            ):
                # Save the name and keep looping
                name_waiting = cols[0]
                underline = line
                # print(underline)
                syntax = None
                continue
            elif "DEFINITIONS" in cols and "::=" in cols and "BEGIN" in cols:
                # "mibname DEFINITIONS ::= BEGIN"
                mib_name = cols[0]
                if mib:
                    all_mibs.append(mib)
                mib = RawMib(mib_name)
                continue
            elif more_needed:
                line = prev_line + " " + line
                more_needed = False
            elif line.find("OBJECT IDENTIFIER") >= 0:
                if line == "OBJECT IDENTIFIER":
                    continue
                elif line.find(")") >= 0:
                    continue
                elif line.find("::=") == -1:
                    # We need to read more to find the assignment
                    more_needed = True
                    prev_line = line
                    continue
                elif line.startswith("OBJECT IDENTIFIER"):
                    # Let's take the previous line as well
                    line = prev_line + " " + line
                match = re.search(r"([\w-]+)\s*OBJECT IDENTIFIER\s*::=\s*\{\s*([\w-]+)\s*([0-9]+)\s*\}", line)
                name = match[1]
                parent = match[2]
                number = match[3]
            elif line.startswith("IMPORTS"):
                imported_items = []
                parsing_imports = True
                words = re.split(r"[, ]+", line)
                if len(words) == 1:
                    continue
                i = 1   # Skip the first word "IMPORTS"
                while i < len(words):
                    if words[i] != "FROM":
                        imported_items.append(words[i])
                    else:
                        imported_from = words[i+1]
                        i += 1
                        if imported_from.endswith(";"):
                            parsing_imports = False
                            imported_from = imported_from[:-1]
                        for item in imported_items:
                            imports[item] = imported_from
                        imported_items = []
                    i += 1
                continue
            else:
                prev_line = line
                continue
            #print("{} = {{ {} {} }}".format(name, parent, number))
            if parent != "0":   # Skip zeroDotZero
                # print(f"{name} = {{ {parent} {number} {syntax} }}")
                mib.add_item(name, parent, int(number), syntax)
                # syntax = None
    if mib:
        mib.syntax = syntax
        global missing_imports
        for item, mib_name in imports.items():
            if not load_mib_by_name(mib_name):
                missing_imports[item] = mib_name
        all_mibs.append(mib)
    return True


def get_mib_name_from_file(path: Path) -> Optional[str]:
    """Returns the MIB name from the MIB file."""
    with open(path) as f:
        try:
            for line in f:
                line = line.strip()
                match = re.search(r"^([\w-]+)\s+DEFINITIONS\s*::=\s*BEGIN", line)
                if match:
                    return match[1]
        except UnicodeDecodeError:
            return None
    return None


def get_all_mibs(path: Path):
    """Returns all MIB names with their file names."""

    mib_files: dict = {}
    for p in path.glob("*"):
        if p.is_file():
            print(f"Found {p}")
            mib_name = get_mib_name_from_file(p)
            if mib_name:
                mib_files[mib_name] = p
        elif p.is_dir():
            mib_files.update(get_all_mibs(p))
    return mib_files


def main(searchpath: List[str] = []):
    retval = {}
    # parser = argparse.ArgumentParser()
    # # parser.add_argument(
    # #     "mib_name",
    # #     metavar="mibname",
    # #     help="The name of the MIB to be shown",
    # # )
    # parser.add_argument(
    #     "-a", "--add",
    #     metavar="path(s)",
    #     help="Add given path(s) (comma-separated) to MIB search list",
    #     dest="add_paths",
    #     required=False,
    # )
    # parser.add_argument(
    #     "-n", "--no-default",
    #     help="Do not use the default MIB search path",
    #     required=False,
    #     action="store_true",
    # )
    # args = parser.parse_args()
    if searchpath == []:
        searchpath = ["/var/lib/snmp/mibs", "~/.mibs"]
    # if args.add_paths:
    #     searchpath += args.add_paths.split(",")
    global all_mib_files
    for path in searchpath:
        print("Searching in {}".format(path))
        full_path = os.path.expanduser(path)
        all_mib_files.update(get_all_mibs(Path(full_path)))
    for mib_name in all_mib_files:
        print("MIB: {}".format(mib_name))
        try:
            # global root_mib
            root_mib= RawMib("(root)")
            root_mib.add_item("iso", "", 1)
            global all_mibs
            all_mibs = [ root_mib ]
            global missing_imports
            missing_imports = {}
            global missed_mibs
            missed_mibs = set()
            load_mib_by_name(mib_name)
            global mibtree
            mibtree = Node("iso", ".1", "(root)")
            missing_items = set()
            for mib in all_mibs:
                # print("MIB: {}".format(mib.syntax))
                for item in mib.items:
                    # print("Item: {}".format(item.name))
                    if not add_item(mibtree, all_mibs, item):
                        if item.parent in missing_items:
                            missing_items.add(item.name)
                        elif item.parent in missing_imports:
                            print("Missing input: MIB file for {} is needed for resolving \"{} = {{ {} {} }}\" (and others in the same tree)".format(
                                missing_imports[item.parent], item.name, item.parent, item.index,
                            ))
                            missing_items.add(item.name)
                        else:
                            print("Missing input: parent {0} was not found for \"{1} = {{ {0} {2} }}\"".format(
                                item.parent, item.name, item.index,
                            ))
            retval = make_pyDocsis_Dict(mibtree, retval)
            print("here")
        except Exception as e:
            dammit = True
            # print("Error: {} on {}".format(e, mib_name))
    return(retval)



if __name__ == "__main__":
    rets = main()
    with open(os.path.expanduser('~/.mibs.json'), 'w') as f:
        json.dump(rets, f, indent=4)

