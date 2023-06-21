import time,random
class process:
    def __init__(self,id) -> None:
        self.id = id
        self.active = True

class ring:
    def __init__(self) -> None:
        self.numProcess = int(input("Enter number of processes: "))
        self.processes = [process(i) for i in range(1,self.numProcess + 1)]

    def getMaxId(self):
        maxID = -1
        for process in self.processes:
            if process.active == True and process.id > maxID:
                maxID = process.id
        return maxID - 1
    
    def performElection(self):
        time.sleep(0.5)
        print(f"Process number {self.getMaxId() + 1} has failed.")
        failedProcessId= self.getMaxId() + 1
        self.processes[self.getMaxId()].active = False
        randomProcessId = random.randint(1,self.numProcess)
        while randomProcessId == failedProcessId:
            randomProcessId = random.randint(1,self.numProcess)
        time.sleep(0.25)
        print(f"Election initiated by process {randomProcessId}")
        
        previous = randomProcessId - 1
        next = previous + 1
        msg = []
        while True:
            if self.processes[next].active == True:
                msg.append(previous+1)
                print(f"Process {previous + 1} passes election({msg}) message to process {next + 1}")
                previous = next
            if ((next + 1) % self.numProcess) == randomProcessId - 1:
                msg.append(previous + 1)
                print(f"Process {previous + 1} passes election({msg}) message to process {randomProcessId}")
                break
            else:
                next = (next + 1) % self.numProcess
        
        time.sleep(0.25)
        print(f"Process {self.getMaxId() + 1} becomes coordinator")
        coordinator = self.getMaxId()
        previous = randomProcessId - 1
        next = previous + 1
        while True:
            if self.processes[next].active == True:
                print(f"Process {previous + 1} passes coordinator({coordinator + 1}) message to process {next + 1}")
                previous = next
            if ((next + 1) % self.numProcess) == randomProcessId - 1:
                print(f"Process {previous + 1} passes coordinator({coordinator + 1}) message to process {randomProcessId}")
                break
            else:
                next = (next + 1) % self.numProcess
            
    
        print("End of election")

ringSimulation = ring()
ringSimulation.performElection()

# OUTPUT
# Enter number of processes: 5
# Process number 5 has failed.
# Election initiated by process 2
# Process 2 passes election([2]) message to process 3
# Process 3 passes election([2, 3]) message to process 4
# Process 4 passes election([2, 3, 4]) message to process 1
# Process 1 passes election([2, 3, 4, 1]) message to process 2
# Process 4 becomes coordinator
# Process 2 passes coordinator(4) message to process 3
# Process 3 passes coordinator(4) message to process 4
# Process 4 passes coordinator(4) message to process 1
# Process 1 passes coordinator(4) message to process 2
# End of election
