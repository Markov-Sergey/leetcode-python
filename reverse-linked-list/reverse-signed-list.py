class Node(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def append(self, val = 0):
        tmp = Node(val)
        cnt = self
        while cnt.next != None:
            cnt = cnt.next
        cnt.next = tmp
    def show(self):
        cnt = self
        while cnt != None:
            print cnt.val,
            cnt = cnt.next
        print
class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        prev = None
        curr = head
        next = curr.next
        while next != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
print('Example 1')
print '  Input:  ',
a = Node(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.show()
print '  Output: ',
b = Solution().reverseList(a)
b.show()
print('Example 2')
print '  Input:  ',
c = Node(1)
c.append(2)
c.show()
print '  Output: ',
d = Solution().reverseList(c)
d.show()
print('Example 3')
e = None
print '  Input:  ', e
f = Solution().reverseList(e)
print '  Output: ', f