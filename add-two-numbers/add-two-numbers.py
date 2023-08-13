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
    def showln(self):
        cnt = self
        while cnt != None:
            print cnt.val,
            cnt = cnt.next
        print
    def show(self):
        cnt = self
        while cnt != None:
            print cnt.val,
            cnt = cnt.next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        overflow = 0
        l1_finished = False
        l2_finished = False
        first_write = True
        while not l1_finished or not l2_finished or overflow > 0:
            digit2write = overflow
            if not l1_finished:
                digit2write = digit2write + l1.val
            if not l2_finished:
                digit2write = digit2write + l2.val
            if digit2write <= 9:
                if first_write:
                    sum = Node(digit2write)
                    first_write = False
                else:
                    sum.append(digit2write)
                overflow = 0
            else:
                digit2write = digit2write - 10
                overflow = 1
                if first_write:
                    sum = Node(digit2write)
                    first_write = False
                else:
                    sum.append(digit2write)
            if l1.next == None:
                l1_finished = True
            else:
                l1 = l1.next
            if l2.next == None:
                l2_finished = True
            else:
                l2 = l2.next
        return sum
print('Example 1')
print '  Input:  ',
l1 = Node(2)
l1.append(4)
l1.append(3)
print "l1 =",
l1.show()
l2 = Node(5)
l2.append(6)
l2.append(4)
print ", l2 =",
l2.showln()
print '  Output: ',
a = Solution().addTwoNumbers(l1, l2)
a.showln()
print('Example 2')
print '  Input:  ',
l1 = Node(0)
print "l1 =",
l1.show()
l2 = Node(0)
print ", l2 =",
l2.showln()
print '  Output: ',
b = Solution().addTwoNumbers(l1, l2)
b.showln()
print('Example 3')
print '  Input:  ',
l1 = Node(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
l1.append(9)
print "l1 =",
l1.show()
l2 = Node(9)
l2.append(9)
l2.append(9)
l2.append(9)
print ", l2 =",
l2.showln()
print '  Output: ',
c = Solution().addTwoNumbers(l1, l2)
c.showln()