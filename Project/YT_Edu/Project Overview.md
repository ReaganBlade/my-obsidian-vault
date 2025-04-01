**Project: YouTube Educational Content Filter Platform**

## **🔹 Overview**

A web-based platform that filters and categorizes only educational videos from YouTube, reducing distractions and improving learning efficiency. The platform will use YouTube API for fetching videos, Google OAuth 2.0 for authentication, and Appwrite for storage and authentication.

---

## **🔹 Tech Stack**

- **Frontend:** Next.js (App Router), TailwindCSS, Shadcn
    
- **Backend:** Next.js API routes & Server Actions
    
- **Database & Storage:** Appwrite (for authentication & playlists)
    
- **Authentication:** OAuth 2.0 (Google)
    
- **YouTube API:** Fetch & filter educational videos
    

---

## **🔹 MVP Features**

1. **User Authentication** – OAuth 2.0-based login via Google to access YouTube accounts.
    
2. **Video Filtering & Categorization** – Fetch and display only educational content using predefined filters.
    
3. **Custom Playlists** – Allow users to save filtered videos into custom playlists.
    
4. **Minimal UI** – Clean and distraction-free interface using TailwindCSS and Shadcn components.
    

---

## **🔹 Folder Structure**

```
/yt-content-filter  
│── /public                 # Static assets  
│── /src  
│   ├── /app  
│   │   ├── /api  
│   │   │   ├── youtube/route.ts   # Server action for fetching videos  
│   │   │   ├── auth/route.ts      # OAuth authentication logic  
│   │   │   ├── playlists/route.ts # CRUD API for saving playlists  
│   │   ├── /auth  
│   │   │   ├── page.tsx           # Login page  
│   │   ├── /dashboard  
│   │   │   ├── page.tsx           # Main page after login  
│   │   ├── /playlists  
│   │   │   ├── page.tsx           # View saved playlists  
│   │   ├── layout.tsx             # Main layout with navbar  
│   │   ├── page.tsx               # Landing page  
│   ├── /components  
│   │   ├── ui/  
│   │   │   ├── Button.tsx         # Custom button  
│   │   │   ├── Card.tsx           # Video card  
│   │   │   ├── Navbar.tsx         # Top navbar  
│   │   │   ├── Sidebar.tsx        # Sidebar for filtering  
│   │   │   ├── PlaylistCard.tsx   # Playlist card component  
│   │   ├── auth/  
│   │   │   ├── GoogleAuth.tsx     # OAuth 2.0 button  
│   │   ├── video/  
│   │   │   ├── VideoList.tsx      # Renders list of videos  
│   │   │   ├── VideoPlayer.tsx    # Embedded YT player  
│   ├── /config  
│   │   ├── appwrite.ts            # Appwrite config (DB, Auth, Storage)  
│   │   ├── youtube.ts             # YouTube API config  
│   ├── /lib  
│   │   ├── auth.ts                # Authentication helpers  
│   │   ├── youtube.ts             # YouTube API helpers  
│   │   ├── db.ts                  # Database helpers  
│   ├── /styles  
│   │   ├── globals.css            # Global Tailwind styles  
│   ├── /context  
│   │   ├── AuthContext.tsx        # Global auth state  
│   │   ├── PlaylistContext.tsx    # Global playlist state  
│── .env                           # API keys & environment variables  
│── next.config.mjs                # Next.js config  
│── tailwind.config.js             # Tailwind config  
│── package.json                    # Dependencies  
│── README.md                      # Project documentation  
```

---

## **🔹 API Routes (/api)**

- **`api/youtube/route.ts`** → Fetches videos from YouTube API
    
- **`api/auth/route.ts`** → Handles Google OAuth login
    
- **`api/playlists/route.ts`** → CRUD operations for playlists
    

---

## **🔹 App Configs (/config)**

- **`appwrite.ts`** → Configures Appwrite services (DB, Auth, Storage)
    
- **`youtube.ts`** → Manages YouTube API requests
    

---

## **🔹 Components (/components)**

### **📌 UI Components (/ui)**

- `Button.tsx` → Reusable button
    
- `Card.tsx` → Video preview card
    
- `Navbar.tsx` → Main navigation
    
- `Sidebar.tsx` → Filters for categories
    
- `PlaylistCard.tsx` → Playlist preview
    

### **📌 Authentication Components (/auth)**

- `GoogleAuth.tsx` → Google OAuth button
    

### **📌 Video Components (/video)**

- `VideoList.tsx` → Displays fetched videos
    
- `VideoPlayer.tsx` → Embedded YouTube video player
    

---

## **🔹 Context Providers (/context)**

- **`AuthContext.tsx`** → Manages auth state
    
- **`PlaylistContext.tsx`** → Stores playlist state
    

---

## **📌 Next Steps**

1. **Set up Next.js & Appwrite integration**
    
2. **Implement Google OAuth login**
    
3. **Fetch & display educational YouTube videos**
    
4. **Enable saving videos into playlists**
    

---

This document will be updated as the project progresses. 🚀