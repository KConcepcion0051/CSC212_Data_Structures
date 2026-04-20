# Kevin Concepcion CSC 212-01 Country exercise

# This program will read in a data file of countries and their 
# population and GDP, create a list of Country objects, and 
# then display the countries sorted by population, GDP, and 
# GDP per capita. The Country class has methods to get and set 
# the name, population, and GDP, as well as a method to compute 
# the GDP per capita. The main function reads the data file, 
# creates Country objects, and sorts and displays the countries 
# based on different attributes.

import operator

class Country:
    def __init__(self, name, population, gdp):
        self.name = name
        self.population = population
        self.gdp = gdp#gross domestic product (GDP) 
        # compute GDP per capita
        self.computeGdpPerCapita()
        
    def display(self):
        print("%-10s %12d %12d %12d" \
              % (self.name, self.population / 1000000, \
                 self.gdp / 1000000000, self.perCapita))
        
    def getName(self):
        return self.name
    
    def getPopulation(self):
        return self.population
    
    def getGdp(self):
        return self.gdp
    
    def setName(self, name):
        self.name = name
        
    def setPopulation(self, population):
        self.population = population
        self.computeGdpPerCapita()
        
    def setGdp(self, gdp):
        self.gdp = gdp
        self.computeGdpPerCapita()
        
    def computeGdpPerCapita(self):
        self.perCapita = self.gdp / self.population
    
    
def main():
    # open data file
    filename = input("Enter name of countries data file: ")
    fin = open(filename, 'r')
    
    countryList = []
    for record in fin:
        name, gdp, pop = record.split("\t")
        country = Country(name, int(pop), int(gdp))
        countryList.append(country)
        
    print("\n\n*** Countries sorted by population *** ")
    print("Name         Pop. (Mil)   GDP ($Bil)    Per Capita ($)")
    for country in sorted(countryList, key=operator.attrgetter('population')):
        country.display()

    print("\n\n*** Countries sorted by GPD: ")
    print("Name         Pop. (Mil)   GDP ($Bil)    Per Capita ($)")
    for country in sorted(countryList, key=operator.attrgetter('gdp')):
        country.display()    

    print("\n\n*** Countries sorted by GPD per capita: ")
    print("Name         Pop. (Mil)   GDP ($Bil)    Per Capita ($)")
    for country in sorted(countryList, key=operator.attrgetter('perCapita')):
        country.display() 

if __name__ == "__main__":
    main()
        
