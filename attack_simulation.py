# Modbus attack simulation
from pymodbus.client import ModbusTcpClient

def simulate_attack():
    client = ModbusTcpClient('192.168.1.20')  # PLC_1
    client.write_register(0, 1000)  # Malicious valve command
    print("Sent attack to S7-1500 PLC")

# RL agent response
def mitigate_attack():
    os.system("ovs-ofctl add-flow br0 priority=300,dl_type=0x0800,nw_src=192.168.1.10,actions=drop")
    print("Isolated HMI_1 VLAN")
