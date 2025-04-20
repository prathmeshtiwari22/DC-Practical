# lamport.py

class LamportClock:
    def __init__(self, pid):
        self.time = 0
        self.pid = pid

    def event(self):
        self.time += 1
        print(f"Process {self.pid}: Internal Event at time {self.time}")

    def send(self):
        self.time += 1
        print(f"Process {self.pid}: Send Message at time {self.time}")
        return self.time

    def receive(self, sender_time):
        self.time = max(self.time, sender_time) + 1
        print(f"Process {self.pid}: Received Message - updated time to {self.time}")

# Simulate two processes communicating
if __name__ == "__main__":
    p1 = LamportClock(1)
    p2 = LamportClock(2)

    p1.event()
    t = p1.send()
    p2.receive(t)
    p2.event()
    t2 = p2.send()
    p1.receive(t2)


#   py lamport.py
#Process 1: Internal Event at time 1
#Process 1: Send Message at time 2
#Process 2: Received Message - updated time to 3
#Process 2: Internal Event at time 4
#Process 2: Send Message at time 5
#Process 1: Received Message - updated time to 6