

filterGroups = ["1.3.6.1.2.1.69.1.6.2.1"]

class FilterGroup(object):
	self.index = 0


class IpFilterGroup(FilterGroup):
	self.source = ""
	self.destination = ""
	self.sourcePorts = []
	self.destinationPorts = []
	self.protocol = ""
	self.direction = ""
	