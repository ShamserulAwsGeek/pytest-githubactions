from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1



# import sys
# import os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# from src.math_operations import add, sub

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
    
# def test_sub():
#     assert sub(5, 3) == 2
#     assert sub(4, 3) == 1
#     assert sub(3, 3) == 0
#     assert sub(2, 3) == -1