from pydocsis.cmConfig import CmConfig
from pydocsis.configFile import ConfigFile


def test_get_config():
    file = "DCTR3.cfg"
    this_config = ConfigFile()
    this_config.configFilePath = file
    this_config = this_config.get_config()
    assert isinstance(this_config, CmConfig)
