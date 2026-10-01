from analyzer import analyze
from analyzer import analyzer_ip

count_error, count_warning, count_info = analyze()
    
print(f"Логов с ошибкой 'ERROR': {count_error}")
print(f"Логов с ошибкой 'WARNING': {count_warning}")
print(f"Логов с параметром 'INFO': {count_info}")

ip_counts = analyzer_ip()
for ip, counts in ip_counts.items():
    print(f"{ip}: {counts}")
