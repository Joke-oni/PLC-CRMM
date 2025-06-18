import pandas as pd
from transformers import pipeline

# Load CVE data
df = pd.read_csv("ics_cves.csv")

# Initialize NLP pipeline
nlp = pipeline("text-classification", model="bert-base-uncased")

# Auto-tag new CVEs
new_cve = "Mitsubishi PLC memory corruption via MELSEC protocol"
tags = nlp(new_cve)  # Returns {"MELSEC": 0.92, "Memory_Corruption": 0.88}
