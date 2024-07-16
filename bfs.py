# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return root
        if root.left is None and root.right is None: return [[root.val]]

        #here if u use queue, whats happeninf is we can't use pop 
        #theres an inbuilt popleft for deque tho

        #queue stores the nodes 
        
        queue= deque([root])
        result=[]
        while queue:
            #instead of len(queue)>0, just put queue
            size= len(queue)
            level_list=[]

            for i in range(0, size):
                popped= queue.popleft()
                level_list.append(popped.val)

                if popped.left: 
                    #no need to use is not none
                    queue.append(popped.left)

                if popped.right:
                    queue.append(popped.right)

            result.append(level_list)   
        return result