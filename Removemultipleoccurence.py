import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
            
    return head

def main():
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            return

        data_list = list(map(int, sys.stdin.readline().split()))
        
        # Create the linked list
        head = Node(data_list[0])
        current = head
        for i in range(1, n):
            current.next = Node(data_list[i])
            current = current.next

        # Remove duplicates
        new_head = remove_duplicates(head)
        
        # Print the result
        result = []
        current = new_head
        while current:
            result.append(str(current.data))
            current = current.next
        
        print(" ".join(result))

    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    main()