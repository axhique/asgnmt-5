class student:
    __name=None
    __rollnumber=0

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def setRollNumber(self,r_no):
        self.__rollnumber=r_no

    def getRollNumber(self):
        return self.__rollnumber

a=student()

a.setName('Aash')
print(a.getName())

a.setRollNumber(55)
print(a.getRollNumber())
