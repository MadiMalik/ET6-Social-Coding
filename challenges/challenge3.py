# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib_venn import venn2


"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 3: Access Visualization
Objective
Develop a visual representation of the company's access control system to identify patterns, overlaps, and security risks.
Scenario
The company’s security team is struggling to interpret raw access data. They need a clear way to see:
Employees who have access to financial records, technical documents, or both.
Employees with no access, who may need onboarding.
Any overlap that could indicate excessive privileges or security risks.
Instead of listing raw data, your task is to create a structured representation that makes these relationships intuitive and easy to understand.
Your Task
Using the provided employee access data, design a way to illustrate:
Who belongs where? Group employees based on their level of access.
Where is the overlap? Show employees who have access to both financial and technical records.
Who is left out? Identify employees without access.
Are there risks? Indicate employees who might be exposed to unnecessary data.
Your output should visually highlight these relationships without explicitly listing them in a simple table or list. Think beyond just printing data—use a format that helps detect patterns at a glance.
"""


finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
admin = {"E0001"}
new_employee = {"E9999"}

both_access = finance_access.union(tech_access)
finance_only = finance_access.difference(tech_access)
tech_only = tech_access.difference(finance_access)
no_access = new_employee


venn = venn2([finance_access, tech_access], ('Finance Access', 'Tech Access'))
plt.title("Employee Access Visualization")
plt.annotate(f"No Access: {', '.join(no_access)}", xy=(-0.5, -0.4),
             xycoords='axes fraction', fontsize=12, color='red')
plt.annotate(f"Admin: {', '.join(admin)} (Access to all data)",
             xy=(-0.5, -0.5), xycoords='axes fraction', fontsize=12, color='blue')

plt.show()
