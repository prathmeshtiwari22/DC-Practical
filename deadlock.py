class Process :

    def __init__(self,pid):
        self.pid = pid
        self.waiting_for = None

    def detectdeadlock(self,initiator):
        
        if self.waiting_for == None :
            print('waiting for no one')
            return False
        
        probe = [initiator,self.pid,self.waiting_for.pid] 
        print(f'{self.pid} send {probe} to {self.waiting_for.pid}')

        if self.waiting_for.pid == initiator :
            print(f'deadlock detected !')
            return True
        
        return self.waiting_for.detectdeadlock(initiator)

p1 = Process(1)
p2 = Process(2)
p3 = Process(3)
p1.waiting_for = p2
p2.waiting_for = p3
p3.waiting_for = p1  # Cycle formed

print("\n--- Deadlock Test ---")
if p1.detectdeadlock(p1.pid):
    print("Deadlock confirmed.")
else:
    print("No deadlock detected.")

# --- No Deadlock Example ---
p4 = Process(4)
p5 = Process(5)
p4.waiting_for = p5
p5.waiting_for = None  # No cycle

print("\n--- No Deadlock Test ---")
if p4.detectdeadlock(p4.pid):
    print("Deadlock confirmed.")
else:
    print("No deadlock detected.")

# output : 
#--- Deadlock Test ---
#1 send [1, 1, 2] to 2
#2 send [1, 2, 3] to 3
#3 send [1, 3, 1] to 1
#deadlock detected !
#Deadlock confirmed.

#--- No Deadlock Test ---
#4 send [4, 4, 5] to 5
#waiting for no one
#No deadlock detected.
