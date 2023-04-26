# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root:
            return f"({root.val}{self.serialize(root.left)}{self.serialize(root.right)})"
        else:
            return "*"

    def deserialize(self, data: str) -> TreeNode:
        if data == '*':
            return None
        data = data[1:-1]
        i = -1
        for j in range(0, len(data)):
            if data[j] == "(" or data[j] == "*":
                i = j
                break
        result = TreeNode(int(data[:i]))
        data = data[i:]
        k = 0
        for i in range(0, len(data)):
            if data[i] == '(':
                k+=1
            if data[i] == ')':
                k-=1
            if k==0:
                break
        if data[0] == "*":
            i+=1
        result.left = self.deserialize(data[:i+1])
        result.right = self.deserialize(data[i+2:])
        return result

test = TreeNode(1)
test.left = TreeNode(2)
r = TreeNode(3)
test.right = r
r.left = TreeNode(4)
r.right = TreeNode(5)

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
data = ser.serialize(test)
print(data)
ans = deser.deserialize(data)