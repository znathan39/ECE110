"""
Created on Fri Oct 11 18:12:15 2024

@author: Nathan Zou
"""

import numpy as np
import matplotlib.pyplot as plt

#Tutorial Graph

voltage = np.array([0,1,2,3,4,5,6,7,8,9,10])
current = np.array([0,1,4,9,16,25,36,49,64,81,100])

plt.figure()
plt.plot(voltage,current)

plt.title('My First Python Plot: nzou3')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.grid(axis='both')


# Bar graph of FA24 New Beginning Freshmen 10-Day Profile
# Data from https://dmi.illinois.edu/stuenr/abstracts/fa24freshman_ten.htm

# Data
categories = ['Agr, Cons, Env Sci', 'Applied Health Sci', 'Business', 'Education',
              'Fine & Applied Arts', 'General Studies', 'Grainger Engineering',
              'Liberal Arts & Sci', 'Media', 'School of Information Scie', 
              'School of Social Work']
students = [642, 426, 661, 200, 427, 1088, 2454, 2656, 158, 211, 85]

# Create figure and axes
fig, axis = plt.subplots(figsize=(12, 6))

bar_width = 0.4
index = np.arange(len(categories))
bars = axis.bar(index, students, bar_width, color='skyblue')

for bar in bars:
    height = bar.get_height()
    axis.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')

axis.set_ylabel('Number of Students')
axis.set_xlabel('College')
axis.set_title('UIUC FA24 Freshman 10-Day Profile - Enrollment by College: nzou3')
plt.xticks(index, categories, rotation=45, ha="right")

plt.subplots_adjust(left=0.2, bottom=0.3)
plt.show()


# Pie graph of FA24 Freshman Grainger Engineering Breakdown by Major
# Data from https://dmi.illinois.edu/stuenr/class/enrfa24.htm

# Data
categories = ['Physics', 'CS + Physics',  'Environmental', 'Civil', 'CS + BioE', 'Bio', 'Neural',  
              'Industrial', 'Systems Engineering and Design', 'CS', 'Undeclared', 'Aerospace', 
              'Engr Mechanics', 'MechE', 'MechSE', 'CE', 'EE', 'Nuclear, Plasma, Radiologic Engr']
values = [87, 8, 34, 120, 9, 56, 8, 43, 44, 51, 138, 99, 10, 102, 35, 77, 90, 20]

colors = plt.get_cmap('tab20')(np.linspace(0, 1, len(categories)))

# Create figure
plt.figure(figsize=(12, 14))
wedges, texts, autotexts = plt.pie(values, labels=categories, autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(values) / 100), 
                                   startangle=140, colors=colors)
plt.text(0, 0, 'Total: 1031', horizontalalignment='center', verticalalignment='center', fontsize=14, fontweight='bold')


for i, text in enumerate(texts):
    text.set_color(wedges[i].get_facecolor())

plt.title("UIUC FA24 Freshman Grainger Engineering Breakdown by Major: nzou3", pad=40)
plt.axis('equal')
plt.show()
