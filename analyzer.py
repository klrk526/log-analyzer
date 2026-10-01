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