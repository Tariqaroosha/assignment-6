class Employee:
    def __init__(self,name,_salary,__ssn):
        self.name = name
        self._salary = _salary
        self.__ssn = __ssn

if __name__ == "__main__":
   emp = Employee("aroosha",5000, "123-456-789")

   print("public variable",emp.name)

   print("protected variable",emp._salary)

   
   print("private variable",emp._Employee__ssn)
