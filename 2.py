import sys

def solve():
    """
    Main function to solve the problem by reading input,
    processing the items, and printing the result.
    """
    try:
        # Read the number of items
        N_str = sys.stdin.readline()
        if not N_str:
            return
        N = int(N_str.strip())

        items = []
        for _ in range(N):
            # Read each item line and split it into a list of strings
            item_line = sys.stdin.readline().strip()
            if item_line:
                items.append(item_line.split())

        # Read the ruleKey and ruleValue
        ruleKey = sys.stdin.readline().strip()
        ruleValue = sys.stdin.readline().strip()

        # Map ruleKey to the corresponding index
        key_map = {"type": 0, "color": 1, "name": 2}
        
        # Check if the ruleKey is valid
        if ruleKey not in key_map:
            print(0)
            return 

        rule_index = key_map[ruleKey]
        count = 0

        # Iterate through items and count matches
        for item in items:
            if len(item) > rule_index and item[rule_index] == ruleValue:
                count += 1
        
        print(count)

    except (IOError, ValueError):
        # Gracefully handle potential errors with input
        pass

if __name__ == "__main__":
    solve()