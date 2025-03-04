import sys
from collections import defaultdict
from typing import Dict, TypedDict

from colorama import Fore
from prettytable import PrettyTable

from decorators import input_error

type Log = Dict[str, int]


class LogEntry(TypedDict):
    date: str
    time: str
    debug_level: str
    reason: str


def load_logs(file_path: str) -> list:
    try:
        splitted = file_path.split(".")

        if not splitted[-1].endswith("txt"):
            raise ValueError("It should be text file")

        with open(file_path) as file:
            lines = file.read().split("\n")
            if lines[len(lines) - 1] == "":
                lines.pop()
            return lines
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    try:
        for log in logs:
            if level.upper() in log:
                print(log)
    except Exception as e:
        print(Fore.RED + f"Error while filtering logs: {e}")
        return []


def count_logs_by_level(logs: list) -> Log:
    try:
        counted_logs = {}
        for line in logs:
            line_data = parse_log_line(line)
            if line_data["debug_level"] not in counted_logs:
                counted_logs[line_data["debug_level"]] = 1
            else:
                counted_logs[line_data["debug_level"]] += 1

        return counted_logs
    except Exception as e:
        print(Fore.RED + f"Error while counting logs: {e}")
        return {}


def display_log_counts(counts: dict):
    try:
        table = PrettyTable()
        table.field_names = ["Logs level", "Quantity"]
        for key, value in counts.items():
            table.add_row([key, value])
        print(table)
    except Exception as e:
        print(Fore.RED + f"Error while displaying logs: {e}")


def parse_log_line(line: str) -> LogEntry:
    try:
        date, time, debug_level, *reason = line.split(" ")
        return {
            "date": date,
            "time": time,
            "debug_level": debug_level,
            "reason": " ".join(reason),
        }
    except ValueError:
        print(Fore.RED + f"Error parsing log line: {line}")
        return {"date": "", "time": "", "debug_level": "", "reason": ""}
    except Exception as e:
        print(Fore.RED + f"Unexpected error while parsing log line: {e}")
        return {"date": "", "time": "", "debug_level": "", "reason": ""}


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2 or len(sys.argv) > 3:
            raise SyntaxError(
                "Command should look like this: 'python logs_parser path/to/file error'"
            )

        _, path, *logs_level = sys.argv

        logs = load_logs(path)
        counted_logs = count_logs_by_level(logs)
        display_log_counts(counted_logs)
        if logs_level:
            print(Fore.CYAN + f"\n-----Logs details for {logs_level} level-------\n")
            filter_logs_by_level(logs, str(logs_level[0]))
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
