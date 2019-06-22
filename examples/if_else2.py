# Note: driver assumes functions named "testing" and "expect".
def testing(a):
    if a:
        a = 15
    else:
        a = 16
    return a
def expect():
    return """
test BasicBlock(#0 range: (0, 2), flags=[0, 14], follow_offset=4, edge_count=2, jumps=[10])
  fallthrough BasicBlock(#1 range: (4, 8), flags=[8], follow_offset=10, edge_count=2, jumps=[14])
    sequence BasicBlock(#1 range: (4, 8), flags=[8], follow_offset=10, edge_count=2, jumps=[14])
  end fallthrough
  alternate BasicBlock(#2 range: (10, 12), follow_offset=14, edge_count=1)
    sequence BasicBlock(#2 range: (10, 12), follow_offset=14, edge_count=1)
  end alternate
end test
sequence BasicBlock(#3 range: (14, 16), flags=[1], follow_offset=None, edge_count=0)
"""
