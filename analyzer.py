def analyze():
    with open("sample.log", "r") as f:
        count_error = 0
        count_warning = 0
        count_info = 0
        for stroka in f:
            if "ERROR" in stroka:
                count_error += 1
            elif "WARNING" in stroka:
                count_warning += 1
            elif "INFO" in stroka:
                count_info += 1
        return count_error, count_warning, count_info

def analyzer_ip():
    with open("sample.log", "r") as f1:
        count_ip = {}
        for stroka1 in f1:
            words = stroka1.split()
            ip = words[-1]
            count_ip[ip] = count_ip.get(ip, 0) + 1
        return count_ip

    
