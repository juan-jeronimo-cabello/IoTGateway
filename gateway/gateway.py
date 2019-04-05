import json
import os
import sys

__configurationFile__ = ".\gateway\config.json"

##Class that implmentes the Field gateway as a whole
class Gateway:
    # Method to load the configuration from a json file
    def loadConfiguration(self, config):
        with open(config) as configFileStr:
            self.configuration = json.load(configFileStr)
            configFileStr.close()
    
    #Initializes the message buffer, sends startup event to the hub and starts main loop 
    #def startup(self):
        
    
    #Compiles messages and sends events to the hub
    #def sendEvents(self):
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide the path to the configuration file as argument")
    else:
        gw = Gateway()
        #gw.loadConfiguration(__configurationFile__)
        gw.loadConfiguration(sys.argv[1])
        print(gw.configuration)

