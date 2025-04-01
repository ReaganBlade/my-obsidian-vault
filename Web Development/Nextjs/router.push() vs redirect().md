In **Next.js with NextAuth.js**, you can use either `router.push` or `redirect` for navigation after authentication, but they serve slightly different purposes.

### **1. `router.push()` (Client-side Navigation)**

- Uses the **Next.js router** (`useRouter`) to navigate **without a full page reload**.
    
- Works **on the client side** after an async operation.
    
- Example:
    
    ```tsx
    import { useRouter } from "next/router";
    
    const router = useRouter();
    router.push("/dashboard"); // Navigates to dashboard
    ```
    

### **2. `redirect()` (Server-side Navigation)**

- Used within API routes, middleware, or `getServerSideProps()`.
    
- Causes a **full-page reload** (server-side redirection).
    
- Example in `getServerSideProps()`:
    
    ```tsx
    export async function getServerSideProps(context) {
      return {
        redirect: {
          destination: "/dashboard",
          permanent: false,
        },
      };
    }
    ```
    

### **Which One to Use?**

✅ Use **`router.push()`** for client-side redirection after login/logout.  
✅ Use **`redirect()`** when handling authentication inside API routes or `getServerSideProps()`.

For **NextAuth.js**, `router.push()` is often preferred after sign-in:

```tsx
import { signIn } from "next-auth/react";
import { useRouter } from "next/router";

const router = useRouter();

async function handleLogin() {
  await signIn("google");
  router.push("/dashboard"); // Redirects after login
}
```