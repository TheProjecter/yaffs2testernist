**0. Make sure you have gmp library installed:**

http://gmplib.org/


Switch to yaffs2tester directory:

**1. To generate some yaffs2 test cases:**

python yaffs2tester.py --gentestcases --startidx ${startidx} --endidx {$endidx} --tslength  ${tslength} --workingfolder ${workingfolder}

--startidx: the start index of the test cases to be generated.

--endidx: the end index of the test cases to be generated

--tslength: test case length, a.k.a. the number of API calls.

--workingfolder: the place of the generated test cases.

For example:

<font color='Blue'>python yaffs2tester.py --gentestcases --startidx 0 --endidx 9 --tslength 200 --workingfolder ts200</font>

All the generated test cases will be under ts200/testcases/000200

**2. To minimize a test case in terms of it's function or line coverage:**

python yaffs2DD.py ${inputtestcasefile} ${-f|-l} ${outputtestcasefile}

Arguments:

${inputtestcasefile}: the test case to be minimized.

${-f|-l}: minimize test case in terms of function or line coverage.

${outputtestcasefile}: minimal resulting test case file name.

For example, we could minimize a test case created in step1 with the command below using function coverage:

<font color='Blue'>python yaffs2DD.py ts200/testcases/000200/ts000000.c -f ts0.c</font>

**3. To check a mutants killing for a set of test cases on a specified mutant:**

python checkmutants.py --testcasesdir ${testcasesdir} --mutantid ${muid} --mukillfile ${mukillfilename}

--testcasesdir: test cases directory, all test cases will be checked on the specified mutant. NOTE: the test case file names under the specified folder must have the format:
tsXXXXX.c

--mutantid: id of the specified mutant, this has to be the line number of file mutgen/yaffs2.c.MutantDescs.txt

--mukillfile: mutant killing results - one line file. "0" means a test case didn't kill this mutant while "1" means it did.

For example, we could check mutants killing for the test cases generated in step1 with this command.

<font color='Blue'>python checkmutants.py --testcasesdir ts200/testcases/000200/ --mutantid 3000 --mukillfile abc</font>