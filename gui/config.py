'''
Modify this file to change GUI configuration
'''

# default parameter config file
config_path = ''

# fpga config
pid_bit_file = './pid_controller_Paladin_lock.bit' # path to hdl bit file
    # opal kelly serial number; leave blank to connect to first device found
serial = '14370009KG' #Red Chamber Serial
#serial = '13510007J1' #Green Chamber Serial
#serial = '14370009H5' #Common 1577 Serial
adc_clk_freq = 17 # adc serial frequency (max 17MHz)
sys_clk_freq = 50 # system clock frequency (max 50MHz)

# list of all hdl header files to parse
header_list = [ '../init.vh', '../ep_map.vh', '../parameters.vh']

