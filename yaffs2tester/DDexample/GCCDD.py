# $Id: GCCDD.py,v 1.1 2001/11/05 19:53:33 zeller Exp $
# Using delta debugging on GCC input

import DD
import commands
import string

class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)
        
    def _test(self, deltas):
        # Build input
        input = ""
        for (index, character) in deltas:
            input = input + character

        # Write input to `input.c'
        out = open('input.c', 'w')
        out.write(input)
        out.close()

        print self.coerce(deltas)

        if deltas == []:
            return self.PASS

        # Invoke GCC
        (status, output) = commands.getstatusoutput(
            "rm out.exe; (gcc -o out.exe -g input.c; ./out.exe ) 2>&1")

        print output
        print "Exit code", status

        # Determine outcome
        if status == 0:
            return self.PASS
        elif string.find(output, "Segmentation fault") >= 0:
            return self.FAIL
        elif string.find(output, "assertion") >= 0:
            return self.FAIL
        return self.UNRESOLVED

    def coerce(self, deltas):
        # Pretty-print the configuration
        input = ""
        for (index, character) in deltas:
            input = input + character
        return input


if __name__ == '__main__':
    # Load deltas from `bug.c'
    deltas = []
    index = 1

    for line in open('bug.c'):
        print ("Line = " + line)
        deltas.append((index, line))
        index = index + 1

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
    # (c, c1, c2) = mydd.dd(deltas)	# Invoke DD
    # print "The 1-minimal failure-inducing difference is", c
    # print mydd.coerce(c1), "passes,", mydd.coerce(c2), "fails"




# Local Variables:
# mode: python
# End:
