# ring_election.py

class Process:
    def __init__(self, pid):
        self.pid = pid
        self.active = True

def ring_election(processes, initiator_index):
    print(f"Election initiated by Process {processes[initiator_index].pid}")
    n = len(processes)
    msg = processes[initiator_index].pid
    i = (initiator_index + 1) % n

    while i != initiator_index:
        if processes[i].active:
            print(f"Process {processes[i].pid} received message: {msg}")
            if processes[i].pid > msg:
                msg = processes[i].pid
        i = (i + 1) % n

    print(f"Process {msg} is elected as the new coordinator (leader).")

# Example usage
if __name__ == "__main__":
    # Create 5 processes with IDs
    processes = [Process(3), Process(1), Process(4), Process(2), Process(5)]

    # Start election from process at index 1 (ID = 1)
    ring_election(processes, 1)


# py ring.py
#Election initiated by Process 1
#Process 4 received message: 1
#Process 2 received message: 4
#Process 5 received message: 4
#Process 3 received message: 5
#Process 5 is elected as the new coordinator (leader).