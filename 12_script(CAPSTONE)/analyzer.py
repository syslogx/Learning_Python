import datetime
def analyze_data(data):
    event_counter = {}
    ip_counter = {}
    for row in data:
        event = row["event"]
        ip = row["ip"]
        # Count events
        if event in event_counter:
            event_counter[event] +=1
        else:
            event_counter[event] = 1
        # Count IPs
        if ip in ip_counter:
            ip_counter[ip] += 1
        else:
            ip_counter[ip] = 1

    # Sort counter entries
    event_counter = dict(sorted(event_counter.items(),key=lambda x: x[1], reverse=True))
    ip_counter = dict(sorted(ip_counter.items(),key=lambda x: x[1], reverse=True))
    return dict(event_counter), dict(ip_counter)
