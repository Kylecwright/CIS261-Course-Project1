def get_dates():
    from_date = input("Enter from date (mm/dd/yyyy): ")
    to_date = input("Enter to date (mm/dd/yyyy): ")
    return from_date, to_date


def get_employee_data():
    from_date, to_date = get_dates()
    employee_name = input("Enter employee name: ")
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    tax_rate = float(input("Enter income tax rate (example 0.15 for 15%): "))

    return [from_date, to_date, employee_name, hours_worked, hourly_rate, tax_rate]


def process_payroll(employee_list):
    totals = {
        "employee_count": 0,
        "total_hours": 0,
        "total_tax": 0,
        "total_net_pay": 0
    }

    print("\nEmployee Payroll Details")
    print("-" * 50)

    for employee in employee_list:
        from_date = employee[0]
        to_date = employee[1]
        employee_name = employee[2]
        hours_worked = employee[3]
        hourly_rate = employee[4]
        tax_rate = employee[5]

        gross_pay = hours_worked * hourly_rate
        income_tax = gross_pay * tax_rate 
        net_pay = gross_pay - income_tax

        print(f"Fron Date: {from_date}")
        print(f"To Date: {to_date}")
        print(f"Employee Name: {employee_name}")
        print(f"Hours Worked: {hours_worked}")
        print(f"Hourly Rate: ${hourly_rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {tax_rate:.2%}")
        print(f"Income Taxes: ${income_tax:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print("-" * 50)

        totals["employee_count"] += 1
        totals["total_hours"] += hours_worked
        totals["total_tax"] += income_tax
        totals["total_net_pay"] += net_pay

    return totals


def display_totals(totals):
    print("\nPayroll Totals")
    print("-" * 30)
    print(f"Total Number of Employees: {totals['employee_count']}")
    print(f"Total Hours Worked: {totals['total_hours']}")
    print(f"Total Income Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")


def main():
    employee_list = []

    while True:
        employee_data = get_employee_data()
        employee_list.append(employee_data)

        another_employee = input("Enter another employee? (yes/no): ").lower()
        if another_employee != "yes":
            break


    totals = process_payroll(employee_list)
    display_totals(totals)


main()

          

