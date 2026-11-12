# Smart File Organizer & Automation Tool

A Python-based file organization application that automatically scans, categorizes, and organizes files into dedicated folders. Built using Object-Oriented Programming (OOP), this tool provides safe preview functionality, duplicate filename protection, logging, and automated summary reports.

## Project Overview

Managing files manually can be time-consuming, especially when a folder contains different types of files.

The **Smart File Organizer & Automation Tool** solves this problem by automatically identifying file extensions and organizing files into appropriate categories.

Users can preview the planned file movements before performing the actual organization.

## Features

- **Automatic File Scanning:** Scans files inside a user-provided directory using Python's `os` module.
- **File Categorization:** Automatically identifies file types and organizes them into five categories.
- **Automatic Folder Creation:** Creates category folders when they do not already exist.
- **Preview Mode:** Displays planned file movements without modifying or moving files.
- **Duplicate Filename Protection:** Prevents overwriting existing files by generating unique filenames.
- **Logging System:** Records successful file movements, organization activities, and errors.
- **Summary Report:** Generates a timestamped text report containing file counts and movement details.
- **Input Validation:** Handles invalid paths, empty paths, and file paths instead of directories.
- **Error Handling:** Handles file operation errors using exception handling.

## File Categories

| Category | Supported Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png` |
| Documents | `.pdf`, `.docx`, `.txt` |
| Videos | `.mp4`, `.mkv` |
| Python Files | `.py` |
| Others | All remaining file extensions |

## Project Structure

```text
Smart_File_Organizer_And_Automation_Tool/
│
├── app.py
├── file_organizer.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── 01_Preview_Mode.png
    ├── 02_File_Organization_Report.png
    ├── 03_Duplicate_Preview.png
    ├── 04_Duplicate_Organization_Report.png
    └── 05_Duplicate_File_Verification.png
```

**Note:**
- The `venv/` directory is excluded from GitHub.
- Local testing folders are excluded from GitHub.
- The `logs/` and `reports/` directories are generated automatically when the application runs.
- Generated log files and summary reports are excluded from version control.


## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- os module
- shutil module
- logging module
- datetime module
- Exception Handling

No external Python packages are required. The project uses Python's built-in standard library.

## Installation

### 1. Clone the Repository

```bash
git clone git clone https://github.com/Sifatuzzahan/Smart-File-Organizer-And-Automation-Tool.git
```

### 2. Navigate to the Project Directory

```bash
cd Smart_File_Organizer_And_Automation_Tool
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Run the Application

```bash
python app.py
```

## How to Use

### Step 1: Enter a Folder Path

When the application starts, enter the path of the directory you want to organize.

Example:

```text
C:\Users\YourName\Downloads
```

### Step 2: Select an Operation

The application provides two options:

```text
Select Operation:
1. Preview Mode
2. Organize Files
```

**Option 1: Preview Mode**

Displays the planned file movements without moving any files.

Example:

```text
========== PREVIEW MODE ==========
No files will be moved.

[PREVIEW] photo.jpg -> Images/photo.jpg
[PREVIEW] report.pdf -> Documents/report.pdf

PREVIEW COMPLETED
```

**Option 2: Organize Files**

Moves files into their respective category folders after user confirmation.

The application asks:

```text
Are you sure you want to move the files? (yes/no):
```

Enter `yes` to proceed.

## Duplicate Filename Handling

The application prevents existing files from being overwritten.

If a destination file already exists, the program automatically generates a unique filename.

Example:

```text
Existing:
sample.txt
sample_1.txt

New incoming file:
sample.txt

Generated filename:
sample_2.txt
```

The same logic handles multiple filename conflicts by checking for an available filename before moving the file.

## Logging System

All important organization activities are recorded in:

```text
logs/organizer.log
```

The log records:

- Organization start and completion.
- Successful file movements.
- Source and destination paths.
- Empty folder detection.
- File movement errors.
- Summary report generation.

## Summary Report

After an organization operation, the application generates a timestamped report inside the `reports/` directory.

Example:

```text
reports/
    summary_report_2026-11-12_07-03-14_012256.txt
```

The report includes:

- Report generation date and time.
- Selected folder path.
- Total files moved.
- Category-wise file counts.
- Total categorized files.
- Names of successfully moved files.

## Object-Oriented Programming

The project uses a class named `FileOrganizer`, implemented in `file_organizer.py`.

Its responsibilities are divided into separate methods:

| Method | Responsibility |
|---|---|
| `__init__()` | Validates the folder path and initializes logging. |
| `scan_files()` | Scans and categorizes files. |
| `create_category_folders()` | Creates category directories. |
| `get_unique_destination()` | Generates unique filenames to prevent overwriting. |
| `move_files()` | Handles preview and actual file movement. |
| `generate_summary_report()` | Generates the final organization report. |

The `app.py` file serves as the main entry point and handles user interaction.

## Safe Testing Instructions

Before organizing important personal files, test the application using a separate test directory containing sample files.

Recommended testing scenarios:

1. Test with different file extensions.
2. Test with an empty directory.
3. Test with an invalid directory path.
4. Test with a file path instead of a directory.
5. Test duplicate filenames.
6. Verify Preview Mode does not move files.
7. Verify actual file movement.
8. Check the generated summary report.
9. Verify the logging system.

**Important:** Always use a dedicated test folder first. Actual organization moves files from their original locations, and the application does not provide an automatic undo feature.

## Author

**Developed by: Sifatuzzahan**

Python Project | Smart File Organizer & Automation Tool

---

*This project was developed as part of a Python programming assignment to demonstrate Object-Oriented Programming, file handling, automation, logging, exception handling, and practical problem-solving.*
