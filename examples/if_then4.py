# Note: driver assumes functions named "testing" and "expect".
def testing(a):
    if a:
        return 5
    return 6

def expect():
    return """
test BasicBlock(#0 range: (0, 2), flags=[0, 14], follow_offset=4, edge_count=2, jumps=[8])
  fallthrough BasicBlock(#1 range: (4, 6), flags=[1], follow_offset=8, edge_count=0)
    sequence BasicBlock(#1 range: (4, 6), flags=[1], follow_offset=8, edge_count=0)
  end fallthrough
end test
sequence BasicBlock(#2 range: (8, 10), flags=[1], follow_offset=None, edge_count=0)
"""
