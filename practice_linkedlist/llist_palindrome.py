# Implement a function to check if a linked list is a palindrome.

def is_palindrome(self):
    head = self
    prev = None
    while self.next:

        self.prev = prev
        prev = self
        self= self.next

    tail = self
    tail.prev = prev
    while head is not tail and head.data == tail.data:
        head = head.next
        tail = tail.prev

    if head is tail:
        return True

    elif head.data == tail.data:
        return True
    else:
        return False