### **Users Collection**

**Collection ID:** `users` **Description:** Stores user profile information.

#### **Attributes:**

- `user_id` → **String** (Required, Unique)
    
- `name` → **String** (Required)
    
- `email` → **String** (Required, Unique)
    
- `profile_picture` → **String** (Optional)
    

#### **Permissions:**

- **Read:** Only the user (`user:$userId`)
    
- **Write:** Only the user (`user:$userId`)
    
- **Create:** Any authenticated user (`role:member`)
    

---

### **Playlists Collection**

**Collection ID:** `playlists` **Description:** Stores user-created playlists.

#### **Attributes:**

- `user_id` → **String** (Required, Index)
    
- `name` → **String** (Required)
    
- `videos` → **Array of Strings** (Stores video IDs/Links)
    
- `description` → **String** (Optional, Description of the playlist)
    
- `created_at` → **DateTime** (Required)
    
- `visibility`→ **ENUM (PUBLIC/PRIVATE)** (REQUIRED)

#### **Permissions:**

- **Read:** Only the playlist owner (`user:$userId`)
    
- **Write:** Only the playlist owner (`user:$userId`)
    
- **Create:** Any authenticated user (`role:member`)
    

---
