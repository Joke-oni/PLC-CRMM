import streamlit as st
import pandas as pd

# Set page config (No boring interface!)
st.set_page_config(layout="wide", page_title="PLC Attack Tracker", page_icon="🔐")

# Title with style
st.markdown("<h1 style='color: red;'>Naija PLC Security Dashboard</h1>", unsafe_allow_html=True)

# Sample Data - Replace with your Excel!
attacks = {
    "Attack": ["Modbus Hack", "Cisco Crash", "SCADA Virus"],
    "Source IP": ["192.168.1.1", "10.0.0.2", "172.16.0.3"],
    "Severity": ["🔥 Critical", "⚠️ High", "⚠️ High"],
    "Action": ["BLOCK PORT", "THROTTLE", "ISOLATE"]
}

# Display Attack Table
st.dataframe(pd.DataFrame(attacks), height=200, use_container_width=True)

# Buttons for Actions
if st.button("🚨 Block Modbus Attack", type="primary"):
    st.error("Port 502 don block for PLC1!")

if st.button("🛡️ Throttle Cisco Traffic"):
    st.warning("Traffic don reduce for 60 seconds")

# Network Graph (Simple but mighty!)
st.graphviz_chart('''
digraph {
    Attacker -> PLC1 [label="Hack"]
    PLC1 -> Firewall [label="Block"]
}
''')

# Footer
st.markdown("---")
st.write("© 2024 - No Scam, Just Code")
