# section 1
project_name = "LITA (Language Instructed Temporal Localization)"
project_lead = "Prithwis Das"
version = 3.0
year_started = 2024
main_language = "English"

project_info = (project_name, version, year_started, main_language, project_lead)

print("="*40)
print(project_name)
print(f"Project Lead : {project_info[-1]}")
print("="*40)
print(f"Name : {project_info[0]} | Version : {project_info[1]} | Started : {project_info[2]}")
print(f"First 3 fields : {project_info[:3]}")
print(f"Language count : 1 | Language Index : {project_info.index(main_language)}")
print("-"*40)

contributors = []
for _ in range(4):
    dev_info = {}
    name = input("Enter your name: ")
    role = input("Enter your role: ")
    language = input("Enter your language: ")
    commits = int(input("Number of commits: "))
    country = input("Enter your nationality: ")
    dev_info.update({"name": name, "role": role, "language": language, "commits": commits, "country": country})
    contributors.append(dev_info)

names = []
for dev in contributors:
    names.append(dev.get("name"))
names.sort()
print(f"Sorted Names : {names}")
print(f"Last name: {names[-1]}   First two: {names[:2]}")


for dev in contributors:
    dev.update({"status": "Active"})
print(f"Contributor 1 Status: {contributors[0].get("status")}")

first_contributor = contributors[0].copy()
print(first_contributor)

# section 2
issues = []

# Collect exactly 5 issues
print("="*50)
print("ISSUE TRACKER SYSTEM")
print("="*50)
print("\nEnter details for 5 issues:")
print("-"*50)

for i in range(5):
    print(f"\n--- Issue {i+1} ---")
    issue = {}
    issue["id"] = input(f"Enter issue ID {i+1}: ")
    issue["title"] = input(f"Enter issue title {i+1}: ")
    issue["type"] = input(f"Enter type ({i+1}) [Bug/Feature]: ")
    issue["priority"] = input(f"Enter priority ({i+1}) [Critical/High/Medium/Low]: ")
    issue["reporter"] = input(f"Enter reporter name ({i+1}): ")
    issue["status"] = input(f"Enter status ({i+1}) [Open/In Progress/Resolved]: ")
    issues.append(issue)

print("\n" + "="*50)
print("LIST OPERATIONS")
print("="*50)

# Count 'Open' issues using a loop (no count() method)
open_count = 0
for issue in issues:
    if issue["status"] == "Open":
        open_count += 1
print(f"\nOpen issues\t\t: {open_count}")

# Change the first issue's priority to 'Critical' using index
issues[0]["priority"] = "Critical"
print(f"First issue → priority updated to Critical.")

# Use slicing to print the last two issues
print(f"Last two issues\t\t: {issues[-2:]}")

print("\n" + "="*50)
print("SET OPERATIONS")
print("="*50)

# Build reporters set from issues (using loop)
reporters = set()
for issue in issues:
    reporters.add(issue["reporter"])
print(f"\nreporters\t\t: {reporters}")

# Build tech_stack set from contributors (using loop)
tech_stack = set()
for contributor in contributors:
    tech_stack.add(contributor["language"])
print(f"tech_stack\t\t: {tech_stack}")

# add() one more technology manually
tech_stack.add("Python")

# discard() one that may or may not exist
tech_stack.discard("Rust")

# Create a set of all priorities
priority_set = set()
for issue in issues:
    priority_set.add(issue["priority"])

# union() - combine both sets
combined = reporters.union(tech_stack)
print(f"union\t\t\t: {combined}")

# intersection() - find common items
common = reporters.intersection(tech_stack)
print(f"intersection\t\t: {common}")

# difference() - find reporters not in tech_stack
reporters_only = reporters.difference(tech_stack)
print(f"difference\t\t: {reporters_only}")

# Check if 'Critical' is in the set of all priorities
if "Critical" in priority_set:
    print(f"Critical present\t: YES – flag for immediate review.")
else:
    print(f"Critical present\t: NO")

print("\n" + "="*50)
print("DICTIONARY OPERATIONS")
print("="*50)

