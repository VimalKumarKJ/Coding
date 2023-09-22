#to get the top view of the binary tree
from sys import stdin
from queue import Queue

class BinaryTree:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
    def getTopView(root):
        rec = {}
        queue = []
        root_hz_dis = 0
        
        queue.append((root, root_hz_dis))
        
        while queue:
            curr, hz_dis = queue.pop()
            if hz_dis not in rec:
                rec[hz_dis] = curr.val
            if curr.left:
                queue.append((curr.left, hz_dis-1))
            if curr.right:
                queue.append((curr.right, hz_dis+1))
        sorted_keys = sorted(rec.keys())
        return [rec[i] for i in sorted_keys]
    #.....#
