class FCFS:
    def __init__(self):
        self.numProcesses = int(input("Enter number of processes: "))
        self.processes = [int(i) for i in input("Enter processes: ").split(",")]
        self.arrivalTimes = [int(i) for i in input("Enter arrival times: ").split(",")]
        self.burstTimes = [int(i) for i in input("Enter burst times: ").split(",")]
        self.waitingTimes = [0] * self.numProcesses
        self.turnAroundTimes = [0] * self.numProcesses
        self.completionTimes = [0] * self.numProcesses
        self.completed = [False] * self.numProcesses

    def printTable(self):
        print("Processes\tArrival Times\tBurst Times\tWaiting Time\tTurn Around Time  Completion Time\n")
        for i in range(self.numProcesses):
            print(self.processes[i],self.arrivalTimes[i],self.burstTimes[i],self.waitingTimes[i],self.turnAroundTimes[i],self.completionTimes[i],sep="\t\t")
    
    def calcWaitTime(self):
        for i in range(self.numProcesses):
            for j in range(i):
                self.waitingTimes[i] += self.burstTimes[j]
            self.waitingTimes[i] = self.waitingTimes[i] - self.arrivalTimes[i]
            if self.waitingTimes[i] < 0:
                self.waitingTimes[i] = 0
        return None
    
    def calcTurnAroundTime(self):
        for i in range(self.numProcesses):
            self.turnAroundTimes[i] = self.burstTimes[i] + self.waitingTimes[i]
        return None
    
    def calcCompletionTime(self):
        for i in range(self.numProcesses):
            self.completionTimes[i] = self.turnAroundTimes[i] + self.arrivalTimes[i]
        return None

    def calcAvgWaitingTime(self):
        avgWaitingTime = 0
        for i in range(self.numProcesses):
            avgWaitingTime += self.waitingTimes[i]
        avgWaitingTime = avgWaitingTime / self.numProcesses
        print("Average waiting Time is: ",avgWaitingTime)
        return None 
    
    def calcAvgTurnAroundTime(self):
        avgTurnAroundTime = 0
        for i in range(self.numProcesses):
            avgTurnAroundTime += self.turnAroundTimes[i]
        avgTurnAroundTime = avgTurnAroundTime / self.numProcesses
        print("Average Turn Around Time is: ",avgTurnAroundTime)
        return None
    
    def printGanttChart(self):
        minTime = 999
        jobID = -1
        completedProcess = 0
        print("\nGantt Chart:")
        print("0 | ",end="")
        while True:
            for i in range(self.numProcesses):
                if (self.waitingTimes[i] < minTime) and (self.completed[i] == False):
                    minTime = self.waitingTimes[i]
                    jobID = i
            print("P" + str(jobID + 1) + " | " + str(self.completionTimes[jobID]),end=" | ")
            completedProcess += 1
            self.completed[jobID] = True
            minTime = 999
            if completedProcess == self.numProcesses:
                print("\n")
                break


    
    def calculateAll(self):
        self.calcWaitTime()
        self.calcTurnAroundTime()
        self.calcCompletionTime()
        self.printGanttChart()
        self.printTable()
        self.calcAvgWaitingTime()
        self.calcAvgTurnAroundTime()
        
        
                

