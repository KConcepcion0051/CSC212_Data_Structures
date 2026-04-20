#CSC 212 Kevin Concepcion  Assignment 5
from Employee import Employee
from Queue import Queue

# This function accepts the 'q' parameter which is a queue created from main. The function opens the .txt file and creates an employee object
# for each line (each word per line is seperated by \t) then all the objects are passed added into the queue. Every employee in the queue gets 
# dequeue then enqueue to ensure correct order is maintained
def extract(q):
    fin = open('humanResource.txt','r')
    for line in fin:
        first, last, pay = line.split("\t")
        line = Employee(first,last, int(pay))
        q.enqueue(line)
    
    
# This function goes through the queue and for each employee the bonus gets calculated and set for that employee. The starting employee gets 
# a 20% bonus of their pay then for every other employee the bonus percentage increments by -1%. dec varible gets set to 0.20 then decreases 
# by 0.01 after each iteration. Every employee in the queue gets dequeue then enqueue to ensure correct order is maintained
def add_bonus(q):
    dec = 0.20
    for i in range(q.size()):
        emp = q.dequeue()
        
        new_bonus = (emp.getPay())* (dec)
        emp.setBonus(round(new_bonus))
        dec -= 0.01
        
        #print(f"Employee: {emp.fullName()}, pay: {emp.getPay()}, bonus: {emp.getBonus()}")
       
        q.enqueue(emp)
     
    print("\nCurrent count of employees: ",q.size(),"\n")
    q.print_queue()
        
        
# This function goes through the queue, gets the bonus of each employee and adds the value to a variable called bonus_sum to reflect the total 
# amount of bonuses that the company is paying. Every employee in the queue gets dequeue then enqueue to ensure correct order is maintained
def calc_bonus(q,bonus_sum):
    for i in range(q.size()):
        emp = q.dequeue()
        
        bonus_sum += emp.getBonus()
        
        q.enqueue(emp)
    print("Sum of employee bonus: ",bonus_sum)


    
        
def main():
    q = Queue()
    
    bonus_sum = 0
    extract(q)
    add_bonus(q)
    calc_bonus(q,bonus_sum)
    
    
    
if __name__ == "__main__":
    main()