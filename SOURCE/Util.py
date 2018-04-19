import sys
import subprocess
import time
import os

def isEqualStr(a, b):
    return a.lower() == b.lower()

def executeCommand(cmd,outputFname):

    print "Executing %s...   " % (cmd),
    sys.stdout.flush()
    dumpFile = open(outputFname, "w")

    p = subprocess.Popen([cmd], shell=True, stdout=dumpFile, stderr=dumpFile)

    startTime = time.time()

    while p.poll() == None:
        # time.sleep(pollTime)
        if time.time() - startTime > 350:
            ans = raw_input("Still running. Continue (c), Restart (r), Quit(q)? ")
            ans = "q"
            print "Killing process"
            startTime = time.time()
            if ans.strip() == "q":
                os.kill(p.pid + 1, 9)
                sys.exit(-1)
            elif ans.strip() == "c":
                continue
            elif ans.strip() == "r":
                os.kill(p.pid + 1, 9)
            else:
                print "Unrecognized response. Continuing."

    dumpFile.close()
    # time.sleep(5)
    endTime = time.time()

    with open(outputFname, "r") as fh:
        data = fh.readlines()
    return data
