import os
import json
#import helper functions for lmnft
import launchmynft





def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())


#gets config
config = getConfig()

#if windows True, else False (mac, linux)
isWindows = True if os.name == 'nt' else False

#if mint on launchmynft.io
if "launchmynft.io" in config[0]:
    print("Found launchmynft.io link")
    launchmynft.mint(config, isWindows)

#if platform not supported
else:
    print("Could not recognize link")