# Build priority_count dict by looping (no hardcoding)
priority_count = {}
for issue in issues:
    priority = issue["priority"]
    if priority in priority_count:
        priority_count[priority] += 1
    else:
        priority_count[priority] = 1

# Use keys(), values(), items() at least once when printing
print(f"\npriority_keys\t\t: {priority_count.keys()}")
print(f"priority_values\t\t: {priority_count.values()}")

# Build status_groups dict - each key is status, value is list of titles
status_groups = {}
for issue in issues:
    status = issue["status"]
    title = issue["title"]
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(title)

print(f"Status Groups\t\t: ", end="")
first = True
for status, titles in status_groups.items():
    if not first:
        print(" | ", end="")
    print(f"{status} : {titles}", end="")
    first = False
print()

# Find the top reporter using a loop (no max() or Counter())
reporter_count = {}
for issue in issues:
    reporter = issue["reporter"]
    if reporter in reporter_count:
        reporter_count[reporter] += 1
    else:
        reporter_count[reporter] = 1

top_reporter = None
top_count = 0
for reporter, count in reporter_count.items():
    if count > top_count:
        top_count = count
        top_reporter = reporter

print(f"Top reporter\t\t: {top_reporter} ({top_count} issues)")

# Use pop() to remove 'type' key from first issue
removed_type = issues[0].pop("type")
print(f"After pop('type')\t: {issues[0]}")

print("\n" + "="*50)


# section 3
import os

# Create folder name from project name (lowercase, underscores)
folder_name = project_info[0].lower().replace(" ", "_").replace("(", "").replace(")", "").split()[0]

# Check if folder exists before creating
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder created : {folder_name}/")
else:
    print(f"Folder already exists : {folder_name}/")

# Build project_report.txt content
report_content = f"""{"="*50}
{project_info[0]} – PROJECT REPORT
{"="*50}

PROJECT INFORMATION:
Project Name: {project_info[0]}
Version: {project_info[1]}
Year Started: {project_info[2]}
Main Language: {project_info[3]}
Project Lead: {project_info[4]}

CONTRIBUTORS ({len(contributors)}):
"""

for contributor in contributors:
    report_content += f"  - {contributor['name']} ({contributor['role']}), {contributor['country']}, commits: {contributor['commits']}\n"

report_content += f"\nTECH STACK:\n"
for lang in sorted(tech_stack):
    report_content += f"  - {lang}\n"

report_content += f"\nISSUES SUMMARY ({len(issues)} total):\n"
open_count = 0
for issue in issues:
    if issue["status"] == "Open":
        open_count += 1
    report_content += f"  [{issue['id']}] {issue['title']} | Priority: {issue['priority']} | Status: {issue['status']} | Reporter: {issue['reporter']}\n"

report_content += f"\nOPEN ISSUES: {open_count}\n"

reporter_count = {}
for issue in issues:
    reporter = issue["reporter"]
    if reporter in reporter_count:
        reporter_count[reporter] += 1
    else:
        reporter_count[reporter] = 1

top_reporter = None
top_count = 0
for reporter, count in reporter_count.items():
    if count > top_count:
        top_count = count
        top_reporter = reporter

report_content += f"TOP REPORTER: {top_reporter} ({top_count} issues)\n"

priority_count = {}
for issue in issues:
    priority = issue["priority"]
    if priority in priority_count:
        priority_count[priority] += 1
    else:
        priority_count[priority] = 1

report_content += f"\nPRIORITY BREAKDOWN:\n"
for priority in sorted(priority_count.keys()):
    report_content += f"  {priority}: {priority_count[priority]}\n"

report_content += f"\n{'='*50}\n"

# Save project_report.txt with error handling
try:
    report_path = os.path.join(folder_name, "project_report.txt")
    with open(report_path, "w") as report_file:
        report_file.write(report_content)
except IOError as e:
    print(f"Error writing report file: {e}")

# Build and save issues.csv with error handling
try:
    csv_path = os.path.join(folder_name, "issues.csv")
    with open(csv_path, "w") as csv_file:
        csv_file.write("id,title,priority,reporter,status\n")
        for issue in issues:
            csv_file.write(f"{issue['id']},{issue['title']},{issue['priority']},{issue['reporter']},{issue['status']}\n")
