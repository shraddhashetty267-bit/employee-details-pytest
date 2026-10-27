def employee_details(name, employee_id, department, salary):
    return (
        f"Name: {name}\n"
        f"Employee ID: {employee_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
print(employee_details("Rahul", 101, "IT", 30000))