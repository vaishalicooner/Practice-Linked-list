# reverse a linked list

def reverse_ll(head):
    if head is None or head.next is None:
        return head

        prev = None
        curr = head
        post = head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = post
            if post is not None:
                post = post.next

        return prev
        