# OSS-Repo

## Overview:

 It's a Python command-line program that models an open source software project.

The application handles contributors, issues, data analysis and produces output files (reports
and CSV). It showcases the use of basic Python data structures and highlights aspects of open
source project management, such as issue management, contributor management and data
management.

## Code and Explanation:

## Contributor Management:

```
contributors = []
```
```
for i in range(4):
name = input("Enter contributor name: ")
role = input("Enter role: ")
language = input("Enter programming language: ")
commits = int(input("Enter number of commits: "))
country = input("Enter country: ")
```
```
contributor = {
"name": name,
"role": role,
"language": language,
"commits": commits,
"country": country
}
```
```
contributors.append(contributor)
```
**Explanation:**
- This part of the code creates an empty list to store contributors. Contributors are stored as
dictionaries, enabling the storage of multiple key-value pairs.

- A loop is employed to gather a specific number of contributors. Dictionaries allow key-value
pairs, facilitating access to specific properties like "name" or "commits". The list enables
dynamic and flexible storage and iteration of contributors.


## Issues Tracking:

```
issues = []
issue_ids = set()
```
```
for i in range(5):
issue_id = input("Enter issue ID: ")
```
```
while issue_id in issue_ids:
issue_id = input("Duplicate ID! Enter a new issue ID: ")
```
```
issue_ids.add(issue_id)
```
```
issue = {
"id": issue_id,
"type": input("Enter type (Bug/Feature): "),
"priority": input("Enter priority: "),
"status": input("Enter status: "),
"reporter": input("Enter reporter name: ")
}
```
```
issues.append(issue)
```
**Explanation:**
- Issues are stored in a list, and the set is used to ensure unique issue IDs. The set has an
average time complexity of O(1) for checking membership, which is perfect for checking for
duplicates.

- The while loop guarantees uniqueness of issue ID, ensuring data integrity. Issues are also
stored in dictionaries, like contributors, to represent properties such as type, priority and
status.


## Frequency Analysis of Issues:

```
priority_count = {}
```
```
for issue in issues:
priority = issue["priority"]
priority_count[priority] = priority_count.get(priority, 0) + 1
```
**Explanation:**
- The .get() method is used here to count the issues, and it returns a default value if the key is
not found. This eliminates the need for extra checks.

## Grouping Issues by Status:

```
status_group = {}
```
```
for issue in issues:
status = issue["status"]
if status not in status_group:
status_group[status] = []
status_group[status].append(issue)
```
**Explanation:**

- The keys are the status (e.g. Open, In Progress) and the values are the issues in the status.

## Set Operations:

```
reporters = set(issue["reporter"] for issue in issues)
contributors_names = set(c["name"] for c in contributors)
```
```
common_users = reporters.intersection(contributors_names)
```
**Explanation:**

- This section uses set operations to explore the relationship between contributors and
reporters.

- Set comprehension is applied to get distinct names from each set. Intersection yields common
users.

## File I/O:

```
import os
```
```
folder = "open_track"
os.makedirs(folder, exist_ok=True)
```
```
with open(f"{folder}/project_report.txt", "w") as file:
file.write("Project Report\n")
file.write(str(contributors))
```
**Explanation:**
- The os.makedirs() method facilitates folder creation if it doesn't already exist.
- It writes contributor data to a text file for storage. File handling allows for data persistence outside of the program's execution, which is crucial for practical applications.

## CSV Export:

```
with open(f"{folder}/issues.csv", "w") as file:
file.write("ID,Type,Priority,Status,Reporter\n")
for issue in issues:
```
```
file.write(f"{issue['id']},{issue['type']},{issue['priority']},{issue['status']},{issue['reporter']}
\n")
```
**Explanation:**
- This part writes issues to a CSV file. CSV (comma-separated values) is a common format for
tabular data, which can be imported into spreadsheet programs.
- Issues are written in a row, maintaining a consistent format. 

## Peiority Issue Detection:

```
urgent = [i for i in issues if i["priority"] in ["Critical", "High"]]
```
**Explanation:**

- Displays issues based on priority using list comprehension.

## Bonus Feature: Append Urgent Issues:

```
with open(f"{folder}/project_report.txt", "a") as file:
file.write("\nUrgent Issues:\n")
for issue in urgent:
file.write(str(issue) + "\n")
```
**Explanation:**
- The "a" in the open mode indicates that the data is appended. This makes the report more user-friendly by drawing attention to urgent items, allowing users to quickly identify them.


