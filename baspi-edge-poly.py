#!/usr/bin/env python
"""
This is a NodeServer template for Polyglot v2 written in Python2/3
by Einstein.42 (James Milne) milne.james@gmail.com
BASpi-Edge 6U6R by Steven Bailey / Gerrod Bailey 
"""
try:
    import polyinterface
except ImportError:
    import pgc_interface as polyinterface
import sys


LOGGER = polyinterface.LOGGER

# Grab My Controller Node 
from nodes import BasEdgeController

if __name__ == "__main__":
    try:
        polyglot = polyinterface.Interface('BASpiEdge')
        polyglot.start()
        control = BasEdgeController(polyglot)
        control.runForever()
        
    except (KeyboardInterrupt, SystemExit):
        LOGGER.warning("Received interrupt or exit...")
        """
        Catch SIGTERM or Control-C and exit cleanly.
        """
        polyglot.stop()
    except Exception as err:
        LOGGER.error('Excption: {0}'.format(err), exc_info=True)
    sys.exit(0)
