import time
class process:
    def __init__(self,id) -> None:
        self.id = id
        self.active = True

class bully:
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
        time.sleep(1)
        print(f"Process number {self.getMaxId() + 1} has failed.")
        self.processes[self.getMaxId()].active = False

        initiator = 0
        while True: #Loop until co-ordinator is found
            higherValueIdActive = False
            time.sleep(0.5)
            for i in range(initiator+1,self.numProcess):
                if self.processes[i].active == True:
                    print(f"Process {initiator + 1} passes election ({initiator + 1}) message to process {i+1}")
                    higherValueIdActive = True
            print("\n")
            #confirmation from processes having higher valued IDs
            if (higherValueIdActive == True):
                time.sleep(0.5)
                for i in range(initiator + 1,self.numProcess):
                    if self.processes[i].active == True:
                        print(f"Process {i+1} passes confirmation OK({i+1}) message to process {initiator + 1}")
                print("\n")
                initiator += 1
            #when no processes having higher valued IDs are available
            else:
                coordinator = self.getMaxId()
                time.sleep(0.5)
                print(f"Finally process {coordinator + 1} becomes the coordinator.")
                for i in range(self.numProcess):
                    time.sleep(0.25)
                    if self.processes[i].active == True and i != coordinator:
                        print(f"Process {coordinator + 1} passes coordinator ({coordinator + 1}) message to process {i+1}")
                print("\nEnd Of Election")
                break


bullySimulation = bully()
bullySimulation.performElection()


"""
OUTPUT:
Enter number of processes: 5
Process number 5 has failed.
Process 1 passes election (1) message to process 2
Process 1 passes election (1) message to process 3
Process 1 passes election (1) message to process 4


Process 2 passes confirmation OK(2) message to process 1
Process 3 passes confirmation OK(3) message to process 1
Process 4 passes confirmation OK(4) message to process 1


Process 2 passes election (2) message to process 3
Process 2 passes election (2) message to process 4


Process 3 passes confirmation OK(3) message to process 2
Process 4 passes confirmation OK(4) message to process 2


Process 3 passes election (3) message to process 4


Process 4 passes confirmation OK(4) message to process 3




Finally process 4 becomes the coordinator.
Process 4 passes coordinator (4) message to process 1
Process 4 passes coordinator (4) message to process 2
Process 4 passes coordinator (4) message to process 3

End Of Election
"""
