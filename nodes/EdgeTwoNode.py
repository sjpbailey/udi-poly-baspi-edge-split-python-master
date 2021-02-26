
try:
    import polyinterface
except ImportError:
    import pgc_interface as polyinterface
import sys
import time
import urllib3
from bascontrolns import Device, Platform

LOGGER = polyinterface.LOGGER

class EdgeTwoNode(polyinterface.Node):
    def __init__(self, controller, primary, address, name, ipaddress2, bc2):
        super(EdgeTwoNode, self).__init__(controller, primary, address, name)
        self.lpfx = '%s:%s' % (address,name)
        self.ipaddress2 = (str(ipaddress2).upper()) #Device(str(ipaddress).upper())
        self.bc2 = bc2

    def start(self):
        if self.ipaddress2 is not None:
            self.bc2 = Device(self.ipaddress2)
                        
            ### BASpi-Edge One ###
            if self.bc2.ePlatform == Platform.BASC_NONE:
                LOGGER.info('Unable to connect')
                LOGGER.info('ipaddress')
            if self.bc2.ePlatform == Platform.BASC_PI:
                LOGGER.info('Connected to BASpi-6U6R Device Two')
            if self.bc2.ePlatform == Platform.BASC_ED:
                LOGGER.info('Connected to BASpi-Edge Device Two')    
                self.setDriver('ST', 1)    
            #LOGGER.info('IP Address for Controller 1' + self.ipaddress2)

            if self.bc2.ePlatform == Platform.BASC_ED:   
                LOGGER.info('Universal inputs in this BASpi-EDGE1' + '\t' + str(self.bc2.uiQty))
                LOGGER.info('Binary outputs in this BASpi-EDGE1' + '\t' + str(self.bc2.boQty))
            if self.bc2.ePlatform == Platform.BASC_PI:
                LOGGER.info('Universal inputs in this BASpi-6U6R' + '\t' + str(self.bc2.uiQty))
                LOGGER.info('Binary outputs in this BASpi-6U6R' + '\t' + str(self.bc2.boQty))
                

            # Input/Output Status
            LOGGER.info('UI 1' + '\t' + str(self.bc2.universalInput(1)))
            LOGGER.info('UI 2' + '\t' + str(self.bc2.universalInput(2)))
            LOGGER.info('UI 3' + '\t' + str(self.bc2.universalInput(3)))
            LOGGER.info('UI 4' + '\t' + str(self.bc2.universalInput(4)))
            LOGGER.info('UI 5' + '\t' + str(self.bc2.universalInput(5)))
            LOGGER.info('UI 6' + '\t' + str(self.bc2.universalInput(6)))
            LOGGER.info('BO 1' + '\t' + str(self.bc2.binaryOutput(1)))
            LOGGER.info('BO 2' + '\t' + str(self.bc2.binaryOutput(2)))
            LOGGER.info('BO 3' + '\t' + str(self.bc2.binaryOutput(3)))
            LOGGER.info('BO 4' + '\t' + str(self.bc2.binaryOutput(4)))
            LOGGER.info('BO 5' + '\t' + str(self.bc2.binaryOutput(5)))
            LOGGER.info('BO 6' + '\t' + str(self.bc2.binaryOutput(6)))
            
            ### Universal Inputs ###
            input_one = self.bc2.universalInput(1)
            input_two = self.bc2.universalInput(2)
            input_thr = self.bc2.universalInput(3)
            input_for = self.bc2.universalInput(4)
            input_fiv = self.bc2.universalInput(5)
            input_six = self.bc2.universalInput(6)

            # Binary/Digital Outputs
            output_one = (self.bc2.binaryOutput(1))
            output_two = (self.bc2.binaryOutput(2))
            output_tre = (self.bc2.binaryOutput(3))
            output_for = (self.bc2.binaryOutput(4))
            output_fiv = (self.bc2.binaryOutput(5))
            output_six = (self.bc2.binaryOutput(6))
                        
            self.setDriver('GV0', input_one, force=True)
            self.setDriver('GV1', input_two, force=True)
            self.setDriver('GV2', input_thr, force=True)
            self.setDriver('GV3', input_for, force=True)
            self.setDriver('GV4', input_fiv, force=True)
            self.setDriver('GV5', input_six, force=True)

            # Binary/Digital Outputs
            self.setDriver('GV6', output_one, force=True)
            self.setDriver('GV7', output_two, force=True)
            self.setDriver('GV8', output_tre, force=True)
            self.setDriver('GV9', output_for, force=True)
            self.setDriver('GV10', output_fiv, force=True)
            self.setDriver('GV11', output_six, force=True)
           
               
    # Output 1
    def setOn1(self, command):
        if self.bc2.binaryOutput(1) != 1:
            self.bc2.binaryOutput(1, 1)
            self.setDriver("GV6", 1) 
            LOGGER.info('Output 1 On')   
            
    def setOff1(self, command):
        if self.bc2.binaryOutput(1) == 1:
            self.bc2.binaryOutput(1, 0)
            self.setDriver("GV6", 0) 
            LOGGER.info('Output 1 Off')

    # Output 2
    def setOn2(self, command):
        if self.bc2.binaryOutput(2) != 1:
            self.bc2.binaryOutput(2,1)
            self.setDriver("GV7", 1) 
            LOGGER.info('Output 2 On')
    
    def setOff2(self, command):
        if self.bc2.binaryOutput(2) != 0:
            self.bc2.binaryOutput(2,0)
            self.setDriver("GV7", 0) 
            LOGGER.info('Output 2 Off')         
    # Output 3
    def setOn3(self, command):
        if self.bc2.binaryOutput(3) != 1:
            self.bc2.binaryOutput(3,1)
            self.setDriver("GV8", 1) 
            LOGGER.info('Output 3 On')
    
    def setOff3(self, command):
        if self.bc2.binaryOutput(3) != 0:
            self.bc2.binaryOutput(3,0)
            self.setDriver("GV8", 0) 
            LOGGER.info('Output 3 Off')
    # Output 4
    def setOn4(self, command):
        if self.bc2.binaryOutput(4) != 1:
            self.bc2.binaryOutput(4,1)
            self.setDriver("GV9", 1) 
            LOGGER.info('Output 4 On')
    
    def setOff4(self, command):
        if self.bc2.binaryOutput(4) != 0:
            self.bc2.binaryOutput(4,0)
            self.setDriver("GV9", 0) 
            LOGGER.info('Output 4 Off')
    # Output 5
    def setOn5(self, command):
        if self.bc2.binaryOutput(5) != 1:
            self.bc2.binaryOutput(5,1)
            self.setDriver("GV10", 1) 
            LOGGER.info('Output 5 On')
    
    def setOff5(self, command):
        if self.bc2.binaryOutput(5) != 0:
            self.bc2.binaryOutput(5,0)
            self.setDriver("GV10", 0) 
            LOGGER.info('Output 5 Off')
    # Output 6
    def setOn6(self, command):
        if self.bc2.binaryOutput(6) != 1:
            self.bc2.binaryOutput(6,1)
            self.setDriver("GV11", 1) 
            LOGGER.info('Output 6 On')
    
    def setOff6(self, command):
        if self.bc2.binaryOutput(6) != 0:
            self.bc2.binaryOutput(6,0)
            self.setDriver("GV11", 0) 
            LOGGER.info('Output 6 Off')
    
    def shortPoll(self):
        LOGGER.debug('shortPoll')
        #if int(self.getDriver('ST')) == 1:
        #    self.setDriver('ST',0)
        #else:
        #    self.setDriver('ST',1)
        #LOGGER.debug('%s: get ST=%s',self.lpfx,self.getDriver('ST'))

    def longPoll(self):
        LOGGER.debug('longPoll')
   
    def cmd_ping(self,command):
        LOGGER.debug("cmd_ping:")
        r = self.http.request('GET',"google.com")
        LOGGER.debug("cmd_ping: r={}".format(r))


    def query(self,command=None):
        self.reportDrivers()

    "Hints See: https://github.com/UniversalDevicesInc/hints"
    hint = [1,2,3,4]
    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 2},
        {'driver': 'GV0', 'value': 1, 'uom': 56},
        {'driver': 'GV1', 'value': 1, 'uom': 56},
        {'driver': 'GV2', 'value': 1, 'uom': 56},
        {'driver': 'GV3', 'value': 1, 'uom': 56},
        {'driver': 'GV4', 'value': 1, 'uom': 56},
        {'driver': 'GV5', 'value': 1, 'uom': 56},
        {'driver': 'GV6', 'value': 1, 'uom': 80},
        {'driver': 'GV7', 'value': 1, 'uom': 80},
        {'driver': 'GV8', 'value': 1, 'uom': 80},
        {'driver': 'GV9', 'value': 1, 'uom': 80},
        {'driver': 'GV10', 'value': 1, 'uom': 80},
        {'driver': 'GV11', 'value': 1, 'uom': 80},
        ]
    """
    Optional.
    This is an array of dictionary items containing the variable names(drivers)
    values and uoms(units of measure) from ISY. This is how ISY knows what kind
    of variable to display. Check the UOM's in the WSDK for a complete list.
    UOM 2 is boolean so the ISY will display 'True/False'
    """
    id = 'baspiedge2_id'
    """
    id of the node from the nodedefs.xml that is in the profile.zip. This tells
    the ISY what fields and commands this node has.
    """
    commands = {
                    'BON1': setOn1,
                    'BOF1': setOff1,
                    'BON2': setOn2,
                    'BOF2': setOff2,
                    'BON3': setOn3,
                    'BOF3': setOff3,
                    'BON4': setOn4,
                    'BOF4': setOff4,
                    'BON5': setOn5,
                    'BOF5': setOff5,
                    'BON6': setOn6,
                    'BOF6': setOff6,
                    'QUERY': query,
                    'PING': cmd_ping
                }
    """
    This is a dictionary of commands. If ISY sends a command to the NodeServer,
    this tells it which method to call. DON calls setOn, etc.
    """
