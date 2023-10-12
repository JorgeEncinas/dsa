# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    head_node = None
    last_node = head_node

    def append(self, node):
        if(self.head_node is None): #first element!
            self.head_node = node
            self.last_node = self.head_node
        else: #Go to last one
            self.last_node.next = node
            self.last_node = node

    def append_lone_digits(self, node, carryover):
        while node is not None:    
            add = node.val + carryover
            unit = add % 10 # Gives us the "surplus", which is what is kept here.
            carryover = 1 if add > 9 else 0
            l3 = ListNode(val=unit, next=None)
            self.append(l3)
            node = node.next
        if carryover == 1:
            self.append(ListNode(val=carryover, next=None))

    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #One might be bigger than the other
        nodes_are_not_null = True
        carryover = 0
        head_node = None
        last_node = None
        while nodes_are_not_null:
            add = l1.val + l2.val + carryover
            unit = add % 10 # Gives us the "surplus", which is what is kept here.
            carryover = 1 if add > 9 else 0
            l3 = ListNode(val=unit, next=None)
            self.append(l3)
            l1 = l1.next
            l2 = l2.next
            if l1 is None or l2 is None:
                nodes_are_not_null = False
        #Arriving here, check if one of these had less digits than the other.
        if l1 is None and l2 is not None:
            self.append_lone_digits(l2, carryover)
        elif l2 is None and l1 is not None:
            self.append_lone_digits(l1, carryover)
        elif carryover == 1:
            self.append(ListNode(val=carryover, next=None))

        return self.head_node
