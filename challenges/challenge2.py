# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""


def access_control(employee_id):
    finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
    tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
    new_employee = {"E9999"}
    admin = {"E0001"}

    # This condition is not necessary
    # Employees with access to at least one type of data
    # employees_with_access_at_leat_one = finance_access.union(tech_access)

    # Employees with access to both financial and technical data
    employees_with_access_both = admin.union(
        finance_access.intersection(tech_access))

    # Employees with exclusive access to only one type of data
    employees_with_access_only_finance_access = finance_access.difference(
        tech_access)
    employees_with_access_only_tech_access = tech_access.difference(
        finance_access)

    # Employees who lack access
    no_access = new_employee

    print(employees_with_access_both)
    if employee_id in employees_with_access_both:
        return "Access to both financial and technical data"
    elif employee_id in employees_with_access_only_finance_access:
        return "Exclusive access to financial data"
    elif employee_id in employees_with_access_only_tech_access:
        return "Exclusive access to technical data"
    elif employee_id in no_access:
        return "You are new set in your place"
    else:
        return "You have no access"


print(access_control("E7642"))
print(access_control("E1021"))
print(access_control("E0001"))
