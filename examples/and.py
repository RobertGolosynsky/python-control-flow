# Note: driver assumes functions named "testing" and "expect".
def testing(a, b):
    if a \
       and b:
        c = 1
    return c
def expect():
    ## FIXME: the current code puts the trailing sequence in the wrong place.
    return """
test BasicBlock(#0 range: (0, 2), flags=[0, 14], follow_offset=4, edge_count=2, jumps=[12])
  fallthrough BasicBlock(#1 range: (4, 6), flags=[14], follow_offset=8, edge_count=2, jumps=[12])
    test BasicBlock(#1 range: (4, 6), flags=[14], follow_offset=8, edge_count=2, jumps=[12])
      fallthrough BasicBlock(#2 range: (8, 10), follow_offset=12, edge_count=1)
        sequence BasicBlock(#2 range: (8, 10), follow_offset=12, edge_count=1)
      end fallthrough
    end test
  end fallthrough
end test
sequence BasicBlock(#3 range: (12, 14), flags=[1], follow_offset=None, edge_count=0)
"""
