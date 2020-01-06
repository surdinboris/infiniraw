# 1 Input  data. Preparation of configuration data - verifying system components type and amount
# could be JSON-like parsed hard card or something else

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

#3 addtional component descriptors for proper interface counting and other skybox/ibox depending stuff
nodeifs={'r740': {'ISCSI': 8, 'data': 6, 'sas': 4, 'IB': 2, 'power':2},
             'r730': {'ISCSI': 8, 'data': 4, 'sas': 4, 'IB': 2, 'power':2}}

enclosureifs = {'NDS-4600': {'IOM-A': 4, 'IOM-B': 4, 'power': 2}}

bbuifs = {'APC 1500': {'usb':1, 'eth': 1, 'power': 1, 'outlet': 1},
          'Eaton 5P UPS': {'usb': 1, 'eth': 1, 'power': 1, 'powoutlet': 2}}

# defining some base object class
class Component:
    def __init__(self, hwconfig):
        self.config = {}
        # self.subcomponents = {}
        for key in hwconfig:
            self.config[key] = hwconfig[key]

# it may be some specific factory depending by component type
# in case of automatic FC\DATA ports amount evaluation for nodes for example
# class Node():
#     def __init__(self, hwconfig):
#         self.config = {}
#         self.subcomponents = {}
#
#         for key in hwconfig:
#             self.config[key] = hwconfig[key]

#
# class Enclosure():
#     pass
# class Pdu():
#     pass



#creating testing objects
testingproc = {}

def createConfigInstances(systemConfig, comptype):
    print("Creating  {} equipment class  objects....".format(comptype.rstrip('s')))
    for component in systemConfig[comptype]:
        #possible scenario to build some mapping type to define which
        testingproc[component] = Component(systemConfig[comptype][component])


def createSystemConfig(systemConfig):
    for comptype in systemConfig:
        createConfigInstances(systemConfig, comptype)


createSystemConfig(systemConfig)

# print(testingproc)

def generateports(testingproc):
    for dev in testingproc.items():
        print(dev)

generateports(testingproc)
# for confobj in testingproc:
#     print(testingproc[confobj].__dict__. items())
# print(testingproc['bbu1'])