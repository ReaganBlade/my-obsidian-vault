**Step-by-Step Guide to Implementing Server Actions in Appwrite**

## **1. Setting Up Appwrite SDK in Your Project**

### **Install Appwrite SDK**

Ensure you have Appwrite's SDK installed in your Next.js project:

```sh
npm install appwrite
```

### **Configure Appwrite Client**

Create a file `config/appwrite.ts` and initialize the Appwrite SDK:

```ts
import { Client, Databases } from 'appwrite';

const client = new Client();

client
  .setEndpoint(process.env.NEXT_PUBLIC_APPWRITE_ENDPOINT as string)
  .setProject(process.env.NEXT_PUBLIC_APPWRITE_PROJECT_ID as string);

export const databases = new Databases(client);
```

---

## **2. Implementing Server Actions**

### **User Actions (Users Collection)**

#### **1. Save User Data**

- This action stores user profile data after OAuth authentication.
    
- Requires: `user_id`, `name`, `email`, `profile_picture`.
    
- Call this function after a successful authentication response.
    

#### **2. Get User Data**

- Fetches user profile data based on `user_id`.
    
- Useful for user authentication validation and displaying profiles.
    

---

### **Playlist Actions (Playlists Collection)**

#### **1. Create a Playlist**

- Adds a new playlist linked to a `user_id`.
    
- Requires: `user_id`, `name`, `videos` (array of video IDs).
    
- Helps users organize educational videos efficiently.
    

#### **2. Get Playlists for a User**

- Retrieves all playlists associated with a `user_id`.
    
- Enables users to access and manage their saved videos.
    

#### **3. Delete a Playlist**

- Removes a specific playlist from the collection using `playlistId`.
    
- Allows users to clean up unwanted or outdated playlists.
    

---

## **3. Setting Up Environment Variables**

Add the required environment variables in `.env.local`:

```env
NEXT_PUBLIC_APPWRITE_ENDPOINT=your-appwrite-endpoint
NEXT_PUBLIC_APPWRITE_PROJECT_ID=your-appwrite-project-id
NEXT_PUBLIC_APPWRITE_DATABASE_ID=your-database-id
NEXT_PUBLIC_APPWRITE_USERS_COLLECTION_ID=your-users-collection-id
NEXT_PUBLIC_APPWRITE_PLAYLISTS_COLLECTION_ID=your-playlists-collection-id
```

---

## **4. Error Handling & Debugging**

- Wrap all API calls in `try-catch` blocks.
    
- Log errors for debugging purposes.
    
- Use Appwrite's dashboard to verify database updates and permissions.
    

---

## **5. Testing the Server Actions**

- Use `console.log()` to verify API responses.
    
- Ensure data is correctly stored in Appwrite's dashboard.
    
- Test retrieval and deletion of data through API calls.