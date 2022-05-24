work_hours = [('Bob',200),('Sarah', 500),('Greg', 150)]

def employee_award(hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month, current_max)

if __name__ == "__main__":
    name,hours = employee_award(work_hours)
    print(name)
    print(hours)