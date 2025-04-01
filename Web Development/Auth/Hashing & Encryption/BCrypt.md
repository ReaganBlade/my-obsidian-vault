### **What is BCrypt?**

BCrypt is a password hashing function designed to securely store passwords. It incorporates a salt to protect against rainbow table attacks and uses a work factor to make brute-force attacks computationally expensive.

### **How BCrypt Works?**

1. **Salting:** A unique random salt is generated for each password before hashing.
    
2. **Hashing:** The password and salt are combined and hashed using the Blowfish cipher.
    
3. **Work Factor (Cost Parameter):** Controls the computational complexity, making it harder to brute-force.
    
4. **Verification:** When a user logs in, the provided password is hashed with the stored salt and compared to the stored hash.
    

### **Why Use BCrypt?**

- **Adaptive Work Factor:** Increases computation time as hardware gets faster.
    
- **Automatic Salting:** Prevents precomputed attacks.
    
- **Secure Against Brute-Force Attacks:** Due to its computational complexity.
    

### **Implementation in TypeScript**

```typescript
import bcrypt from 'bcrypt';

const saltRounds = 10;

// Function to hash a password
const hashPassword = async (password: string): Promise<string> => {
    const salt = await bcrypt.genSalt(saltRounds);
    const hashedPassword = await bcrypt.hash(password, salt);
    return hashedPassword;
};

// Function to verify a password
const verifyPassword = async (password: string, hash: string): Promise<boolean> => {
    return await bcrypt.compare(password, hash);
};

// Example Usage
(async () => {
    const password = "securePassword123";
    const hashed = await hashPassword(password);
    console.log("Hashed Password:", hashed);
    
    const isMatch = await verifyPassword("securePassword123", hashed);
    console.log("Password Match:", isMatch);
})();
```

### **Conclusion**

BCrypt is one of the most secure password hashing algorithms due to its built-in salting mechanism and adaptive work factor. It is widely used in authentication systems to ensure password security and protect against brute-force attacks.