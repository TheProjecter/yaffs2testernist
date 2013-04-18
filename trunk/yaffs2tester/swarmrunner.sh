#!/bin/bash

for s in {2,3,5,6,8,9}
do 
   
   python yaffs2tester.py --gentestcases --mutantskill --workingfolder 50KSwarm${s}00 --tslength 200 --configfile ./configs/yaffs2swarmconfig50K${s}00.txt --startidx 0 --endidx 4999 --suitesize 5000
   wait
   
   tar cvzf ./50KSwarm${s}00/testcases.tar.gz ./50KSwarm${s}00/testcases
   wait
   rm -rf ./50KSwarm${s}00/testcases/
   
   wait
done

echo "done all runs" | mail -s "done" zhangch@onid.orst.edu
