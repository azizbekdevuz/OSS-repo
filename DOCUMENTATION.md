# documentation

## Overview

This repository contains the Week 5 Open Source Software assignment notebook:

- `22013143_OSS_Task_5.ipynb`

The notebook is a single interactive Python program that simulates basic open-source project management tasks. It collects project information, contributor details, and issue records, then performs data processing and file handling operations.

## Assignment Scope

The notebook demonstrates practical use of:

- strings
- tuples
- lists
- dictionaries
- sets
- loops
- conditionals
- file and folder creation
- file writing, reading, and appending
- basic error handling with `try/except`

## Notebook Structure

### 1. Title cell
The first cell is a markdown heading containing:

- course title
- student ID and name
- task number
- week assignment label

### 2. Main code cell
The second cell contains the full implementation in one code cell.

It is divided into these parts:

- **Section 1**: project information and contributors
- **Section 2**: issue tracking and analysis
- **Section 3**: folder creation and file operations
- **Bonus**: urgent issue extraction and append
- **Final Summary**: printed completion summary

## Program Flow

### Section 1 — Project information
The program asks the user to enter:

- project name
- project version
- year started
- main language
- project lead name

These values are stored in a tuple called `project`.

The program then prints selected tuple values and slices to demonstrate tuple usage.

### Contributor collection
The program collects data for **4 contributors**.  
For each contributor, it asks for:

- name
- role
- language
- commits
- country

Each contributor is stored as a dictionary and added to a contributors list.

After collection, the program:

- extracts contributor names into a list
- sorts the names
- adds a default `status: Active`
- creates a backup copy of the first contributor

## Section 2 — Issue tracking
The program collects data for **5 issues**.  
For each issue, it asks for:

- issue id
- title
- type
- priority
- reporter
- status

Each issue is stored as a dictionary and added to an issues list.

After that, the program performs several operations:

- counts issues whose status is exactly `Open`
- updates the first issue priority to `Critical`
- prints the last two issues
- builds a set of reporters
- builds a set of contributor languages as a tech stack
- adds `Git` to the tech stack
- demonstrates set union, intersection, and difference
- checks whether `Critical` exists in the priority set
- creates a priority frequency dictionary
- groups issue titles by status
- counts how many issues each reporter submitted
- finds the top reporter
- removes the `type` field from the first issue with `pop()`

## Section 3 — File and folder handling

The notebook creates a folder from the project name:

- lowercase
- spaces replaced with underscores

Example:
- `Fishlinic` → `fishlinic/`

Inside that folder, the program creates:

- `project_report.txt`
- `issues.csv`

### `project_report.txt`
This text report includes:

- project details
- contributor list
- issue list
- analysis summary

### `issues.csv`
This CSV file contains:

- id
- title
- priority
- reporter
- status

## File reading operations

After writing the files, the notebook demonstrates:

- `read()` to print the full report
- `readline()` to print the first two lines
- `readlines()` to load all lines and filter important ones

It then checks lines containing `Critical` or `High`.

## Bonus section

The notebook creates an `urgent` list containing issue titles with priority exactly:

- `Critical`
- `High`

It appends an `URGENT ISSUES` section to `project_report.txt` and prints the last part of the file to confirm the append worked.

## Final output

At the end, the notebook prints a final summary including:

- project name
- version
- lead
- contributor count
- sorted contributor names
- tech stack
- issue count
- open issue count
- reporters
- top reporter
- priority breakdown
- generated file paths

## Requirements

- Python 3.x
- Jupyter Notebook or Google Colab
- standard library only (`os` is used)

No external packages are required.

## How to run

### Option 1 — Jupyter Notebook
Open:

`22013143_OSS_Task_5.ipynb`

Then run all cells and provide the requested input values.

### Option 2 — Google Colab
Upload the notebook to Colab and run the cells there.

## Generated Output Example

If the user enters a project name like `Fishlinic`, the notebook will create:

```text
fishlinic/
├── project_report.txt
└── issues.csv
