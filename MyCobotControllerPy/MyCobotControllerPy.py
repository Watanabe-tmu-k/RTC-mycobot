#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file MyCobotControllerPy.py
 @brief MyCobotControllerPy
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import Mycobot
import os
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
sys.path.append(os.path.dirname(__file__))
from pymycobot.port_setup import setup

#global
mycobot: MyCobot


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
mycobotcontrollerpy_spec = ["implementation_id", "MyCobotControllerPy", 
         "type_name",         "MyCobotControllerPy", 
         "description",       "MyCobotControllerPy", 
         "version",           "1.0.0", 
         "vendor",            "TMU", 
         "category",          "Robot", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class MyCobotControllerPy
# @brief MyCobotControllerPy
# 
# 
# </rtc-template>
class MyCobotControllerPy(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_inPose = OpenRTM_aist.instantiateDataType(RTC.TimedFloatSeq)
        """
        """
        self._inPoseIn = OpenRTM_aist.InPort("inPose", self._d_inPose)
        self._d_inMode = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._inModeIn = OpenRTM_aist.InPort("inMode", self._d_inMode)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>

    old_mode = 0
		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("inPose",self._inPoseIn)
        self.addInPort("inMode",self._inModeIn)
		
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

        global mycobot
        mycobot = setup()
        #mycobot.set_gripper_ini()
        nowcoords = mycobot.get_coords()
        print("::get_coords() ==> coords {}\n".format(nowcoords))

        reset = [-140, -60, 180, -90, 45, 90]
        self.old_mode = 0

        #reset = [0, 0, 300, 0, 0, 0]
        mycobot.send_coords(reset, 40, 0)
        time.sleep(3)

        #mycobot.set_gripper_ini()
        #print("::get_coords() ==> coords {}\n".format(mycobot.get_coords()))
        mycobot.set_gripper_value(50, 70)
        #print("::get_gripper_value() ==> {}\n".format(mycobot.get_gripper_value()))
        time.sleep(3)
    
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

        coords = [48.9, -67.0, 405.2, 101.1, -41.89, 77.92]
        mycobot.send_coords(coords, 30, 0)
        #mycobot.set_gripper_value(2048, 70)
        time.sleep(3)
        mycobot.set_gripper_value(50, 30)
        time.sleep(3)
    
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

        #print(mycobot.is_moving())
        if self._inPoseIn.isNew():
            data = self._inPoseIn.read()
            print("[MYCOBOT ARM] data {}".format(data))
            input = [data.data[0], data.data[1], data.data[2]]
            if input[0] < -200:
                input[0] = -200
            if input[0] > -140:
                input[0] = -140
            if input[1] < -120:
                input[1] = -120
            #if input[1] > 100:
            #    input[1] = 100
            if input[2] > 200:
                input[2] = 200            

            coords = [input[0], input[1], input[2], -90, 45, 90]
            #coords = [-4.9, -19.3, 412.2, 90.35, -14.19, -164.88]
            #coords = [posedata[0], posedata[1], posedata[2], 91, -74, 26]
            #-116.2, -21.3, 298.6, 90.24, -14.26, -164.94
            try:
                if len(coords) != 6:
                    raise Exception('')
                mycobot.send_coords(coords, 40, 0)
                print("::send_coords() ==> send coords {}, speed 40, mode 0".format(coords))
            except Exception:
                print('[MYCOBOT ARM] Error: invalid angles string.')
                #break
            time.sleep(0.5)

        if self._inModeIn.isNew():
            mode = self._inModeIn.read()
            print("[MYCOBOT GRIPPER] data {}".format(mode))
            if self.old_mode != mode.data:
                if mode.data == 0:
                    #mycobot.set_gripper_state(0, 50)
                    mycobot.set_gripper_value(90, 90)
                    self.old_mode = 0
                    print("[MYCOBOT GRIPPER] Open")
                    time.sleep(2)
                elif mode.data == 1:
                    #mycobot.set_gripper_state(1, 50)
                    mycobot.set_gripper_value(36, 90)
                    self.old_mode = 1
                    print("[MYCOBOT GRIPPER] Closed")
                    time.sleep(2)
                #else:



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
	



def MyCobotControllerPyInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=mycobotcontrollerpy_spec)
    manager.registerFactory(profile,
                            MyCobotControllerPy,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MyCobotControllerPyInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("MyCobotControllerPy" + args)

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

