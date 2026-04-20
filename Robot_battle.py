# CSC 212 Assignment 3 Kevin Concepcion 

# This program is a robot battle game where two robots will fight each other 
# until one of the robot's energy runs out. Each robot has a name, energy, strength, 
# and dodge value. The robots will take turns attacking each other and the attack 
# accuracy is determined by a random number between 0 and 1. If the attack accuracy 
# is greater than the target robot's dodge value, the target robot will lose energy 
# equal to the attacking robot's strength. The program will print out the status of 
# each robot after each attack and declare the winner at the end of the battle.

import random

class robot():                                                  # All of the private fields: name, energy, strenght, dodge(0-1) all these are fixed variables
    def __init__(self,name,energy,strength,dodge):              
        self.__name = name                              
        self.__energy = energy
        self.__strength = strength
        self.__dodge = dodge
# Getter methods for each of the privates fields
    def get_name(self):
        return self.__name
    
    def get_energy(self):
        return self.__energy
    
    def get_strength(self):
        return self.__strength
    
    def get_dodge(self):
        return self.__dodge
    
# Setter for energy
    def set_energy(self,new_energy):
        self.__energy = new_energy
        
# Attack method
    def attack(self):
        self.__energy -= 1
# Recieve attack method takes in attack accuracy and attacking robot as parameters. 
    def recieve_attack(self,attacking_accuracy, attacking_robot):
        if attacking_accuracy > self.get_dodge():
            self.set_energy(self.get_energy() - attacking_robot.get_strength() )
            
# String method to print out robots status. name and energy      
    def __str__(self):
        return f"Robot name is: {self.get_name()}, energy is: {self.get_energy()}"



# Battle method that takes the first robot and second robot and allows them to attack each other until one of the robot's energy runs out
def battle(firstR, secondR):
    firstR.attack()                                                                     # calls attack method takes one value of energy away from the attacking robot
    while firstR.get_energy() > 0 and secondR.get_energy() > 0:
        
        attack_ac = random.random()                                                     # random number between 0,1 to represent the attack acuracy
        print(attack_ac)
        secondR.recieve_attack(attack_ac,firstR)                                        # first robot is attacking so secondR calls the recieve attack method as the target robot
        if attack_ac > secondR.get_dodge():
            print(f"{firstR.get_name()}, attacked {secondR.get_name()},  with a strength of: {firstR.get_strength()}")
        else:
            print(f"{secondR.get_name()} dodged {firstR.get_name()}")
        
        if secondR.get_energy() <=0:
            print(f"{secondR.get_name()}, lost. \n{firstR.get_name()} is the winner!")     # if the second robot lost its energy first robot is declared the winner
            break
        
        print(firstR)                                                                   # prints out the name and status of each of the robots
        print(secondR)
        
        attack_ac = random.random()                                                     # same as before this time second robot is the attacking robot and the first is the target robot
        print(attack_ac)
        firstR.recieve_attack(attack_ac,secondR)
        if attack_ac > secondR.get_dodge():
            print(f"{secondR.get_name()}, attacked {firstR.get_name()},  with a strength of: {secondR.get_strength()}")
        else:
            print(f"{firstR.get_name()} dodged {secondR.get_name()}")
        
        if firstR.get_energy() <=0:
            print(f"{firstR.get_name()}, lost. \n{secondR.get_name()} is the winner!")    # if the first robot lost its energy second robot is declared the winner
            break
        
        print(firstR)
        print(secondR)


def main():                                     # two robot objects
    rb_1 = robot("Bob",10,8,0.6)
    
    print(f"\nThe robot name is: {rb_1.get_name()}, energy is: {rb_1.get_energy()}, strength is: {rb_1.get_strength()}, and dodge is :  {rb_1.get_dodge()}")
    
    rb_2 = robot("Mike",10,4,0.8)
    
    print(f"The robot name is: {rb_2.get_name()}, energy is: {rb_2.get_energy()}, strength is: {rb_2.get_strength()}, and dodge is :  {rb_2.get_dodge()}\n")

    toss = random.randint(0,1)
    

    
    if toss == 0:
        print(f"{rb_1.get_name()}, will be going first\n")
        battle(rb_1,rb_2)
    else:
        print(f"{rb_2.get_name()}, will be going first\n")
        battle(rb_2,rb_1)
if __name__ == "__main__":
    main()


