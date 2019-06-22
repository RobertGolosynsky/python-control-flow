#!/usr/bin/env python
import sys
import os.path as osp
from control_flow.main import doit
from glob import glob

def testing():
    assert False, "This should have been replaced via read-in python script with a function called testing"

if len(sys.argv) == 1:
    mydir = osp.dirname(osp.abspath(__file__))
    glob_path = mydir + '/../examples/*.py'
    files = glob(glob_path)
else:
    files = sys.argv[1:]
    pass

total = count = 0
for filename in files:

    # FIXME: redo with import module
    source = open(filename).read();
    exec(source)
    print("\n", '=' * 20, "\n")

    short = osp.basename(filename)[0:-3]

    cs = doit(testing, short)  # NOQA
    got = cs.strip()
    want = expect().strip()  # NOQA
    if got != want:
        print("\n** filename %s fails **\n" % filename)
        print(want)
        print("\n", '-' * 20, "\n")
        print(got)
        pass
        sys.exit(1)
    else:
        count += 1
        pass
    total += 1
    pass


print("%d tests, %d passed." % (total, count))
assert count == total