class STRF:
    def __init__(self):
        self.numProcesses = int(input("Enter number of processes: "))
        self.processes = [int(i) for i in input("Enter processes: ").split(",")]
        self.arrivalTimes = [int(i) for i in input("Enter arrival times: ").split(",")]
        self.burstTimes = [int(i) for i in input("Enter burst times: ").split(",")]
        self.waitingTimes = [0] * self.numProcesses
        self.turnAroundTimes = [0] * self.numProcesses
        self.completionTimes = [0] * self.numProcesses
    

    def execute(self):
        remainingTime = []
        totalTime = 0
        for i in range(self.numProcesses):
            remainingTime.append(self.burstTimes[i])
            totalTime += self.burstTimes[i]
        prevJob = -1
        jobID = -1
        minTime = 99
        for time in range(totalTime + 1):
            for i in range(self.numProcesses):
                if (self.arrivalTimes[i] <= time) and (remainingTime[i] > 0) and (remainingTime[i] < minTime):
                    jobID = i
                    minTime = remainingTime[i]
            
            remainingTime[jobID] -= 1
            minTime = remainingTime[jobID]
            if minTime == 0:
                minTime = 99
            
            if remainingTime[jobID] == 0:
                finishTime = time + 1
                self.waitingTimes[jobID] = finishTime - self.arrivalTimes[jobID] - self.burstTimes[jobID]
                self.completionTimes[jobID] = finishTime

                if self.waitingTimes[jobID] < 0:
                    self.waitingTimes[jobID] = 0
            
            if (time == 0):
                print("Gantt Chart:")
                print("0 | P" + str(jobID + 1),end= " | ")
            elif (time == totalTime):
                print(str(totalTime))
            elif jobID != prevJob:
                print(str(time) + " | " + "P" + str(jobID + 1),end=" | ")
            prevJob = jobID
        return None

    
    def calcTurnAroundTime(self):
        for i in range(self.numProcesses):
            self.turnAroundTimes[i] = self.burstTimes[i] + self.waitingTimes[i]
        return None

    def calcAvgWaitingTime(self):
        avgWaitingTime = 0
        for i in range(self.numProcesses):
            avgWaitingTime += self.waitingTimes[i]
        avgWaitingTime = avgWaitingTime / self.numProcesses
        print("Average waiting Time is: ",avgWaitingTime)
        return None 
    
    def calcAvgTurnAroundTime(self):
        avgTurnAroundTime = 0
        for i in range(self.numProcesses):
            avgTurnAroundTime += self.turnAroundTimes[i]
        avgTurnAroundTime = avgTurnAroundTime / self.numProcesses
        print("Average Turn Around Time is: ",avgTurnAroundTime)
        return None

    def printTable(self):
        print("Processes\tArrival Times\tBurst Times\tWaiting Time\tTurn Around Time  Completion Time\n")
        for i in range(self.numProcesses):
            print(self.processes[i],self.arrivalTimes[i],self.burstTimes[i],self.waitingTimes[i],self.turnAroundTimes[i],self.completionTimes[i],sep="\t\t")

    def calculateAll(self):
        self.execute()
        self.calcTurnAroundTime()
        self.printTable()
        self.calcAvgWaitingTime()
        self.calcAvgTurnAroundTime()
        

class Priority_nonPreemptive:
    def __init__(self):
        self.numProcesses = int(input("Enter number of processes: "))
        self.processes = [int(i) for i in input("Enter processes: ").split(",")]
        self.arrivalTimes = [int(i) for i in input("Enter arrival times: ").split(",")]
        self.burstTimes = [int(i) for i in input("Enter burst times: ").split(",")]
        self.priorities = [int(i) for i in input("Enter priorities: ").split(",")]
        self.waitingTimes = [0] * self.numProcesses
        self.turnAroundTimes = [0] * self.numProcesses
        self.completionTimes = [0] * self.numProcesses
        self.completed = [False] * self.numProcesses

    def execute(self):
        completedProcesses = 0
        time  = 0
        jobID = -1
        minPriority = 999
        while completedProcesses < self.numProcesses:
            jobID = -1
            minPriority = 999
            for i in range(self.numProcesses):
                if (self.arrivalTimes[i] <= time) and (self.priorities[i] < minPriority) and (self.completed[i] == False):
                    jobID = i
                    minPriority = self.priorities[i]
            if time == 0:
                print("Gantt Chart:\n")
                print("| 0 |",end=" ")

            time += self.burstTimes[jobID]
            self.completionTimes[jobID] = time
            self.completed[jobID] = True
            completedProcesses += 1
            self.turnAroundTimes[jobID] = self.completionTimes[jobID] - self.arrivalTimes[jobID]
            self.waitingTimes[jobID] = self.turnAroundTimes[jobID] - self.burstTimes[jobID]
            print("P" + str(jobID + 1) + " | " + str(time) + " | ",end="")
        print("\n")

    def printTable(self):
        print("Processes\tArrival Times\tBurst Times\tWaiting Time\tTurn Around Time  Completion Time  Priorities\n")
        for i in range(self.numProcesses):
            print(self.processes[i],self.arrivalTimes[i],self.burstTimes[i],self.waitingTimes[i],self.turnAroundTimes[i],self.completionTimes[i],self.priorities[i],sep="\t\t")

    def calcAvgWaitingTime(self):
        avgWaitingTime = 0
        for i in range(self.numProcesses):
            avgWaitingTime += self.waitingTimes[i]
        avgWaitingTime = avgWaitingTime / self.numProcesses
        print("Average waiting Time is: ",avgWaitingTime)
        return None 
    
    def calcAvgTurnAroundTime(self):
        avgTurnAroundTime = 0
        for i in range(self.numProcesses):
            avgTurnAroundTime += self.turnAroundTimes[i]
        avgTurnAroundTime = avgTurnAroundTime / self.numProcesses
        print("Average Turn Around Time is: ",avgTurnAroundTime)
        return None

    def excecuteAll(self):
        self.execute()
        self.printTable()
        self.calcAvgTurnAroundTime()
        self.calcAvgWaitingTime()





