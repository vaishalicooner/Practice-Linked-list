# Implement an algorithm to find the kth to last element of a singly linked list.

def k_to_last(self,k):

    lead,follow = self,self

    for x in range[k:]:
        if not lead:
            return None
        lead = lead.next

        while lead:
            lead,follow = lead.next,follow.next
        return follow