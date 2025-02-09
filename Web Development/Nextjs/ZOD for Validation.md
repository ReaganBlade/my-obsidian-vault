To use **Zod** for validation in a Next.js project, follow these steps:

---
### **Step 1: Install Zod**

Run the following command:

```sh
npm install zod
```

Or with yarn:

```sh
yarn add zod
```

---
### **Step 2: Create a Validation Schema**

Create a file `lib/validation.js` (or any suitable location) and define your schema:

```js
import { z } from "zod";

export const signupSchema = z.object({
  name: z.string().min(2, "Name must be at least 2 characters"),
  email: z.string().email("Invalid email format"),
  password: z.string().min(6, "Password must be at least 6 characters"),
});
```

---
### **Step 3: Validate Form Data in an API Route**

Edit or create an API route in `pages/api/signup.js`:

```js
import { signupSchema } from "@/lib/validation";

export default function handler(req, res) {
  if (req.method === "POST") {
    const result = signupSchema.safeParse(req.body);
    if (!result.success) {
      return res.status(400).json({ errors: result.error.format() });
    }
    res.status(200).json({ message: "Signup successful!" });
  } else {
    res.status(405).json({ message: "Method Not Allowed" });
  }
}
```

---
### **Step 4: Validate on the Client Side (Optional)**

If you want to validate in a React form:

```js
import { useState } from "react";
import { signupSchema } from "@/lib/validation";

export default function SignupForm() {
  const [errors, setErrors] = useState({});

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = {
      name: e.target.name.value,
      email: e.target.email.value,
      password: e.target.password.value,
    };

    const result = signupSchema.safeParse(formData);
    if (!result.success) {
      setErrors(result.error.format());
    } else {
      console.log("Valid Data:", result.data);
      setErrors({});
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" />
      {errors.name && <p>{errors.name._errors[0]}</p>}

      <input name="email" placeholder="Email" />
      {errors.email && <p>{errors.email._errors[0]}</p>}

      <input name="password" type="password" placeholder="Password" />
      {errors.password && <p>{errors.password._errors[0]}</p>}

      <button type="submit">Sign Up</button>
    </form>
  );
}
```

---
### **Done! ✅**

Now, your Next.js project has **Zod** validation both on the **server** and **client-side**! 🚀
(Setting-Up)[www.google.com]
