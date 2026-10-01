from analyzer import analyze

count_error, count_warning, count_info = analyze()
    
print(f"Логов с ошибкой 'ERROR': {count_error}")
print(f"Логов с ошибкой 'WARNING': {count_warning}")
print(f"Логов с параметром 'INFO': {count_info}")
