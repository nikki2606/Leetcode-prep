def ipList(logs):
    maxCount = 0
    ipDict = {}
    for log in logs:
        ip = log.split(" ")[0]
        if ip not in ipDict:
            ipDict[ip] = 0
        ipDict[ip] += 1
        maxCount = max(maxCount, ipDict[ip])
    
    res = []
    for ip, freq in ipDict.items():
        if freq == maxCount:
            res.append(ip)
    return res

example = ["10.0.0.1 - log entry 1 11", "10.0.0.1 - log entry 2 213", "10.0.0.2 - log entry 1 11", "10.0.0.2 - log entry 2 213", "10.0.0.2 - log entry 133132"]
print(ipList(example))