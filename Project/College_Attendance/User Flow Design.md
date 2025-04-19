## **1. User Authentication**

### 1.1 Authentication Options
- **OAuth Integration** (e.g., Google Sign-In)
- **Custom Email/Password Login**

### 1.2 Flow
- **New User**
    - Redirect to **Registration Page**
    - Collect basic profile data and image (for face recognition)
    - Save details in `Users` collection
    
- **Returning User**
    - Redirect to **Login Page**
    - Authenticate credentials using OAuth or custom method
---

## **2. Class Selection**
### 2.1 List of Available Classes

- Once authenticated, fetch the list of `Batches` or `Classes` assigned to the student
- Display basic details:
    - Course Name
    - Batch Name
    - Timings
    - Location
### 2.2 Class/Batch Selection

- User selects the appropriate batch from the displayed list
- Redirects to attendance interface

---

## **3. Attendance Marking**

### 3.1 Attendance Interface

- Display:
    - Class details
    - “Mark My Attendance” button

### 3.2 Attendance Submission Steps

1. User clicks **“Mark My Attendance”**
2. App activates the camera
3. User captures an image
4. User confirms and submits the image

---
## **4. Server Processing**

### 4.1 Data Sent to Backend

- **Image**
- **GPS Location**
- **Timestamp**
- **enrollment_number**
- **Selected batch_id**

### 4.2 Facial Verification

- Server uses **Machine Learning (e.g., DeepFace, FaceNet)** to verify:
    - If the captured face matches the stored image in the `Users` collection

### 4.3 Attendance Recording

- If matched:
    - Create an entry in `AttendanceRecords`
    - Status: `"present"`
    - Log the timestamp, location, and admin verifier (if applicable)
    
- If mismatch:
    - Return error: "Face verification failed"
    - User is prompted to retry or report the issue

---
## **5. Admin View (Parallel Flow)**

- Admins can:
    - View live attendance records
    - Manually verify flagged entries
    - Access reports per class, date, and student
