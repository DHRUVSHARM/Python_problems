# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def postorder(node):
            # "element""left subtree""right subtree" -> str representation
            if not node:
                return "N"
            
            result = str(node.val) + ","
            result += postorder(node.left) + ","
            result += postorder(node.right)

            return result

        serialized_tree = postorder(root)
        return serialized_tree
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # we need to recreate the tree 
        # 1 2nn 34nn5nn

        if data == "N":
            return None

        # make it a list to deserialize
        data_list = data.split(",")
        # print(data_list)
        
        curr = 0
        def helper():
            nonlocal curr 

            if data_list[curr] == "N":
                curr += 1
                return None

            value = data_list[curr]
            if value.startswith("-"):
                value = -int(data_list[curr][1:])
            else:
                print(data_list[curr][1:])
                value = int(data_list[curr])

            new_node = TreeNode(value)
            curr += 1
            new_node.left = helper()
            new_node.right = helper()

            return new_node

        deserialized_tree = helper()
        return deserialized_tree

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))