edges = [
    {"source": "Engineering_PC", "target": "HMI_1", "protocol": "HTTP", "port": 80, "risk": 0.3},
    {"source": "Engineering_PC", "target": "Historian", "protocol": "HTTPS", "port": 443, "risk": 0.2},
    {"source": "HMI_1", "target": "PLC_1", "protocol": "PROFINET", "port": 34964, "risk": 1.5},
    {"source": "HMI_1", "target": "PLC_2", "protocol": "CIP", "port": 44818, "risk": 0.9},
    {"source": "PLC_1", "target": "Valve_1", "protocol": "Analog I/O", "risk": 2.0},
    {"source": "PLC_2", "target": "Motor_1", "protocol": "Digital I/O", "risk": 0.5}
]
