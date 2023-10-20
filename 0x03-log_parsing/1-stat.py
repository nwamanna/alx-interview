#!/usr/bin/env python3
""" a script that reads stdin line by line and computes metrics """
import sys
import re


def main():
    """ a script that reads stdin line by line and computes metrics """
    line_count = 0
    status_codes = {}
    total_file_size = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            #use regex to check valid line
            match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
            if match:
                ip_address, date, status_code, file_size = match.groups()
                status_code = int(status_code)
                file_size = int(file_size)
                total_file_size += file_size

                #updates the status code count
                status_code[status_code] = status_codes.get(status_code, 0) + 1
                line_count += 1

                if line_count % 10 == 0:
                     print_statistics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)

def print_statistics(total_file_size, status_codes):
    print(f'Total file size: {total_file_size} bytes')
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        print(f'{status_code}: {count}')
                
