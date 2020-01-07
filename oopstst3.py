# 1 Input  data. Preparation of configuration data - verifying system components type and amount
# could be JSON-like parsed hard card or something else

systemConfig = {
    'bbus': {
        'bbu1': {'devtype': 'bbu', 'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
        'bbu2': {'devtype': 'bbu', 'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
        'bbu3': {'devtype': 'bbu', 'model': 'Eaton 5P UPS', 'PN': 'BBU-00002-A'},
    },
    'nodes': {
        'node1': {'devtype': 'node', 'model': 'r730', 'PN': 'SRV-10384-A'},
        'node2': {'devtype': 'node', 'model': 'r740', 'PN': 'SRV-10384-A'},
        'node3': {'devtype': 'node', 'model': 'r740', 'PN': 'SRV-10384-A'},
    },
    'enclosures': {
        'enclosure1': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure2': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure3': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure4': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure5': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure6': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure7': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
        'enclosure8': {'devtype': 'enclosure', 'model': 'NDS-4600', 'PN': 'ENC-00001-A'},
    },
    'pdus': {
        'pdu1': {'devtype': 'pdu', 'model': 'AP8941', 'PN': 'PDU-00013-A'},
        'pdu2': {'devtype': 'pdu', 'model': 'AP8941', 'PN': 'PDU-00013-A'},
        'pdu3': {'devtype': 'pdu', 'model': 'AP8941', 'PN': 'PDU-00013-A'},
        'pdu4': {'devtype': 'pdu', 'model': 'AP8941', 'PN': 'PDU-00013-A'},
    }
}

# 3 addtional component descriptors for proper interface counting and other skybox/ibox depending stuff
portConfig = {
    'node': {'r740': {'ISCSI': 8, 'data': 6, 'sas': 4, 'IB': 2, 'powerin': 2},
             'r730': {'ISCSI': 8, 'data': 4, 'sas': 4, 'IB': 2, 'powerin': 2}},

    'enclosure': {'NDS-4600': {'IOM-A': 4, 'IOM-B': 4, 'powerin': 2}},

    'bbu': {'APC 1500': {'usb': 1, 'eth': 1, 'powerin': 1, 'powoutlet': 1},
            'Eaton 5P UPS': {'usb': 1, 'eth': 1, 'powerin': 1, 'powoutlet': 2}},

    'pdu': {'AP8941': {'eth': 1}}
}

#factory\container  class
class System:
    def __init__(self,systemConfig, portConfig):
        # modules = testingproc['modules']
        for componentsection, componentlist in systemConfig.items():
            print("Creating {} modules class  objects....".format(componentsection.rstrip('s')))
            for componentname, componentprefs in componentlist.items():
                devtype = componentprefs["devtype"]
                devmodel = componentprefs["model"]
                self.addcomponent({componentname: Port(componentprefs, portConfig[devtype][devmodel])})

    def addcomponent(self, component):
        self.__dict__.update(component)
    def getbbuports(self,bbu):
        return self.__dict__[bbu].ports


# defining some base object class
class Component:
    def __init__(self, hwconfig):
        # self.config = {}
        # self.subcomponents = {}
        for key in hwconfig:
            # dynamically creating attributes accessible as properties
            self.__dict__.update({key: hwconfig[key]})

    def getportsbyfamily(self,portfamily):
        return self.__dict__.items()

#port subclass
class Port(Component):
    def __init__(self, hwconfig, portconf):
        self.ports={}
        for portfamily, portamount in portconf.items():
            for port in range(1,portamount+1):
                portid='{}{}'.format(portfamily, port)
                self.ports.update({portid: {'results': {}}})
                Component.__init__(self, hwconfig)

    def getportsbyfamily(self,portfamily):
        return self.__dict__.items()

system = System(systemConfig, portConfig)

#testing
print(system.getbbuports('bbu1'))
print(system.bbu1.PN)
print(system.node3.model)