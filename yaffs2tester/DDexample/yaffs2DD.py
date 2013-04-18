# Using delta debugging on yaffs2 input

import DD
import commands
import string
import subprocess
import myutils
import os

testcaseinput='xyz12/testcases/000200/ts000000.c'
newinput='input.c'
cmdline='yaffs2_gcov -start 0 -num 1 -testcasefile %s'%(testcaseinput)
origcov=''
#--------------------------------------------------------
def getLineCoverage(filename):
    s=''
    f = open(filename)
    lines = f.readlines()
    f.close()
    for line in lines:
        parts=line.split(':')
        p0 = parts[0]
        p0=p0.strip()
        if p0 != '-' and p0 != '#####':
            s += parts[1].strip()
            s += ','
   return s
#--------------------------------------------------------
class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)
        
    def _test(self, deltas):
        # Build input
        input = ""
        for (index, character) in deltas:
            input = input + character

        # Write input to `input.c'
        out = open(newinput, 'w')
        out.write(input)
        out.close()

        print self.coerce(deltas)

        if deltas == []:
            return self.PASS

        # Invoke yaffs2
        cmd='rm yaffs2.gcov yaffs2.gcda'
          myutils.exec_cmd(cmd)
        cmd='yaffs2_gcov -start 0 -num 1 -testcasefile %s'%(input)
        myutils.exec_cmd(cmd)
        if os.path.exists('yaffs2.gcda'):
            myutils.exec_cmd('gcov yaffs2.c')
            if os.path.exists('yaffs2.c.gov'):
                newcov=getLineCoverage('yaffs2.c.gcov')
                if newcov == origcov:
                    return self.FAIL
                else:
                    return self.PASS
            else:
                return self.UNRESOLVED
        else:
            self.UNRESOLVED

    def coerce(self, deltas):
        # Pretty-print the configuration
        input = ""
        for (index, character) in deltas:
            input = input + character
        return input

#--------------------------------------------------------
if __name__ == '__main__':
    # Load deltas from `bug.c'
    deltas = []
    index = 1

    for line in open(testcaseinput):
        print ("Line = " + line)
        deltas.append((index, line))
        index = index + 1

    cmd='rm yaffs2.gcov yaffs2.gcda'
    myutils.exec_cmd(cmd)
    myutils.exec_cmd(cmdline)
    myutils.exec_cmd('gcov yaffs2.c')
    origcov=getLineCoverage('yaffs2.c.gcov')
    mydd = MyDD()
    
    print "Simplifying failure-inducing input..."
    c = mydd.ddmin(deltas)              # Invoke DDMIN
    print "The 1-minimal failure-inducing input is", mydd.coerce(c)
    print "Removing any element will make the failure go away."

    # Write input to `input.c'
    out = open('minimal.c', 'w')
    out.write(mydd.coerce(c))
    out.close()

    # print
    
    # print "Isolating the failure-inducing difference..."
    # (c, c1, c2) = mydd.dd(deltas)    # Invoke DD
    # print "The 1-minimal failure-inducing difference is", c
    # print mydd.coerce(c1), "passes,", mydd.coerce(c2), "fails"




# Local Variables:
# mode: python
# End:
