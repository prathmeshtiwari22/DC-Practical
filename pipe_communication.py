# pipe_communication.py

from multiprocessing import Process, Pipe

def child(conn):
    print("Child: waiting for data...")
    msg = conn.recv()  # Receive message from parent
    print(f"Child received: {msg}")
    conn.send("Hello from child!")  # Send response

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    # Create child process
    p = Process(target=child, args=(child_conn,))
    p.start()

    # Send message to child
    parent_conn.send("Hello from parent!")
    print("Parent: sent data to child.")

    # Receive message from child
    msg = parent_conn.recv()
    print(f"Parent received: {msg}")

    # Wait for child to finish
    p.join()


#py pipe_communication.py

#Parent: sent data to child.
#Child: waiting for data...
#Child received: Hello from parent!
#Parent received: Hello from child!