class Priority_Preemptive:
    def __init__(self):
        self.numProcesses = int(input("Enter number of processes: "))
        self.processes = [int(i) for i in input("Enter processes: ").split(",")]
        self.arrivalTimes = [int(i) for i in input("Enter arrival times: ").split(",")]
        self.burstTimes = [int(i) for i in input("Enter burst times: ").split(",")]
        self.priorities = [int(i) for i in input("Enter priorities: ").split(",")]
        self.waitingTimes = [0] * self.numProcesses
        self.turnAroundTimes = [0] * self.numProcesses
        self.completionTimes = [0] * self.numProcesses
    

    def execute(self):
        remainingTime = []
        totalTime = 0
        for i in range(self.numProcesses):
            remainingTime.append(self.burstTimes[i])
            totalTime += self.burstTimes[i]
        prevJob = -1
        jobID = -1
        minPriority = 99
        for time in range(totalTime + 1):
            for i in range(self.numProcesses):
                if (self.arrivalTimes[i] <= time) and (remainingTime[i] > 0) and (self.priorities[i] < minPriority):
                    jobID = i
                    minPriority = self.priorities[i]
            
            remainingTime[jobID] -= 1
            
            if remainingTime[jobID] == 0:
                finishTime = time + 1
                self.waitingTimes[jobID] = finishTime - self.arrivalTimes[jobID] - self.burstTimes[jobID]
                self.completionTimes[jobID] = finishTime
                self.turnAroundTimes[jobID] = self.completionTimes[jobID] - self.arrivalTimes[jobID]
                minPriority = 999

                if self.waitingTimes[jobID] < 0:
                    self.waitingTimes[jobID] = 0
            
            if (time == 0):
                print("Gantt Chart:")
                print("0 | P" + str(jobID + 1),end= " | ")
            elif (time == totalTime):
                print(str(totalTime))
            elif jobID != prevJob:
                print(str(time) + " | " + "P" + str(jobID + 1),end=" | ")
            prevJob = jobID
        return None

    def printTable(self):
        print("Processes\tArrival Times\tBurst Times\tWaiting Time\tTurn Around Time  Completion Time  Priorities\n")
        for i in range(self.numProcesses):
            print(self.processes[i],self.arrivalTimes[i],self.burstTimes[i],self.waitingTimes[i],self.turnAroundTimes[i],self.completionTimes[i],self.priorities[i],sep="\t\t")

    def calcAvgWaitingTime(self):
        avgWaitingTime = 0
        for i in range(self.numProcesses):
            avgWaitingTime += self.waitingTimes[i]
        avgWaitingTime = avgWaitingTime / self.numProcesses
        print("Average waiting Time is: ",avgWaitingTime)
        return None 
    
    def calcAvgTurnAroundTime(self):
        avgTurnAroundTime = 0
        for i in range(self.numProcesses):
            avgTurnAroundTime += self.turnAroundTimes[i]
        avgTurnAroundTime = avgTurnAroundTime / self.numProcesses
        print("Average Turn Around Time is: ",avgTurnAroundTime)
        return None

    def excecuteAll(self):
        self.execute()
        self.printTable()
        self.calcAvgTurnAroundTime()
        self.calcAvgWaitingTime()



