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
        arr = data.split()
        return self.deserialize_imp(arr)

    def deserialize_imp(self, arr):
        val = arr.pop(0)
        if val == "*":
            return None
        node = TreeNode(int(val))
        node.left = self.deserialize_imp(arr)
        node.right = self.deserialize_imp(arr)
        return node


class Solution:
    def rightSideView(self, root, height=0, res=None):
        if res is None:
            res = []
        if root:
            if len(res) == height:
                res.append(root.val)
            height += 1
            self.rightSideView(root.right, height, res)
            self.rightSideView(root.left, height, res)
        return res


class Solution1:
    def isValidBST(self, root, min_val = float('-inf'), max_val = float('inf')):
        if root is None:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBST(root.left, min_val, root.val) and self.isValidBST(root.right, root.val, max_val)

class Solution2:
    def trimBST(self, root, low, high):
        if root is None:
            return
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif high < root.val:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
