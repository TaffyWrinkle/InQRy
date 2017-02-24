import platform
import yaml
from inqry import system_profiler

# import sys
# if sys.platform == 'win32':
#   import win32_sysinfo as sysinfo
# elif sys.platform == 'darwin':
#   import mac_sysinfo as sysinfo
# elif 'linux' in sys.platform:
#   import linux_sysinfo as sysinfo
#  etc

class SystemSpecs(object):
    """Represents the machine's system specifications before it's data is used
    to form an asset object.

    A SystemSpecs object should be able to be used to access several system
    profile specs, even if they are not used by the Asset class.

    A SystemSpecs object should also be able to be used the same way,
    regardless of which operating system the specs were generated from"""

    def __init__(self):
        """TODO"""
        self.os_type = platform.system()

    def operating_system(self):
        if self.os_type == 'Darwin':
            mac_hardware()
        elif self.os_type == 'Windows':
            windows()
        else:
            raise OSError(
                '{os}: Unknown operating system'.format(os=self.os_type))

    def storage(self):
        pass

    @property
    def serial(self):
        # assert isinstance(serial, str)
        return mac_hardware().get('Serial Number (system)')

    @property
    def cpu_name(self):
        name = mac_hardware().get('Processor Name')
        assert isinstance(name, str)
        return name

    @property
    def cpu_processors(self):
        processors = mac_hardware().get('Number of Processors')
        assert isinstance(processors, int)
        return processors

    @property
    def cpu_cores(self):
        cores = mac_hardware().get('Total Number of Cores')
        assert isinstance(cores, int)
        return cores

    @property
    def cpu_speed(self):
        speed = mac_hardware().get('Processor Speed')
        assert isinstance(speed, str)
        return speed

    @property
    def memory(self):
        memory = mac_hardware().get('Memory')
        return memory

    @property
    def model(self):
        model = mac_hardware().get('Model Identifier')
        return model

    @property
    def name(self):
        name = mac_hardware().get('Model Name')
        return name


def mac_hardware():
    return system_profiler.hardware()


def mac_storage():
    """
    This function is used as the primary means of obtaining a Mac's
    physical storage information.
    """
    pass


def windows():
    """
    This function is used as the primary means of obtaining basic Windows
    machine hardware components.
    """
    pass


def _mac_system_profiler():
    return yaml.load(system_profiler.hardware())
