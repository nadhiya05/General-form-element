class Employee:
    __fname = ""
    __lname = ""
    __salary = 0
    __increment=0
    def setData(self, fname, lname, salary,increment):
        self.__fname=fname
        self.__lname=lname
        self.__salary = salary
        self.__increment=increment
        self.__total=self.__salary*self.__increment
    def showData(self):
        print("Values Are:", self.__fname,self.__lname,self.__salary)
        print("The total value is:",self.__total)

def main():
    emp = Employee()
    emp.setData('dheeraj', 'kushwaha', 25000,1.5)
    emp.showData()


if __name__ == "__main__":
    main()