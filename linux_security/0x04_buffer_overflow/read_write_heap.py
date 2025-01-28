#!/usr/bin/pyhton3
"""Script to find and eplace a string in the heap of
a running process
"""
import sys
import re


def print_usage():
    """Print usage instructions and exit"""
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)


def validate_args(args):
    """validates commande-line arguments."""
    if len(args) != 4:
        print_usage()

    try:
        int(args[1])
    except ValueError:
        print("Error: pid must be an integer.")
        print_usage()


def find_and_replace_in_heap(pid, search_string, replace_string):
    """searchs for and replace a string in the heap
    of a given process
    """
    search_bytes = search_string.encode('ascii')
    replace_bytes = replace_string.encode('ascii')

    if len(replace_bytes) > len(search_bytes):
        print("Error: Replacement string must not be onger than the search string")
        sys.exit(1)

    maps_file = f"/proc/{pid}/maps"

    try:
        with open(maps_file, "r") as maps:
            heap_region = None
            for line in maps:
                if "[heap]" in line:
                    match = re.match(r"([0-9a-f]+)-([0-9a-f]+)", line)
                    if match:
                        start, end = int(match.group(1), 16), int(match.group(2), 16)
                        heap_region = (start, end)
                        break
                    if not heap_region:
                        print("Error: Could not locate the heap region.")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Process with pid {pid} does not exist.")
        sys.exit(1)

    mem_file = f"/proc/{pid}/mem"
    try:
        with open(mem_file, "rb+") as mem:
            start, end = heap_region
            mem.seek(start)
            heap_data = mem.read(end - start)

            # Search for the target string in the heap
            offset = heap_data.find(search_bytes)
            if offset == -1:
                print(f"Error: '{search_string}' not found in the heap.")
                sys.exit(1)

            # Replace the string in the heap
            print(f"Found '{search_string}' at offset {offset}. Replacing with '{replace_string}'...")
            mem.seek(start + offset)
            mem.write(replace_bytes.ljust(len(search_bytes), b'\x00'))
            print("Replacement successful.")
    except PermissionError:
        print("Error: Permission denied. Try running the script as root.")
        sys.exit(1)


if __name__ == "__main__":
    # Validate and parse arguments
    validate_args(sys.argv)

    pid = int(sys.argv[1])
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    # Perform the search and replace operation
    find_and_replace_in_heap(pid, search_string, replace_string)
