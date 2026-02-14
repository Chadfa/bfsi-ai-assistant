import json

base_data = []

loan_topics = [
    "personal loan eligibility",
    "home loan eligibility",
    "EMI schedule",
    "interest rate details",
    "loan foreclosure charges",
    "late payment penalty",
    "loan processing time",
    "credit score requirement",
    "application rejection reason",
    "account update process"
]

for i in range(15):
    for topic in loan_topics:
        entry = {
            "instruction": topic,
            "input": f"Can you explain {topic}?",
            "output": f"{topic.capitalize()} depends on bank policies and customer profile. Please refer to the official portal or contact support for accurate information."
        }
        base_data.append(entry)

with open("dataset/bfsi_alpaca.json", "w", encoding="utf-8") as f:
    json.dump(base_data, f, indent=2)

print("Dataset generated with", len(base_data), "entries.")
