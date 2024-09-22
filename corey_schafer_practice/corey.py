class Employee:
    # I want to indicate my EMPLOYEE class that I need to create an INSTANCE of it, 1 specific employee, with a series of attributes.
    def __init__(self, first_name, last_name, employeepay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = employeepay
        self.email = first_name + "." + last_name + "@company.com"

    # Now, I want to create a method that prints the full name of an employee without me needing to type in a ton of code.

    # Every method within a class will take the instance of that class as its first argument by default.
    def print_full_employee_name(self):
        return f"This is employee {self.first_name} {self.last_name}"


employee_1 = Employee("Corey", "Schafer", "5000")
employee_2 = Employee("Yami", "Lemos", "6000")
print(employee_1.print_full_employee_name())