class roundRobin:
    def __init__(self):
        self.numProcesses = int(input("Enter number of processes: "))
        self.processes = [int(i) for i in input("Enter processes: ").split(",")]
        self.arrivalTimes = [int(i) for i in input("Enter arrival times: ").split(",")]
        self.burstTimes = [int(i) for i in input("Enter burst times: ").split(",")]
        self.timeQuantum = int(input("Enter time quantum value: "))
        self.waitingTimes = [0] * self.numProcesses
        self.turnAroundTimes = [0] * self.numProcesses
        self.completionTimes = [0] * self.numProcesses
        self.completed = [False] * self.numProcesses


    def execute(self):
        remainingTimes = [0] * self.numProcesses
        currentJob = -1
        minArr = 999
        for i in range(self.numProcesses):
            remainingTimes[i] = self.burstTimes[i]
            if self.arrivalTimes[i] < minArr:
                currentJob = i
                minArr = self.arrivalTimes[i]
        queueArray = []
        queueArray.append(currentJob)
        queueFront = 0
        completedProcesses = 0
        time = minArr
        print("\nGantt Chart:")
        print(str(minArr) + " | ",end="")
        while True:
            for t in range(time + 1,time + self.timeQuantum + 1):
                for i in range(self.numProcesses):
                    if(t == self.arrivalTimes[i]) and (i != currentJob):
                        queueArray.append(i)

            if remainingTimes[currentJob] > self.timeQuantum:
                time += self.timeQuantum
                remainingTimes[currentJob] -= self.timeQuantum
                print("P" + str(currentJob + 1) + " | " + str(time),end = " | ")
                queueArray.append(currentJob)

            else:
                time += remainingTimes[currentJob]
                remainingTimes[currentJob] = 0
                self.completionTimes[currentJob] = time
                self.completed[currentJob] = True
                completedProcesses += 1
                self.turnAroundTimes[currentJob] = self.completionTimes[currentJob] - self.arrivalTimes[currentJob]
                self.waitingTimes[currentJob] = self.turnAroundTimes[currentJob] - self.burstTimes[currentJob]
                print("P" + str(currentJob + 1) + " | " + str(time),end = " | ")
            if completedProcesses == self.numProcesses:
                break
            queueFront += 1
            currentJob = queueArray[queueFront]
        print("\n")

    def printTable(self):
        print("Processes\tArrival Times\tBurst Times\tWaiting Time\tTurn Around Time  Completion Time\n")
        for i in range(self.numProcesses):
            print(self.processes[i],self.arrivalTimes[i],self.burstTimes[i],self.waitingTimes[i],self.turnAroundTimes[i],self.completionTimes[i],sep="\t\t")

    def calcAvgWaitingTime(self):
        avgWaitingTime = 0
        for i in range(self.numProcesses):
            avgWaitingTime += self.waitingTimes[i]
        avgWaitingTime = avgWaitingTime / self.numProcesses
        print("Average waiting Time is: ",avgWaitingTime)
        return None 
    
    def calcAvgTurnAroundTime(self):
        avgTurnAroundTime = 0
        for i in range(self.numProcesses):
            avgTurnAroundTime += self.turnAroundTimes[i]
        avgTurnAroundTime = avgTurnAroundTime / self.numProcesses
        print("Average Turn Around Time is: ",avgTurnAroundTime)
        return None

    def excecuteAll(self):
        self.execute()
        self.printTable()
        self.calcAvgTurnAroundTime()
        self.calcAvgWaitingTime()


print("1>FCFS\n",
     "2>STRF\n",
     "3>Priority(Non-Preemptive)\n",
     "4>Priority(Preemptive)\n",
     "5>Round Robin\n")
