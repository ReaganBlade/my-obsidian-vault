
Next.js uses a file-based routing system. This means the structure of your application’s `pages/` directory defines the routes of your application automatically. Here's a detailed explanation of how it works, including examples:

---

## 1. **Basic Routing**

Each `.js`, `.jsx`, `.ts`, or `.tsx` file inside the `pages/` directory becomes a route.

**Example:**

```
pages/
  index.js       =>  /
  about.js       =>  /about
  contact.js     =>  /contact
```

**Explanation:**

- `index.js` maps to the homepage (`/`).
- `about.js` maps to `/about`.
- `contact.js` maps to `/contact`.

---

## 2. **Nested Routes**

Folders inside the `pages/` directory create nested routes.

**Example:**

```
pages/
  blog/
    index.js     =>  /blog
    post.js      =>  /blog/post
```

**Explanation:**

- A file at `pages/blog/index.js` becomes `/blog`.
- A file at `pages/blog/post.js` becomes `/blog/post`.

---

## 3. **Dynamic Routes**

Use square brackets `[param]` to create dynamic routes.

**Example:**

```
pages/
  product/
    [id].js      =>  /product/:id
```

**Explanation:**

- A request to `/product/123` will render `pages/product/[id].js` with `id = 123`.
- Use `useRouter()` from `next/router` to get the dynamic route value.

```js
import { useRouter } from 'next/router';

export default function Product() {
  const router = useRouter();
  const { id } = router.query;

  return <h1>Product ID: {id}</h1>;
}
```

---

## 4. **Catch-All Routes**

Catch-all routes match multiple segments and use `[...param]`.

**Example:**

```
pages/
  docs/
    [...slug].js => /docs/*
```

**Explanation:**

- `/docs/a/b/c` maps to `pages/docs/[...slug].js`.
- `slug` is an array: `["a", "b", "c"]`.

---

## 5. **Optional Catch-All Routes**

Use `[[...param]]` for optional catch-all segments.

**Example:**

```
pages/
  docs/
    [[...slug]].js => /docs/* (including /docs)
```

**Explanation:**

- Matches `/docs` and any nested paths.
- When no extra segment is present, `slug` will be `undefined`.

---

## 6. **API Routes**

Any file in `pages/api/` is mapped to `/api/*` and treated as an API endpoint.

**Example:**

```
pages/
  api/
    hello.js     =>  /api/hello
```

```js
export default function handler(req, res) {
  res.status(200).json({ message: "Hello World" });
}
```

---

## 7. **Custom 404 Page**

Create a `404.js` file in the `pages/` directory to handle unmatched routes.

**Example:**

```
pages/
  404.js         =>  Custom 404 Page
```

---

## 8. **Linking Between Pages**

Use the `next/link` component to navigate between routes without reloading the page.
```js
import Link from 'next/link';

export default function Home() {
  return (
    <nav>
      <Link href="/about">About</Link>
      <Link href="/contact">Contact</Link>
    </nav>
  );
}
```

---

## 9. **Programmatic Navigation**

Use `useRouter().push()` to navigate programmatically.

```js
import { useRouter } from 'next/router';

export default function DashboardButton() {
  const router = useRouter();

  return <button onClick={() => router.push('/dashboard')}>Go to Dashboard</button>;
}
```

---

## Summary Table

| File/Folder               | Route URL       |
| ------------------------- | --------------- |
| `pages/index.js`          | `/`             |
| `pages/about.js`          | `/about`        |
| `pages/blog/index.js`     | `/blog`         |
| `pages/blog/[id].js`      | `/blog/:id`     |
| `pages/docs/[...slug].js` | `/docs/*`       |
| `pages/api/hello.js`      | `/api/hello`    |
| `pages/404.js`            | Custom 404 Page |

---

This is how Next.js handles routing purely through your file structure, making navigation intuitive and easy to manage.