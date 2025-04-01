### **What is Token-Based Authentication?**

Token-Based Authentication is a security mechanism that allows users to authenticate using a unique token instead of traditional username-password combinations. This token grants access to protected resources and is commonly used in modern web applications, APIs, and mobile applications.

### **How Does Token-Based Authentication Work?**

1. **User Login:** The user provides valid credentials (e.g., username and password) to the authentication server.
2. **Token Generation:** If the credentials are valid, the server generates a secure token (e.g., JWT - JSON Web Token).
3. **Token Storage:** The client stores the token (typically in local storage or HTTP cookies).
4. **Token Usage:** For each subsequent request, the client sends the token in the request header.
5. **Token Verification:** The server validates the token before granting access to protected resources.
6. **Token Expiry & Refresh:** Tokens may expire after a set period, requiring re-authentication or token refreshing.

### **Advantages of Token-Based Authentication**

- **Stateless Authentication:** No need for session storage on the server.
- **Scalability:** Works well in distributed systems.
- **Improved Security:** Tokens are encrypted and can be set to expire.
- **Cross-Platform Compatibility:** Used in web, mobile, and API authentication.

### **Types of Token-Based Authentication**

1. **JWT (JSON Web Token)** – Compact, self-contained tokens signed and optionally encrypted.
2. **OAuth Tokens** – Used for third-party authentication (e.g., logging in via Google, Facebook, GitHub).
3. **API Keys** – Unique keys assigned to applications for API access.

### **Implementation in TypeScript (Node.js) Using JWT**

Below is a basic implementation of Token-Based Authentication using JWT in a Node.js (Express) application.

```typescript
import express from 'express';
import jwt from 'jsonwebtoken';
import bodyParser from 'body-parser';

const app = express();
const PORT = 3000;
const SECRET_KEY = "your_secret_key";

app.use(bodyParser.json());

// Mock user data
const users = [{ id: 1, username: "user", password: "password" }];

// Login Route
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);
    
    if (!user) {
        return res.status(401).json({ message: "Invalid credentials" });
    }
    
    const token = jwt.sign({ userId: user.id }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token });
});

// Protected Route
app.get('/protected', (req, res) => {
    const token = req.headers['authorization'];
    
    if (!token) {
        return res.status(403).json({ message: "No token provided" });
    }
    
    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) {
            return res.status(401).json({ message: "Invalid token" });
        }
        res.json({ message: "Access granted", userId: decoded.userId });
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
```

### **Explanation of Code:**

1. **Login Endpoint (`/login`)**
    - Validates user credentials.
    - Generates a JWT token if authentication is successful.
    - Sends the token to the client.
2. **Protected Route (`/protected`)**
    - Checks for a token in the request headers.
    - Verifies the token and grants access if valid.

### **Conclusion**

Token-Based Authentication is an efficient and secure method for user authentication, especially for APIs and modern web applications. Using JWT, it ensures stateless authentication and improved security.