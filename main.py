from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if root:
            return str(root.val)+" "+self.serialize(root.left)+" "+self.serialize(root.right)
        else:
            return "*"

    def deserialize(self, data):
        queue = deque(data.split())
        return self.deserialize_imp(queue)

    def deserialize_imp(self, queue):
        val = queue.popleft()
        if val == "*":
            return None
        node = TreeNode(int(val))
        node.left = self.deserialize_imp(queue)
        node.right = self.deserialize_imp(queue)
        return node