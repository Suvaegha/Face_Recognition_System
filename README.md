# Face Recognition Attendance System

The Face Recognition Attendance System is a web-based application developed using Django and Python, designed to streamline the process of employee attendance management through facial recognition technology.

## Project Description

Facial recognition systems are powerful tools for identifying individuals from digital images or video frames. This project aims to leverage this technology to automate the attendance tracking process in organizations. The system will allow administrators to register employees, capture their facial images, and subsequently record their attendance using facial recognition. The project includes features such as user authentication, employee registration, attendance tracking, leave management, and detailed reporting.

## Features
- **Facial Recognition:** Utilizes advanced facial recognition algorithms to accurately identify individuals and record their attendance.
- **User Authentication:** Secure login system for administrators and users, ensuring access control and data privacy.
- **Attendance Management:** Allows administrators to view, download, and manage attendance records efficiently.
- **Real-time Updates:** Provides real-time updates on attendance status, including notifications for late arrivals and absentees.


## Module 1: Admin Panel

### Task 1: Admin Login & Dashboard
- Implemented a secure login system for administrators.
- Developed a dashboard displaying key metrics such as present count, absent count, and total registered employees for the current day.
- Integrated functionality to view and manage leave requests.

### Task 2: Employee List & Leave Report
- Implemented features to display a list of registered employees and their details.
- Enabled administrators to update employee information and delete employee entries.
- Implemented a leave report functionality to display leave requests for the current month.

### Task 3: Attendance Report
- Developed functionality to generate daily and monthly attendance reports.
- Implemented a filter system to search for attendance records within specific date ranges.
- Utilized efficient rendering techniques to display data without page reloads.

## Module 2: Employee Panel

### Task 1: Employee Dashboard & Leave Requests
- Designed a user-friendly dashboard for employees to view their attendance statistics.
- Implemented features to display leave requests and their status.
- Integrated functionality to allow employees to submit leave requests.

### Task 2: Attendance Capture
- Developed a feature for employees to capture their attendance using facial recognition.
- Implemented a JavaScript popup to access the camera and capture employee photos.
- Integrated image comparison functionality to validate attendance and record check-in/check-out times.

## Technologies Used
- **Django**: Python web framework for backend development.
- **Face-Recognition:**: Library for facial recognition.
- **JavaScript**: Frontend scripting language for interactive features.
- **HTML/CSS**(Very Basic): Frontend markup and styling for user interface.
- **PostgreSQL**: Database management systems for storing employee data and attendance records.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arunnasarain/face_recognition_system.git
2. [face-recognition](https://pypi.org/project/face-recognition/) package supports only python3.8 and python3.9. Change directory ```cd face_recognition_system``` and [setup virtual environment](#setting-up-virtual-environment-for-python-39).
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run migrations:
   ```bash
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver
6. Access the application at http://localhost:8000  in your web browser.


## Usage
- Log in as an administrator to access the admin panel.
- Register employees and manage their details. Capture employee attendance using facial recognition.
- View attendance reports and leave requests.
Log in as an employee to view personal attendance statistics and submit leave requests.


## Setting up Virtual Environment for Python 3.9
1. Install Python 3.9:

   - Download and install Python 3.9 from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Create a Virtual Environment:

   - Open a terminal or command prompt.
   - Navigate to the directory where you want to create the virtual environment.
   - Run the following command to create a virtual environment named venv for Python 3.9:
      ```bash
      python3.9 -m venv .venv
3. Activate the Virtual Environment:

   - On macOS/Linux:
      ```bash
      source .venv/bin/activate
   - On Windows:
      ```bash
      .venv\Scripts\activate
4. Verify Python Version:

   - After activating the virtual environment, verify that Python 3.9 is being used by running:
      ```bash
      python --version
## Troubleshooting Face Recognition Installation
If you encounter issues installing the face-recognition library, follow these steps to troubleshoot:

1. Install Xcode Command Line Tools:
   ```bash
   xcode-select --install
2. Install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3. Install Prerequisites:

   ```bash
   brew install cmake
   brew install boost
   brew install boost-python
   brew install dlib
4. Retry Installation:
   ```bash
   pip install dlib
5. Verify Installation:

   ```bash
   pip list | grep dlib

By following these steps, you should be able to resolve any installation issues related to the face-recognition library on macOS.
"# Face_Recognition_System" 
