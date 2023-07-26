#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file SendPoseDatapyTest.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import SendPoseDatapy

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
sendposedatapytest_spec = ["implementation_id", "SendPoseDatapyTest", 
         "type_name",         "SendPoseDatapyTest", 
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
# @class SendPoseDatapyTest
# @brief ModuleDescription
# 
# 
# </rtc-template>
class SendPoseDatapyTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_outPose = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
        """
        """
        self._outPoseIn = OpenRTM_aist.InPort("outPose", self._d_outPose)
        self._d_outMode = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._outModeIn = OpenRTM_aist.InPort("outMode", self._d_outMode)


        


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
        self.addInPort("outPose",self._outPoseIn)
        self.addInPort("outMode",self._outModeIn)
        
        # Set OutPort buffers
        
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
    
    #    ##
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
    
        return RTC.RTC_OK
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
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
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("SendPoseDatapyTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def SendPoseDatapyTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sendposedatapytest_spec)
    manager.registerFactory(profile,
                            SendPoseDatapyTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SendPoseDatapyTestInit(manager)
    SendPoseDatapy.SendPoseDatapyInit(manager)

    # Create a component
    comp = manager.createComponent("SendPoseDatapyTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

