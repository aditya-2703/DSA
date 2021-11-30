# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.



class ListNode:
    def __init__(self,val=0,next=None):
        self.val =val
        self.next = next
def get_list():
    head = ListNode(1)
    temp =head
    for i in range(2,7):
        nn = ListNode(i)
        temp.next = nn 
        print(f"node {temp} data {temp.val}")
        temp = temp.next
    return head
def middleNode(head):
    if not head or not head.next:
        return head
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == '__main__':
    head = get_list()
    middleNode(head)    
