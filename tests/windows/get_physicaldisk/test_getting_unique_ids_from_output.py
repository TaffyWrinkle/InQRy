from inqry.system_specs import win_physical_disk

UNIQUE_ID_OUTPUT = """
UniqueId
--------
{256a2559-ce63-5434-1bee-3ff629daa3a7}
{4069d186-f178-856e-cff3-ba250c28446d}
{4da19f06-2e28-2722-a0fb-33c02696abcd}
50014EE20D887D66
eui.0025384161B6798A
5000C5007A75E216
500A07510F1A545C
ATA     LITEONIT LMT-256M6M mSATA 256GB         TW0XXM305508532M0705
IDE\Diskpacker-virtualbox-iso-1421140659-disk1__F.R7BNPC\5&1944dbef&0&0.0.0:vagrant-2012-r2
"""


def test_creating_list_of_unique_disk_ids():
    expected_physical_disks = {'{256a2559-ce63-5434-1bee-3ff629daa3a7}',
                               '{4069d186-f178-856e-cff3-ba250c28446d}',
                               '{4da19f06-2e28-2722-a0fb-33c02696abcd}',
                               '50014EE20D887D66',
                               'eui.0025384161B6798A',
                               '5000C5007A75E216',
                               '500A07510F1A545C',
                               'ATA     LITEONIT LMT-256M6M mSATA 256GB         TW0XXM305508532M0705',
                               "IDE\Diskpacker-virtualbox-iso-1421140659-disk1__F.R7BNPC\5&1944dbef&0&0.0.0:vagrant-2012-r2"}
    assert expected_physical_disks == set(win_physical_disk.get_physical_disk_identifiers(UNIQUE_ID_OUTPUT))
