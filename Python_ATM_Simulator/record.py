import json

def load_record():
    try:
        with open("record.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "balance": 0,
            "deposite": [],
            "withdraw": []
        }

def save_record(data):
    with open("record.json", "w") as f:
        json.dump(data, f, indent=4)
