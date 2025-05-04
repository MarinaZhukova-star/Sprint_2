class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        if cls.hours is None:
            cls.hours = (7 - self.rest_days) * 8
        return cls(name, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        if cls.email is None:
            cls.email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    
    def salary(self):
        return self.hours * self.hourly_payment
    
employee1 = EmployeeSalary(name = "Иванов", hours = 40, rest_days=4, email = None)
print("Имя сотрудника:", employee1.name, "количество выходных:", employee1.rest_days, "зарплата:", employee1.salary(), "email:", employee1.email)