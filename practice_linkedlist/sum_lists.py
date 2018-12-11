# You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. 
# Write a function that adds the two numbers and returns the sum as a linked list.

def sum_lists(num1,num2):

    node1, node2= num1, num2
    carry = 0
    result_head, result_node = None, None

    while node1 or node2 or carry:
        value = carry
        if node1:
            value += node1.data
            node1 = node1.next

        if node2:
            value += node2.data
            node2 = node2.next

        if result_node:
            result_node.next = Node(value%10)
            result_node = result_node.next
        else:
            result_node = Node(value%10)
            result_head = result_node
        carry = value/10

    return result_head