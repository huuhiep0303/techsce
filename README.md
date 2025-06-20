# Face Recognition Attendance System

## Project Overview

This project is an automated attendance system using face recognition. It features a PyQt5-based GUI, stores attendance data in Excel files, and can send SMS notifications to parents via Twilio if a student is absent.

## Directory Structure

```
README.md
CODE/
    Code_Main_NOFINAL.py
    FINAL_CODE.py
    TEST.py
    UpdateQT.py
    sms.py
    requirements.txt
    dlib-19.24.1-cp311-cp311-win_amd64.whl
    dlib-19.24.99-cp312-cp312-win_amd64.whl
DATA/
    <student face images>
EXCEL/
    Danh sách điểm danh lớp 10A.xlsx
    Danh sách điểm danh lớp 10B.xlsx
    parent_phonenumbers.xlsx
FILE_UI/
    Diemdanh_UI.ui
OTHERS/
    CODE.txt
    requirements.txt
```

## Requirements

- Python 3.11 or 3.12
- See [`CODE/requirements.txt`](CODE/requirements.txt) for required Python packages
- Dlib: install the appropriate `.whl` file for your Python version

### Install Dependencies

```sh
pip install -r CODE/requirements.txt
pip install CODE/dlib-19.24.1-cp311-cp311-win_amd64.whl  # or the correct dlib wheel for your Python version
```

## Usage

1. **Prepare Data**
   - Add student face images to the [`DATA/`](DATA/) folder. The file name should be the student's name.
   - Update the class attendance Excel files in [`EXCEL/`](EXCEL/).
   - Update [`parent_phonenumbers.xlsx`](EXCEL/parent_phonenumbers.xlsx) with student names and parent phone numbers.

2. **Run the Application**
   - Start the main GUI application:
     ```sh
     python CODE/FINAL_CODE.py
     ```
   - You can also use [`CODE/TEST.py`](CODE/TEST.py) or [`CODE/UpdateQT.py`](CODE/UpdateQT.py) for testing or development.

3. **Using the GUI**
   - Select the Excel attendance file.
   - Choose the attendance date.
   - Start the camera to recognize faces.
   - View lists of present and absent students.
   - Send SMS notifications to parents of absent students.

## SMS Notification Setup (Twilio)

- Register a Twilio account and obtain your `account_sid`, `auth_token`, and `twilio_number`.
- Update these credentials in the `send_sms_twilio` function in the source code.

## Contact

- Author: Hiep Cao Huu
- Email: cacaohh04@gmail.com
