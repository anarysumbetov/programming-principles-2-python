import sys

def process_doramas():
    # Read the number of days (n) from standard input
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1)
    except ValueError:
        return

    dorama_data = {}

    # Read n lines of dorama name and episode count
    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            continue
        try:
            # Splitting by the last space in case the name contains spaces
            # Although the example suggests single word names, this is safer.
            parts = line.strip().rsplit(' ', 1)
            if len(parts) == 2:
                s = parts[0]
                k = int(parts[1])
                # Sum the episodes for each unique dorama name
                if s in dorama_data:
                    dorama_data[s] += k
                else:
                    dorama_data[s] = k
        except ValueError:
            continue

    # Sort the results alphabetically by dorama name
    sorted_doramas = sorted(dorama_data.items())

    # Print the output in the specified format
    for name, episodes in sorted_doramas:
        print(f"{name} {episodes}")

if __name__ == "__main__":
    process_doramas()
