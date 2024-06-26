#!/usr/bin/python3
import unittest
from typing import Optional, List


null = None

# Leet Code Solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Solution Note

"""

# Leet Code Solution

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        def traversal(root, lst):
            if root is None:
                return None

            lst.append(root.val)
            print(lst)

            if sum(lst) == targetSum:
                if root.left is None and root.right is None:
                    results.append([lst[i] for i in range(len(lst))])
                    # results.append(lst)
                    # lst.pop()
                    return None

            left_list = [ lst[i] for i in range(len(lst)) ]
            # right_list = [ lst[i] for i in range(len(lst)) ]
            traversal(root.left, left_list)
            # traversal(root.right, right_list)

            # traversal(root.left, lst)
            traversal(root.right, lst)



        traversal(root, [])
        return results






def make_node(treelist: List[any]) -> Optional[TreeNode]:
    if len(treelist) == 0:
        return None

    # 깊은복사
    lst = []
    for val in treelist:
        lst.append(val)

    tree = TreeNode(lst.pop(0))
    stack = [ tree ]

    while len(lst) > 0:
        node = stack.pop(0)

        # left node
        value = lst.pop(0)
        if value is None:
            node.left = None
        else:
            node.left = TreeNode(value)
            stack.append(node.left)

        if len(lst) == 0:
            break

        #right node
        value = lst.pop(0)
        if value is None:
            node.right = None
        else:
            node.right = TreeNode(value)
            stack.append(node.right)

    return tree


def make_list(root: TreeNode) -> List[any]:
    if root is None:
        return []

    result: List[any] = [ root.val ]
    queue: List[TreeNode] = [ ]

    if root.left is None and root.right is None:
        return result

    queue.append(root.left)
    queue.append(root.right)

    while len(queue) > 0:
        node: TreeNode = queue.pop(0)
        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        if node.left is None and node.right is None:
            continue

        queue.append(node.left)
        queue.append(node.right)

    return result


# python unit test
class UnitTest(unittest.TestCase):

    # 클래스 생성 시 1회 실행
    @classmethod
    def setUpClass(self):
        pass

    # 클래스 소멸 시 1회 실행
    @classmethod
    def tearDownClass(self):
        pass

    # 테스트 케이스 전 실행
    def setUp(self):
        self.solution = Solution()

    # 테스트 케이스 후 실행
    def tearDown(self):
        pass

    def test_make_list(self):
        lst = [1,None,1,None,1]
        # list to TreeNode
        root = make_node(lst)
        # TreeNode to list
        answer = make_list(root)

        # print(lst)
        # print(answer)

        # self.solution.problem(root)
        self.assertEqual(answer, lst)

    def test_case_1(self):
        lst = [5,4,8,11,null,13,4,7,2,null,null,5,1]
        targetSum = 22
        root = make_node(lst)
        answer = [[5,4,11,2],[5,8,4,5]]
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)

    def test_case_2(self):
        lst = [1,2,3]
        targetSum = 5
        root = make_node(lst)
        answer = []
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)

    def test_case_3(self):
        lst = [1,2]
        targetSum = 0
        root = make_node(lst)
        answer = []
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)


    def test_case_4(self):
        lst = [-2, null, -3]
        targetSum = -2
        root = make_node(lst)
        answer = []
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)

    def test_case_5(self):
        lst = [1]
        targetSum = 1
        root = make_node(lst)
        answer = [[1]]
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)

    def test_case_6(self):
        lst = [-2, null, -3]
        targetSum = -3
        root = make_node(lst)
        answer = []
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)

    def test_case_7(self):
        lst = [1,-2,-3,1,3,-2,null,-1]
        targetSum = -1
        root = make_node(lst)
        answer =[[1,-2,1,-1]]
        result = self.solution.pathSum(root, targetSum)
        self.assertEqual(result, answer)







if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
