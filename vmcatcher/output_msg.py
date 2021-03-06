import logging
from vmcatcher.outputbase import output_driver_base
from vmcatcher.outputbase import output_driver_lister
from vmcatcher.outputbase import output_driver_lister
from vmcatcher.outputbase import output_driver_display_metadata
        
from vmcatcher.outputbase import output_driver_display_message
from smimeX509validation import TrustStore, LoadDirChainOfTrust,smimeX509validation, smimeX509ValidationError


class output_driver_message(output_driver_display_message,output_driver_lister,output_driver_base):
    def __init__(self):
        output_driver_base.__init__(self)
        output_driver_lister.__init__(self)
        output_driver_display_message.__init__(self)
        self.log = logging.getLogger("output_driver_message")
    def display_ImageListInstance(self,imagelist):
        smimeProcessor =  smimeX509validation(self.x509anchor)
        try:
            smimeProcessor.Process(str(imagelist.data))
        except smimeX509ValidationError,E:
            self.log.error("Failed to validate text for '%s' produced error '%s'" % (imagelist,E))
            return False
        if not smimeProcessor.verified:
            self.log.error("Failed to validate text for '%s' produced error '%s'" % (subscriptionKey,E))
            return False
        self.fpOutput.write (smimeProcessor.InputDaraStringIO.getvalue())
        return True
    
    def info(self, *args, **kwargs):
        expectedkeys = set([
                "Endorser",
                "EndorserPrincible",
                "ImageDefinition",
                "ImageInstance",
                "ImageListInstance",
                "Subscription",
                "SubscriptionAuth",
                ])
        
        found = set(kwargs.keys())
        if "ImageListInstance" in found:
            argImageInstance = kwargs.get('ImageListInstance', None)
            
            return self.display_ImageListInstance(argImageInstance)
        return False
