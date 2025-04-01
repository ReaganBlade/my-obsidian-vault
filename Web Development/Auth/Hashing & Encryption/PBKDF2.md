### **What is PBKDF2?**

PBKDF2 (Password-Based Key Derivation Function 2) is a key derivation function that applies a cryptographic hash function multiple times to a password and a salt to produce a strong key. It is widely used for password hashing and encryption key derivation.

### **How PBKDF2 Works?**

1. **Salt Generation:** A unique random salt is generated for each password to prevent precomputed attacks like rainbow tables.
    
2. **Multiple Iterations:** The password and salt are repeatedly hashed using a cryptographic function (e.g., SHA-256).
    
3. **Key Stretching:** Repeating the hashing process makes brute-force attacks more time-consuming.
    
4. **Final Key Generation:** The derived key is stored and used for password verification.
    

### **Why Use PBKDF2?**

- **Resistant to Brute-Force Attacks:** The high number of iterations makes password cracking expensive.
    
- **Widely Adopted:** Used in standards like WPA2, PKCS #5, and NIST guidelines.
    
- **Customizable:** The number of iterations and hash function can be adjusted for different security needs.
    

### **Implementation in TypeScript**

```typescript
import crypto from 'crypto';

const hashPassword = (password: string, salt: string, iterations = 100000, keyLength = 64): Promise<string> => {
    return new Promise((resolve, reject) => {
        crypto.pbkdf2(password, salt, iterations, keyLength, 'sha512', (err, derivedKey) => {
            if (err) reject(err);
            resolve(derivedKey.toString('hex'));
        });
    });
};

const verifyPassword = async (password: string, salt: string, hashedPassword: string): Promise<boolean> => {
    const hashedInput = await hashPassword(password, salt);
    return hashedInput === hashedPassword;
};

// Example Usage
(async () => {
    const password = "securePassword123";
    const salt = crypto.randomBytes(16).toString('hex');
    
    const hashed = await hashPassword(password, salt);
    console.log("Hashed Password:", hashed);
    
    const isMatch = await verifyPassword("securePassword123", salt, hashed);
    console.log("Password Match:", isMatch);
})();
```

### **Conclusion**

PBKDF2 is a reliable and secure password hashing algorithm widely used in modern applications. While not as memory-hard as Argon2, it provides strong security when implemented with a high number of iterations and a strong hash function.