#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file SendPoseDatapy.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
sendposedatapy_spec = ["implementation_id", "SendPoseDatapy", 
         "type_name",         "SendPoseDatapy", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.coord_x", "-140",
         "conf.default.coord_y", "-60",
         "conf.default.coord_z", "180",
         "conf.default.mode", "0",

         "conf.__widget__.coord_x", "slider.1",
         "conf.__widget__.coord_y", "slider.1",
         "conf.__widget__.coord_z", "slider.1",
         "conf.__widget__.mode", "radio",
         "conf.__constraints__.coord_x", "-250<x<-100",
         "conf.__constraints__.coord_y", "-180<x<120",
         "conf.__constraints__.coord_z", "0<x<250",
         "conf.__constraints__.mode", "(0,1,-1)",

         "conf.__type__.coord_x", "float",
         "conf.__type__.coord_y", "float",
         "conf.__type__.coord_z", "float",
         "conf.__type__.mode", "short",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class SendPoseDatapy
# @brief ModuleDescription
# 
# 
# </rtc-template>
class SendPoseDatapy(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_outPose = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
        """
        """
        self._outPoseOut = OpenRTM_aist.OutPort("outPose", self._d_outPose)
        self._d_outMode = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._outModeOut = OpenRTM_aist.OutPort("outMode", self._d_outMode)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  x
         - DefaultValue: -140
        """
        self._x = [-140]
        """
        
         - Name:  y
         - DefaultValue: -60
        """
        self._y = [-60]
        """
        
         - Name:  z
         - DefaultValue: 180
        """
        self._z = [180]
        """
        
         - Name:  mode
         - DefaultValue: 0
        """
        self._mode = [0]
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("coord_x", self._x, "-140")
        self.bindParameter("coord_y", self._y, "-60")
        self.bindParameter("coord_z", self._z, "180")
        self.bindParameter("mode", self._mode, "0")
		
        # Set InPort buffers
		
        # Set OutPort buffers
        self.addOutPort("outPose",self._outPoseOut)
        self.addOutPort("outMode",self._outModeOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):

        pose = [0.0 for j in range(3)]
        pose[0] = self._x[0]
        pose[1] = self._y[0]
        pose[2] = self._z[0]
        OpenRTM_aist.setTimestamp(self._d_outPose)
        self._d_outPose.data = pose
        self._outPoseOut.write()
        
        OpenRTM_aist.setTimestamp(self._d_outMode)
        self._d_outMode.data = self._mode[0]
        self._outModeOut.write()

        print("[SEND POSE]{}".format(self._d_outPose.data))
        print("[SEND MODE]{}".format(self._d_outMode.data))
        #print(self._d_outpose)
        #data = self._outposeOut.read()
        #print(data)
        time.sleep(0.2)
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def SendPoseDatapyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sendposedatapy_spec)
    manager.registerFactory(profile,
                            SendPoseDatapy,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SendPoseDatapyInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("SendPoseDatapy" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

