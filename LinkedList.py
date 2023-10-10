# Structure of Linked List 

class Node:
    def __inti__(self, data):
        self.data = data
        self.next = None 
    
    
def rotate_right(head, k):
    #  base case
    if not head or k == 0:
        return head
    
    # two pointers - we can use to find the new head and tail of the linked list
    
    old_tail = head
    length = 1
    
    while old_tail.next:
        length += 1
        old_tail = old_tail.next 
        
    k = k % length # no of rotations
    
    # condition for k values 
    if k == 0:
        return head
    
    new_tail = head
    for i in range(length - k - 1):
        new_tail = new_tail.next 
    
    new_tail = new_tail.next
    new_tail.next = None
    
    old_tail.next = head 
    
    return new_head

   