import os
import json
import re
import datetime
from itertools import product
from log_query import search_logs
from advanced_log_query import search_logs_by_date_range, search_logs_by_regex, search_logs_by_multiple_filters

def main():
    while True:
        print("\n===== Log Query Interface =====")
        print("1. Normal Search")
        print("2. Advanced Search")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            # Normal Search
            filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source): ")
            filter_value = input(f"Enter the value for {filter_key}: ")
            logs = search_logs(filter_key, filter_value)
            print("\nSearch Results:")
            for log in logs:
                print(log)

        elif choice == "2":
            # Advanced Search
            print("\n===== Advanced Search =====")
            print("1. Search by Date Range")
            print("2. Search by Regular Expression")
            print("3. Search by Multiple Filters")
            print("4. Back to Main Menu")
            advanced_choice = input("Enter your choice (1-4): ")

            if advanced_choice == "1":
                # Search by Date Range
                start_date_str = input("Enter the start date (YYYY-MM-DD): ")
                end_date_str = input("Enter the end date (YYYY-MM-DD): ")
                start_date = datetime.datetime.fromisoformat(start_date_str)
                end_date = datetime.datetime.fromisoformat(end_date_str)
                logs = search_logs_by_date_range(start_date, end_date)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "2":
                # Search by Regular Expression
                regex_pattern = input("Enter the regular expression pattern: ")
                logs = search_logs_by_regex(regex_pattern)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "3":
                # Search by Multiple Filters
                filters = {}
                while True:
                    filter_key = input("Enter the key to filter logs (level, log_string, timestamp, metadata.source), or 'q' to quit: ")
                    if filter_key.lower() == 'q':
                        break
                    filter_value = input(f"Enter the value for {filter_key}: ")
                    filters[filter_key] = filter_value
                logs = search_logs_by_multiple_filters(filters)
                print("\nSearch Results:")
                for log in logs:
                    print(log)

            elif advanced_choice == "4":
                # Back to Main Menu
                continue

        elif choice == "3":
            # Exit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()