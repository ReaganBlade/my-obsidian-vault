## ✅ What is React Hook Form?

React Hook Form (RHF) is a performant, flexible, and extensible library designed to manage forms in React using hooks. It minimizes re-renders, reduces boilerplate, and offers simple validation while maintaining high performance.

---

## 🚀 Why Use React Hook Form?

- Lightweight and fast
- Minimal re-renders
- Easy integration with UI libraries (Material UI, AntD, etc.)
- Built-in validation and error handling
- Integrates well with Yup and Zod for schema validation

---

## 🛠️ Installation

```bash
npm install react-hook-form
# or
yarn add react-hook-form
```

---

## 🧪 Basic Usage Example

```jsx
import React from 'react';
import { useForm } from 'react-hook-form';

function App() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const onSubmit = data => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("firstName", { required: true })} placeholder="First Name" />
      {errors.firstName && <p>First name is required.</p>}

      <input type="submit" />
    </form>
  );
}
```

---

## 📦 Real-world Use Case Example (With Validation)

```jsx
import { useForm } from 'react-hook-form';
import * as Yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';

const schema = Yup.object().shape({
  email: Yup.string().email().required('Email is required'),
  password: Yup.string().min(6).required('Password is required')
});

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: yupResolver(schema)
  });

  const onSubmit = data => console.log(data);

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register("email")} placeholder="Email" />
      <p>{errors.email?.message}</p>
      <input {...register("password")} type="password" placeholder="Password" />
      <p>{errors.password?.message}</p>
      <button type="submit">Login</button>
    </form>
  );
}
```

---

## 🔧 Core API Methods

### `useForm()`

Initializes the form and returns methods and properties for managing form state.

### `register(name, options)`

Registers an input or select element and includes validation rules.

### `handleSubmit(onValid, onInvalid?)`

Handles the form submission with optional valid and invalid callbacks.

### `formState`

Returns information like `isDirty`, `isValid`, and `errors`.

### `reset(data?)`

Resets the form state and optionally sets default values.

### `setValue(name, value)`

Manually sets a field's value.

### `watch(name?)`

Watches input changes.

### `getValues(name?)`

Gets form values.

### `trigger(name?)`

Triggers validation manually.

---

## 🎯 Integration with UI Libraries

React Hook Form plays nicely with:

- Material UI
- Ant Design
- Chakra UI

```jsx
import { TextField } from '@mui/material';

<TextField
  label="Email"
  {...register("email")}
  error={!!errors.email}
  helperText={errors.email?.message}
/>
```

---

## 📁 Best Practices

- Use `defaultValues` for controlled inputs
- Leverage `useController` for complex UI components
- Integrate schema validation (Yup, Zod)
- Group validation logic using resolvers

---

## ❓ FAQs

### Q: Is RHF better than Formik?

A: RHF is generally faster with fewer re-renders and less boilerplate code.

### Q: Can I use RHF with class components?

A: No, it's designed for function components using hooks.

---

## 🔗 Resources

- [Official Docs](https://react-hook-form.com/)
- [API Reference](https://react-hook-form.com/api/)
- [GitHub](https://github.com/react-hook-form/react-hook-form)
- [Yup Documentation](https://github.com/jquense/yup)

---

## ✅ Conclusion

React Hook Form is a highly performant and easy-to-use solution for managing forms in React. It simplifies validation, enhances performance, and helps build scalable form systems for production apps.