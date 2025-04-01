### **What is Session-Based Authentication?**

Session-Based Authentication is a method where a server creates a session for an authenticated user and stores session information on the server. The client stores a session identifier (usually in a cookie) and sends it with each request to maintain authentication.

### **How Does It Work?**

1. **User Login:** The user submits their credentials (username and password).
2. **Authentication:** The server verifies credentials and, if valid, creates a session.
3. **Session Storage:** The server generates a session ID and stores it in memory or a database.
4. **Session Cookie:** The client stores the session ID in a cookie and sends it with each request.
5. **Request Handling:** The server validates the session ID on each request to maintain authentication.
6. **Session Expiry:** The session is destroyed after a predefined time or when the user logs out.

### **Advantages of Session-Based Authentication**

- Secure (when implemented correctly with HTTPS and proper session handling)
- Easier to implement in server-side applications
- Allows for more control over session expiration and revocation

### **Disadvantages**

- Less scalable than token-based authentication, as sessions require server-side storage
- Requires session management to handle expiration and cleanup

### **Implementation in TypeScript (Express.js)**

Below is an example of how to implement session-based authentication in a Node.js application using Express and Express-Session.

```typescript
import express from 'express';
import session from 'express-session';
import bodyParser from 'body-parser';

const app = express();
app.use(bodyParser.json());

app.use(session({
    secret: 'your_secret_key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false } // Set secure: true in production
}));

// Dummy user
const user = { username: 'testUser', password: 'password123' };

// Login Route
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (username === user.username && password === user.password) {
        req.session.user = username;
        res.json({ message: 'Login successful' });
    } else {
        res.status(401).json({ message: 'Invalid credentials' });
    }
});

// Protected Route
app.get('/dashboard', (req, res) => {
    if (req.session.user) {
        res.json({ message: `Welcome ${req.session.user}` });
    } else {
        res.status(401).json({ message: 'Unauthorized' });
    }
});

// Logout Route
app.post('/logout', (req, res) => {
    req.session.destroy(err => {
        if (err) {
            return res.status(500).json({ message: 'Logout failed' });
        }
        res.json({ message: 'Logout successful' });
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

### **Explanation of Code:**

1. **Session Middleware:** Uses `express-session` to store session data.
2. **Login Endpoint:** Validates user credentials and creates a session.
3. **Protected Route:** Ensures only authenticated users can access certain endpoints.
4. **Logout Endpoint:** Destroys the session upon logout.

### **Conclusion**

Session-based authentication is a powerful and simple method for maintaining user authentication, especially for traditional server-side applications. However, for modern, scalable applications, token-based authentication is often preferred.