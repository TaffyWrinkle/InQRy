import subprocess
from xml.etree.ElementTree import parse


def xml_data(hardware_property):
    output = subprocess.call(
        ["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
         "Get-CimInstance", hardware_property, "|",
         "ConvertTo-XML", "-As", "String"])
    print(output)