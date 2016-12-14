from ctypes import *


class Api(Structure):
    _fields_ = [
        ("Major", c_int16),
        ("Minor", c_int16),
        ("Bugfix", c_int16)]

class Driver(Structure):
    _fields_ = [
        ("Major", c_int16),
        ("Minor", c_int16),
        ("Bugfix", c_int16)]

class ADMXRC3_VERSION_INFO(Structure):
    _fields_ = [("Api",Api ),
                ("Driver",Driver)]


class Get_api(object):
      def __init__(self):
          self.version=CDLL('/home/lnt/workspace/python_libs/info.so')
#          self.version=CDLL('/home/user/Ravi/admpcie8v3_sdk-1.0.0/host/util-v1_9_0/proj/linux/info/info.so')
          self.python_info_init = self.version.init
          self.python_info_lib_version = self.version.get_version_info
'''
          self.python_info_serial_number = self.version.get_api_serial_number         
          self.python_info_api_model = self.version.get_api_model
	  self.python_info_dma_channels = self.version.get_api_DMA_channels
	  self.python_info_target_fpga = self.version.get_api_target_fpga
	  self.python_info_num_sensors = self.version.get_api_num_sensors
  	  self.python_info_mem_banks = self.version.get_api_mem_banks
	  self.python_info_bak_presence_bitmap = self.version.get_api_bak_presence_bitmap    
          self.python_info_api_mem_bank0=self.version.get_api_mem_bank0_info
          self.python_info_api_mem_bank1=self.version.get_api_mem_bank1_info
          self.python_info_api_bus_window0=self.version.get_api_bus_window0_info
          self.python_info_api_bus_window1=self.version.get_api_bus_window1_info
          self.python_info_api_bus_window2=self.version.get_api_bus_window2_info
          self.python_info_api_bus_window3=self.version.get_api_bus_window3_info    
#	  self.m = self.python_info_init()
'''
#version = ctypes.cdll.LoadLibrary('/home/user/Ravi/python_libs/info.so')
test_obj = Get_api()

print "***********************INIT CALL*******"
#init_val = test_obj.python_info_init()
init_val = test_obj.version.init()

print "***********************LIB VERSION*******"
smb_request = ADMXRC3_VERSION_INFO()
smb_request.Api = (0,0,0)
smb_request.Driver = (0,0,0)

#smbus_read_byte1 = test_obj.python_info_lib_version()
smbus_read_byte=test_obj.version.get_version_info
#print smbus_read_byte

#simbus_read_byte = test_obj.version.get_version_info
smbus_read_byte.argtypes=[]
smbus_read_byte.restype=POINTER(ADMXRC3_VERSION_INFO)
smb_request = smbus_read_byte().contents

print "Api version:%ld.%ld.%ld" % (smb_request.Api.Major,smb_request.Api.Minor,smb_request.Api.Bugfix)
print "Driver version:%ld.%ld.%ld" % (smb_request.Driver.Major,smb_request.Driver.Minor,smb_request.Driver.Bugfix)

print "************************SERIAL NUMBER************"
smb_request = ADMXRC3_VERSION_INFO()
smb_request.Api = (0,0,0)
smb_request.Driver = (0,0,0)
smbus_read_byte=test_obj.version.get_version_info
smbus_read_byte.argtypes=[]
smbus_read_byte.restype=POINTER(ADMXRC3_VERSION_INFO)
smb_request = smbus_read_byte().contents
print "Api version:%ld.%ld.%ld" % (smb_request.Api.Major,smb_request.Api.Minor,smb_request.Api.Bugfix)
print "Driver version:%ld.%ld.%ld" % (smb_request.Driver.Major,smb_request.Driver.Minor,smb_request.Driver.Bugfix)



#smbus_read_byte.argtypes = []
#print type(smbus_read_byte)
'''
smb_request = smbus_read_byte().contents

print "Api version:%ld.%ld.%ld" % (smb_request.Api.Major,smb_request.Api.Minor,smb_request.Api.Bugfix)
print "Driver version:%ld.%ld.%ld" % (smb_request.Driver.Major,smb_request.Driver.Minor,smb_request.Driver.Bugfix)

#print c_char_p(lib_ver).value

print "*******************API_MODEL***********"
api_model = test_obj.python_info_api_model()
print c_char_p(api_model).value

print "*********DMA_CHANNELS*********************"
dma_channel = test_obj.python_info_dma_channels()
print c_int(dma_channel).value

print "**********API_SERIAL_NUMBER***************"
serial_number=test_obj.python_info_serial_number()
print c_int(serial_number).value

print "*********API_TARGET_FPGA*****************"
target_fpga=test_obj.python_info_target_fpga()
print c_int(target_fpga).value

print "***********API_NUMBER_SENSORS***********"
num_sensors=test_obj.python_info_num_sensors()
print c_int(num_sensors).value

print "**********API_MEM_SENSORS**************"
mem_banks=test_obj.python_info_mem_banks()
print c_int(mem_banks).value

print "*********BAK_PRESENCE_BITMAP************"
bak_presence=test_obj.python_info_bak_presence_bitmap()
print c_int(bak_presence).value

print "**********************MEM BANK0 INFO*******"
bank0_info = test_obj.python_info_api_mem_bank0()
print c_char_p(bank0_info).value

print "******************MEM_BANK1_INFO******"
bank1_info = test_obj.python_info_api_mem_bank1()
print c_char_p(bank1_info).value

print "***********************BUS_WINDOW0 INFO*******"
window0Info = test_obj.python_info_api_bus_window0()
print c_char_p(window0Info).value

print "***********************BUS_WINDOW1 INFO*******"
window1Info = test_obj.python_info_api_bus_window1()
print c_char_p(window1Info).value

 
print "***********************BUS_WINDOW2 INFO*******"
window2Info = test_obj.python_info_api_bus_window2()
print c_char_p(window2Info).value

print "***********************BUS_WINDOW3 INFO*******"
window3Info = test_obj.python_info_api_bus_window3()
print c_char_p(window3Info).value
'''

