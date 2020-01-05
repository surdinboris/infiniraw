# 1 Preparation of configuration data frame - verifying system components type and amount

# 2 JSON-like parced hard card or something else
systemConfig = {
    'bbus': {
        'bbu1': {'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
        'bbu2': {'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
        'bbu3': {'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
    },
    'nodes': {
        'node1': {'model': 'r740', 'PN': 'SRV-10384-A'},
        'node2': {'model': 'r740', 'PN': 'SRV-10384-A'},
        'node3': {'model': 'r740', 'PN': 'SRV-10384-A'},
             },
    'enclosures': {
        'enc1': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc2': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc3': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc4': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc5': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc6': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc7': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enc8': {'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
    },
    'pdus': {
        'pdu1': {'model': 'AP8941', 'PN': 'PDU-00013-A'},
        'pdu2': {'model': 'AP8941',  'PN':'PDU-00013-A'},
        'pdu3': {'model': 'AP8941', 'PN': 'PDU-00013-A'},
        'pdu4': {'model': 'AP8941',  'PN':'PDU-00013-A'},
    }
}

# defining some base object class
class Component:
    def __init__(self, hwconfig):
        self.config = {}
        self.subcomponents = {}

        for key in hwconfig:
            self.config[key] = hwconfig[key]

# it may be some specific factory depending by component type
# in case of automatic FC\DATA ports amount evaluation for nodes for example
class Node():
    def __init__(self, hwconfig):
        self.config = {}
        self.subcomponents = {}

        for key in hwconfig:
            self.config[key] = hwconfig[key]
        self.fcports = {}
#
# class Enclosure():
#     pass
# class Pdu():
#     pass



#creating testing objects
testingproc = {}

def createConfigInstances(systemConfig, comptype):
    print("Creating {} class  objects....".format(comptype.rstrip('s')))
    for component in systemConfig[comptype]:
        #possible scenario to build some mapping type to define which
        testingproc[component] = Component(systemConfig[comptype][component])


def createSystemConfig(systemConfig):
    for comptype in systemConfig:
        createConfigInstances(systemConfig, comptype)


createSystemConfig(systemConfig)

print(testingproc)

# for confobj in testingproc:
#     print(testingproc[confobj].__dict__. items())
# print(testingproc['bbu1'])