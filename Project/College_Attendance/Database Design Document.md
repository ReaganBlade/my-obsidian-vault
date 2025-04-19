### **1. Introduction**

This document outlines the database design for the Face Recognition Attendance System. The system maintains two categories of users:
- **Admins**: Faculty or system maintainers who manage student data, create batches, and verify attendance.
- **Students**: Individuals whose attendance is captured via face recognition.

The database design is divided into two main logical databases
- **StudentDB**: Contains collections related to student information and attendance.
- **AdminDB**: Contains collections for admin users, logs, and course-related data.

---

## **2. StudentDB**

### **2.1 Users Collection**

**Purpose:**  
Stores profile and academic information of all students.

**Fields:**

- `enrollment_number` (String, Unique)
- `name` (String)
- `branch` (String)
- `year_of_study` (Number)
- `batch_id` (String, Reference to Batches Collection)
- `personal_details` (Object)
    - `email` (String)
    - `phone` (String)
    - `address` (String, Optional)
- `profile_image_url` (String, URL to student image used for facial recognition)

---

### **2.2 AttendanceRecords Collection**

**Purpose:**  
Stores individual attendance records for each student based on face recognition.

**Fields:**

- `attendance_id` (String, Unique)
- `enrollment_number` (String, Reference to Users Collection)
- `batch_id` (String, Reference to Batches Collection)
- `course_id` (String, Reference to Courses Collection)
- `date` (Date)
- `status` (String, e.g., "present", "absent")
- `timestamp` (DateTime)
- `verified_by` (String, Reference to Admins Collection)

---

### **2.3 Batches Collection**

**Purpose:**  
Defines and manages class or batch groupings to which students are assigned.

**Fields:**

- `batch_id` (String, Unique)
- `batch_name` (String)
- `course_id` (String, Reference to Courses Collection)
- `year_of_study` (Number)
- `branch` (String)
- `assigned_faculty` (String, Reference to Admins Collection)
- `schedule` (Object)
    - `days` (Array of Strings)
    - `time` (String)
- `location` (String)

---

## **3. AdminDB**

### **3.1 Admins Collection**

**Purpose:**  
Stores details of all administrative users (faculty and super administrators).

**Fields:**
- `admin_id` (String, Unique)
- `name` (String)
- `email` (String)
- `phone` (String)
- `role` (String, e.g., "faculty", "superadmin")
- `assigned_batches` (Array of Strings, batch_ids)

---

### **3.2 Courses Collection**

**Purpose:**  
Contains metadata for all academic courses managed in the system.

**Fields:**

- `course_id` (String, Unique)
- `course_name` (String)
- `subject_code` (String)
- `description` (String)
- `semester` (Number)
- `branch` (String)

---

### **3.3 Logs Collection**

**Purpose:**  
Captures and audits actions performed by admin users for accountability.

**Fields:**

- `log_id` (String, Unique)
- `admin_id` (String, Reference to Admins Collection)
- `action` (String)
- `target` (String, could be a batch_id or enrollment_number)
- `timestamp` (DateTime)
- `details` (Object with contextual information, e.g., number of students marked present)

---

## **4. Summary Table**

|Database|Collection|Description|
|---|---|---|
|StudentDB|Users|Stores student profiles and academic data|
|StudentDB|AttendanceRecords|Stores attendance entries|
|StudentDB|Batches|Manages student groupings|
|AdminDB|Admins|Admin and faculty user data|
|AdminDB|Courses|Information on academic courses|
|AdminDB|Logs|Audit trail of admin activities|
