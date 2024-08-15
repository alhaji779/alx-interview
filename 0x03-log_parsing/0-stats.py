#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                continue

            try:
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                continue

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