while True:
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        print("\nFirst Come First Serve:")
        obj1 = FCFS()
        obj1.calculateAll()
    elif (choice == 2):
        print("\nShortest Time Remaining First:")
        obj2 = STRF()
        obj2.calculateAll()
    elif (choice == 3):
        print("\nPriority Scheduling Non-Preemptive:")
        obj3 = Priority_nonPreemptive()
        obj3.excecuteAll()
    elif (choice == 4):
        print("\nPriority Scheduling Preemptive:")
        obj4 = Priority_Preemptive()
        obj4.excecuteAll()
    elif (choice == 5):
        print("\nRound Robin")
        obj5 = roundRobin()
        obj5.excecuteAll()
    else:
        break





# 1>FCFS
#  2>STRF
#  3>Priority(Non-Preemptive)
#  4>Priority(Preemptive)
#  5>Round Robin

# Enter your choice: 1

# First Come First Serve:
# Enter number of processes: 3
# Enter processes: 1,2,3
# Enter arrival times: 0,1,2
# Enter burst times: 24,3,3

# Gantt Chart:
# 0 | P1 | 24 | P2 | 27 | P3 | 30 |

# Processes	Arrival Times	Burst Times	Waiting Time	Turn Around Time  Completion Time

# 1		0		24		0		24		24
# 2		1		3		23		26		27
# 3		2		3		25		28		30
# Average waiting Time is:  16.0
# Average Turn Around Time is:  26.0
# Enter your choice: 2

# Shortest Time Remaining First:
# Enter number of processes: 6
# Enter processes: 1,2,3,4,5,6
# Enter arrival times: 0,1,2,3,4,5
# Enter burst times: 8,4,2,1,3,2
# Gantt Chart:
# 0 | P1 | 1 | P2 | 2 | P3 | 4 | P4 | 5 | P6 | 7 | P2 | 10 | P5 | 13 | P1 | 20
# Processes	Arrival Times	Burst Times	Waiting Time	Turn Around Time  Completion Time

# 1		0		8		12		20		20
# 2		1		4		5		9		10
# 3		2		2		0		2		4
# 4		3		1		1		2		5
# 5		4		3		6		9		13
# 6		5		2		0		2		7
# Average waiting Time is:  4.0
# Average Turn Around Time is:  7.333333333333333
# Enter your choice: 3

# Priority Scheduling Non-Preemptive:
# Enter number of processes: 7
# Enter processes: 1,2,3,4,5,6,7
# Enter arrival times: 0,2,1,4,6,5,7
# Enter burst times: 3,5,4,2,9,4,10
# Enter priorities: 2,6,3,5,7,4,10
# Gantt Chart:

# | 0 | P1 | 3 | P3 | 7 | P6 | 11 | P4 | 13 | P2 | 18 | P5 | 27 | P7 | 37 | 

# Processes	Arrival Times	Burst Times	Waiting Time	Turn Around Time  Completion Time  Priorities

# 1		0		3		0		3		3		2
# 2		2		5		11		16		18		6
# 3		1		4		2		6		7		3
# 4		4		2		7		9		13		5
# 5		6		9		12		21		27		7
# 6		5		4		2		6		11		4
# 7		7		10		20		30		37		10
# Average Turn Around Time is:  13.0
# Average waiting Time is:  7.714285714285714
# Enter your choice: 5

# Round Robin
# Enter number of processes: 6 
# Enter processes: 1,2,3,4,5,6
# Enter arrival times: 0,1,2,3,4,6
# Enter burst times: 5,6,3,1,5,4
# Enter time quantum value: 4

# Gantt Chart:
# 0 | P1 | 4 | P2 | 8 | P3 | 11 | P4 | 12 | P5 | 16 | P1 | 17 | P6 | 21 | P2 | 23 | P5 | 24 | 

# Processes	Arrival Times	Burst Times	Waiting Time	Turn Around Time  Completion Time

# 1		0		5		12		17		17
# 2		1		6		16		22		23
# 3		2		3		6		9		11
# 4		3		1		8		9		12
# 5		4		5		15		20		24
# 6		6		4		11		15		21
# Average Turn Around Time is:  15.333333333333334
# Average waiting Time is:  11.333333333333334
# Enter your choice: 6
