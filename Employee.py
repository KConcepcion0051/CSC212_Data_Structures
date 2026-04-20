#This program is to demo the use of classes
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        self.bonus = 0

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay=pay
        
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def getBonus(self):
        return self.bonus
    
    def setBonus(self,new_Bonus):
        self.bonus = new_Bonus       

    def __str__(self):
       
       return 'Employee name: '+self.fullName()+', Pay: ' +str(self.pay) + ', Bonus :'+str(self.bonus)

