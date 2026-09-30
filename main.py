with open("sample.log", "r") as f:
    count = 0
    count2 = 0
    count3 = 1
    for stroka in f:
        if "ERROR" in stroka:
            count += 1
        elif "WARNING" in stroka:
            count2 += 1
        elif "INFO" in stroka:
            count3 += 1
print(f"Логов с ошибкой 'ERROR': {count}")
print(f"Логов с ошибкой 'WARNING': {count2}")
print(f"Логов с параметром 'INFO': {count3}")
