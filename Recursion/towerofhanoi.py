def towerofhanoi(noOfDisks, startPeg=1, endPeg=3):
    if noOfDisks:
        towerofhanoi(noOfDisks-1, startPeg, 6-startPeg-endPeg)
        print('Move Disks %d from peg %d to peg %d'%(noOfDisks, startPeg, endPeg))
        towerofhanoi(noOfDisks-1, 6-startPeg-endPeg, endPeg)

towerofhanoi(noOfDisks=5)
