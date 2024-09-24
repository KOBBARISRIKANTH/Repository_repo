# Employee data
emp = {
    "ename": ["Srikanth", "kesava", "Jani", "sai", "Raj"],
    "Age": [23, 34, 45, 32, 54],
    "Salary": [65000, 23000, 27000, 14000, 19000]
}
l1=emp["Salary"]
#Total salary of the employees
print("Total salary is:",sum(l1))
#Maximum salary of the employee
print("maximum salary of the employee:",max(l1))
#minumum salary of the employee
print("minimum salary of the employee:",min(l1))

# Find the index of the employee with the highest salary
max_age_index = emp["Salary"].index(max(emp["Salary"]))

# Get the details of the employee with the highest salary
employee_name = emp["ename"][max_age_index]
#employee_age = emp["Age"][max_age_index]
#employee_salary = emp["Salary"][max_age_index]
print("Employee name with highest salary is:",employee_name)
# List to store names of employees with salary greater than 25000
high_salary_employees = []

# Iterate through the salaries and check if they are greater than 25000
for i in range(len(emp["Salary"])):
    if emp["Salary"][i] > 25000:
        high_salary_employees.append(emp["ename"][i])

print("Employees with salary greater than ₹25,000:", high_salary_employees)


#mani prathap
#mani
