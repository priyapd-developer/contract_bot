import json, datetime

def log_action(filename):
    entry = {
        "file": filename,
        "time": str(datetime.datetime.now())
    }
    try:
        data = json.load(open("audit_log.json"))
    except:
        data = []
    data.append(entry)
    json.dump(data, open("audit_log.json","w"), indent=2)
