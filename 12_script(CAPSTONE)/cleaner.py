import datetime

def csv_cleaner(data):
    seen = set()
    cleaned = []
    dateformat = "%Y-%m-%d %H:%M:%S"
    for row in data:
        # Validate Timestamp
        try:
            valid_ts = datetime.datetime.strptime(row["timestamp"],dateformat)
            row["timestamp"] = valid_ts
        except:
            continue

        # Validate Event
        if not row.get("event"):
            continue

        # Validate IP
        ip = row.get("ip")
        if not ip:
            ip = "UNKNOWN"
            row["ip"] = ip

        # Check for duplication, and append key if not duplicate
        key = (valid_ts,ip,row["event"])
        if key in seen:
            continue
        else:
            seen.add(key)

        # Store cleaned row
        cleaned.append(row)

    return cleaned
