### **What is Authentication?**

Authentication is the process of verifying someone’s identity.

**Real-World Example:** When boarding a plane, an airline worker checks your passport to verify your identity. This is authentication.

**Computers Example:** When logging into a website, you authenticate yourself using a username and password, which the website verifies.

#### **Key Points:**

- Authentication is not limited to persons.
- Username and password are not the only authentication methods.

**Other Examples:**

- Websites using HTTPS rely on TLS to authenticate the server.
- Server-to-server communication may require authentication to prevent malicious usage.

### **How Authentication Works**

Authentication is based on three main factors:

1. **Knowledge Factor (Something You Know)**
    - Username and Password
    - Security Codes, PIN Codes, or Security Questions (e.g., ATM PIN)
    
2. **Possession Factor (Something You Have)**
    - Hard Tokens (Physical authentication devices)
    - Soft Tokens (OTP sent to a device used for setup)
    
3. **Inherence Factor (Something You Are)**
    - Biometric Authentication (Fingerprint, iris scan, face recognition, voice recognition)

### **[[Multi-Factor Authentication]] (MFA)**
MFA requires using more than one authentication factor.

**Example:**
- Username/Password (Knowledge Factor) + OTP (Possession Factor)
- Since multiple factors are involved, MFA is more secure than single-factor authentication.

**Important Note:**
- The factors must be different for true MFA (e.g., username/password + security question is not MFA as both belong to the Knowledge Factor).

### **[[Two-Factor Authentication]] (2FA)**
2FA is a subset of MFA where exactly two authentication factors are used.

**Example:**
- Password (Knowledge Factor) + OTP (Possession Factor)
- 2FA is always MFA, but MFA is not always 2FA (as MFA can include more than two factors).

### **Authentication vs. Authorization**

|Concept|Definition|
|---|---|
|**Authentication**|Verifying identity (e.g., login with username and password).|
|**Authorization**|Checking permissions (e.g., determining if a user can access certain features).|

**HTTP Status Codes:**
- **401 Unauthorized:** Authentication failure (invalid username/password).
- **403 Forbidden:** Authorization failure (user lacks permission to perform an action).

### **Common Authentication Strategies**
1. **Basic Authentication** – Uses username and password in the request header.
2. **Session-Based Authentication** – Creates a session for the user on the server.
3. **Token-Based Authentication** – Uses tokens instead of sessions (e.g., API tokens).
4. **JWT Authentication** – Uses JSON Web Tokens for authentication.
5. **OAuth (Open Authorization)** – Allows third-party authentication without sharing credentials.
6. **Single Sign-On (SSO)** – Enables users to log in once and access multiple applications.

These notes summarize authentication, its methods, MFA, 2FA, and the difference between authentication and authorization.