except IOError as e:
    print(f"Error writing CSV file: {e}")

# Print folder contents
files_saved = os.listdir(folder_name)
print(f"Files saved : {sorted(files_saved)}")

print("\n" + "="*50)
print("--- read() ---")
print("="*50)

# read() - print full file content
try:
    with open(report_path, "r") as report_file:
        full_content = report_file.read()
        print(full_content)
except FileNotFoundError as e:
    print(f"Error reading report file: {e}")

print("\n" + "="*50)
print("--- readline() ---")
print("="*50)

# readline() - print first two lines only
try:
    with open(report_path, "r") as report_file:
        line1 = report_file.readline().strip()
        line2 = report_file.readline().strip()
        print(f"Line 1 : {line1}")
        print(f"Line 2 : {line2}")
except FileNotFoundError as e:
    print(f"Error reading report file: {e}")

print("\n" + "="*50)
print("--- readlines() ---")
print("="*50)

# readlines() - count total lines and print lines containing 'Critical' or 'High'
try:
    with open(report_path, "r") as report_file:
        all_lines = report_file.readlines()
        total_lines = len(all_lines)
        critical_high_lines = [line.strip() for line in all_lines if "Critical" in line or "High" in line]
        critical_high_count = len(critical_high_lines)
        print(f"Total lines : {total_lines}\t\tCritical/High lines : {critical_high_count}")
        for line in critical_high_lines:
            print(line)
except FileNotFoundError as e:
    print(f"Error reading report file: {e}")

print("\n" + "="*50)
print(f"{project_info[0]} – FINAL SUMMARY")
print("="*50)

# Build sorted names list
sorted_names = []
for dev in contributors:
    sorted_names.append(dev["name"])
sorted_names.sort()

# Count priorities
priority_breakdown = {}
for issue in issues:
    priority = issue["priority"]
    if priority in priority_breakdown:
        priority_breakdown[priority] += 1
    else:
        priority_breakdown[priority] = 1

# Final summary using only f-strings
print(f"Project : {project_info[0]}\t\tVersion : {project_info[1]}\t\tLead : {project_info[4]}")
print(f"Contributors : {len(contributors)}\t\tNames : {sorted_names}")
print(f"Tech Stack : {tech_stack}")
print(f"Issues : {len(issues)}\t\tOpen : {open_count}\t\tReporters : {len(reporters)}")
print(f"Top Reporter : {top_reporter} ({top_count} issues)")

priority_summary = ""
for priority in sorted(priority_breakdown.keys()):
    if priority_summary:
        priority_summary += f"  {priority}:{priority_breakdown[priority]}"
    else:
        priority_summary += f"{priority}:{priority_breakdown[priority]}"

print(f"{priority_summary}")
print(f"Report : {report_path}")
print(f"CSV\t : {csv_path}")
print("="*50)
print(f"{project_info[0]} complete. Thank you for contributing to open source!")


# challenge section
print("="*50)
print("CHALLENGE SECTION")
print("="*50)

# Part 1: List comprehension - build urgent list with titles of Critical or High priority issues
urgent = [issue['title'] for issue in issues if issue['priority'] in ['Critical', 'High']]

print(f"\nPart 1: List Comprehension")
print(f"Urgent Issues: {urgent}")
print(f"Length: {len(urgent)}")

# Part 2: Append urgent issues section to project_report.txt
urgent_section = f"\n{'='*50}\nURGENT ISSUES:\n{'='*50}\n"
for title in urgent:
    urgent_section += f"  • {title}\n"

try:
    with open(report_path, 'a') as report_file:
        report_file.write(urgent_section)
except IOError as e:
    print(f"Error appending to report file: {e}")

# Read last 6 lines to confirm append worked
print(f"\nPart 2: Append Mode & Confirmation")
try:
    with open(report_path, 'r') as report_file:
        all_lines = report_file.readlines()
        last_six = all_lines[-6:]
        print(f"Last 6 lines of {report_path}:")
        for line in last_six:
            print(line.rstrip())
except FileNotFoundError as e:
    print(f"Error reading report file: {e}")

print("\n" + "="*50)
