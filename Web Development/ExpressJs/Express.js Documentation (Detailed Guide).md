## 📌 What is Express.js?

**Express.js** is a minimal and flexible Node.js web application framework that provides a robust set of features for building web and mobile applications. It is widely used for developing RESTful APIs and single-page, multipage, or hybrid web applications.

## 🚀 Why Use Express?

- Lightweight and fast
    
- Middleware support
    
- Routing made easy
    
- HTTP utility methods
    
- Integration with databases and other tools
    
- Huge community and ecosystem
    

---

## 🛠️ Installation

```bash
npm install express
```

### Basic Setup Example

```js
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

---

## 🌐 Real-World Use Case: RESTful API for Products

```js
const express = require('express');
const app = express();
const PORT = 5000;

let products = [
  { id: 1, name: 'Laptop' },
  { id: 2, name: 'Phone' }
];

app.use(express.json()); // for parsing application/json

// GET all products
app.get('/products', (req, res) => {
  res.json(products);
});

// GET single product
app.get('/products/:id', (req, res) => {
  const product = products.find(p => p.id == req.params.id);
  if (!product) return res.status(404).send('Product not found');
  res.json(product);
});

// POST new product
app.post('/products', (req, res) => {
  const product = { id: products.length + 1, name: req.body.name };
  products.push(product);
  res.status(201).json(product);
});

// PUT update product
app.put('/products/:id', (req, res) => {
  const product = products.find(p => p.id == req.params.id);
  if (!product) return res.status(404).send('Product not found');
  product.name = req.body.name;
  res.json(product);
});

// DELETE a product
app.delete('/products/:id', (req, res) => {
  products = products.filter(p => p.id != req.params.id);
  res.status(204).send();
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
```

---

## 🧰 Core Methods in Express

### app.get(path, callback)

Handles GET requests.

### app.post(path, callback)

Handles POST requests.

### app.put(path, callback)

Handles PUT requests.

### app.delete(path, callback)

Handles DELETE requests.

### app.use([path], middleware)

Mounts middleware at a specific path.

### app.listen(port, callback)

Starts the server and listens on the given port.

---

## 🧱 Middleware in Express

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application’s request-response cycle.

### Example:

```js
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});
```

Types:

- Application-level middleware
    
- Router-level middleware
    
- Error-handling middleware
    
- Built-in middleware (like `express.json()`)
    

---

## 🔀 Routing in Express

Routing refers to how an application’s endpoints (URIs) respond to client requests.

### Route Parameters:

```js
app.get('/users/:userId', (req, res) => {
  res.send(`User ID: ${req.params.userId}`);
});
```

### Query Parameters:

```js
app.get('/search', (req, res) => {
  res.send(`Search Query: ${req.query.q}`);
});
```

---

## 🧩 Template Engines

Express supports various template engines like:

- Pug
    
- EJS
    
- Handlebars
    

### Example with EJS:

```bash
npm install ejs
```

```js
app.set('view engine', 'ejs');
app.get('/', (req, res) => {
  res.render('index', { title: 'Express App' });
});
```

---

## 🔐 Handling Static Files

Use the `express.static` middleware to serve static assets.

```js
app.use(express.static('public'));
```

---

## 🧪 Error Handling

```js
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});
```

---

## 🧾 Best Practices

- Structure your app using MVC pattern
    
- Use environment variables (`dotenv`)
    
- Validate inputs (e.g., `Joi`, `express-validator`)
    
- Secure your app with `helmet`, `cors`
    
- Use `morgan` for logging
    
- Handle errors gracefully
    

---

## 📚 Useful Libraries with Express

- **body-parser**: Parses incoming request bodies (now part of Express)
    
- **cors**: Enable cross-origin requests
    
- **helmet**: Secures HTTP headers
    
- **morgan**: HTTP request logger
    
- **dotenv**: Environment variable management
    
- **jsonwebtoken**: JWT-based authentication
    

---

## 🧾 Conclusion

Express.js is a powerful and efficient framework for building backend services in Node.js. With its simplicity, scalability, and support for a wide range of middleware, it's an ideal choice for RESTful APIs, web apps, and more.

---

## 🔗 Resources

- [Official Express.js Website](https://expressjs.com/)
    
- [Express GitHub Repo](https://github.com/expressjs/express)
    
- [Node.js Documentation](https://nodejs.org/)
    
- [REST API Design Guide](https://restfulapi.net/)