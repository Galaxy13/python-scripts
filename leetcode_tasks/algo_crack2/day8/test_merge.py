from merge_2_binr_trees_617 import *

def test_mergeTrees():
    tree1 = list_to_Treenode([1,3,2,5])
    tree2 = list_to_Treenode([2,1,3,None,4,None,7])
    assert Solution().mergeTrees(tree1, tree2) == list_to_Treenode([3,4,5,5,4,None,7])