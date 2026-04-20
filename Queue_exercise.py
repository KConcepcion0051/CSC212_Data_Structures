# CSC 212 Kevin Concepcion
# This program demonstrates CPU task scheduling using a queue.

from Assign_5_week_8.Queue import Queue

def cpu_task_sceduler(task_list,time_slice):
    q = Queue()
    
    for i in (task_list):
       q.enqueue(i)
       
    print("Starting CPU Scheduling...")
    while not q.is_empty():
        check = q.dequeue()
        name = check[0]
        time = check[1]
        print(f"\nProcessing {name}, (Remaining time: {time})")
        if time > time_slice:
            time -= time_slice
            q.enqueue((name,time))
            print(f"Time slice used: {time_slice}, {name} is not finished - requeueing with {time} left.")
        else:
            print(f"{name}, finished execution!")
   

def main():
    task_list = [("Task1",12),("Task2",8),("Task3",5),("Task4",10)]
    
    time_slice = 4
    
    s = cpu_task_sceduler(task_list,time_slice)
    
main()
    
    