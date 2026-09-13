

def check_health(value):
    if value >= 90:
        return "CRITICAL"
    elif value >= 70:
        return "WARNING"
    else:
        return "OK"
