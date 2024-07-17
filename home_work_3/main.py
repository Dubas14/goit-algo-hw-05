import re
from pathlib import Path
import sys

def parse_log_line(line: str) -> dict:
    # Регулярний вираз для парсингу рядка лог-файлу
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)')
    match = log_pattern.match(line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4).strip()
        }
    else:
        return {}

def load_logs(relative_path: str) -> list:
    logs = []
    try:
        file_path = Path.cwd() / relative_path
        
        with file_path.open('r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            log_entry = parse_log_line(line)
            if log_entry:
                logs.append(log_entry)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("Log Counts by Level:")
    for level, count in counts.items():
        print(f"{level}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <log_file_path> [<log_level>]")
        return
    
    log_file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(log_file_path)
    
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

if __name__ == "__main__":
    main()