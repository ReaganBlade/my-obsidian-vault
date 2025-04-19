## 📌 What is Multer?

**Multer** is a middleware for handling `multipart/form-data`, which is primarily used for uploading files in Node.js applications. It is written on top of the **busboy** library and makes it easy to process form submissions containing files.

## 🔧 Why Use Multer?

When a user uploads a file via a form, the browser sends the file in a format called `multipart/form-data`. Node.js doesn’t handle this by default. That’s where Multer comes in — it parses incoming requests with file uploads and makes the uploaded files available in the `req.file` or `req.files` object.

## 🛠️ Installation

```bash
npm install multer
```

---

## 🗂️ Basic Use Case: File Upload API

### Example: Upload a profile picture

### 1. Folder Structure:

```
project-directory/
├── uploads/
├── index.js
└── package.json
```

### 2. Create `index.js`

```js
const express = require('express');
const multer  = require('multer');
const path = require('path');

const app = express();
const port = 3000;

// Configure storage
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')  // save files to 'uploads/' directory
  },
  filename: function (req, file, cb) {
    cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname))
  }
});

// Initialize multer with storage config
const upload = multer({ storage: storage });

// Route to handle file upload
app.post('/upload', upload.single('profilePic'), (req, res) => {
  try {
    res.send({
      message: 'File uploaded successfully',
      file: req.file
    });
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

### 3. Test using Postman or HTML Form

#### HTML Example:

```html
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="profilePic" />
  <button type="submit">Upload</button>
</form>
```

---

## 🔄 Multer Methods

### `multer(options)`

- Initializes multer with a storage engine and/or file filter.
    

### `upload.single(fieldname)`

- Accepts a single file with the given `fieldname`.
    
- File info available on `req.file`
    

### `upload.array(fieldname[, maxCount])`

- Accepts multiple files with the same field name.
    
- Files info available on `req.files`
    

### `upload.fields(fields)`

- Accepts a mix of files with different field names.
- Example:
    

```js
upload.fields([
  { name: 'avatar', maxCount: 1 },
  { name: 'gallery', maxCount: 8 }
])
```

- File info available on `req.files`
    

### `upload.none()`

- Accepts only text fields; no files.
    

---

## 🧠 Multer Storage Engines

### 1. `diskStorage` (default)

Stores files locally on disk.

```js
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname)
  }
});
```

### 2. `memoryStorage`

Stores files in memory as Buffer.

```js
const storage = multer.memoryStorage();
```

Useful for uploading directly to cloud services (e.g. AWS S3).

---

## ✅ File Filter

Use fileFilter to control which files to accept.

```js
const upload = multer({
  storage: storage,
  fileFilter: function (req, file, cb) {
    if (file.mimetype === 'image/jpeg' || file.mimetype === 'image/png') {
      cb(null, true);
    } else {
      cb(new Error('Only .jpeg or .png allowed!'), false);
    }
  }
});
```

---

## 🔐 Limits

Set limits for file size, number of files, etc.

```js
const upload = multer({
  storage: storage,
  limits: { fileSize: 1024 * 1024 * 2 } // 2MB
});
```

---

## 📂 Accessing Uploaded File

```js
app.post('/upload', upload.single('profilePic'), (req, res) => {
  console.log(req.file);
  /*
  req.file = {
    fieldname: 'profilePic',
    originalname: 'myphoto.jpg',
    encoding: '7bit',
    mimetype: 'image/jpeg',
    destination: 'uploads/',
    filename: 'profilePic-1619993134343.jpg',
    path: 'uploads/profilePic-1619993134343.jpg',
    size: 34567
  }
  */
});
```

---

## 🧪 Testing Multer

Use tools like:

- Postman (for quick API testing)
    
- Insomnia
    
- Curl
    

---

## 📁 Real-World Use Cases

- Uploading profile pictures, resumes, or documents
    
- Handling CSV uploads for data import
    
- Uploading multiple images for galleries
    
- Temporary file handling before uploading to a cloud (S3, GCP, Azure)
    

---

## ⚠️ Common Errors & Fixes

### `LIMIT_FILE_SIZE`

- File exceeds the size limit.
    
- Fix: Increase limit or validate file size on frontend.
    

### `Unexpected field`

- Field name in form doesn’t match what Multer expects.
    
- Fix: Ensure field name in `upload.single()` or `upload.array()` matches the form.
    

### `File type not allowed`

- Filtered by fileFilter.
    
- Fix: Allow correct `mimetype`.
    

---

## 🧼 Best Practices

- Always validate files on both client and server.
    
- Store temporary files and periodically clean up.
    
- Use `memoryStorage` for immediate processing.
    
- Rename files to avoid collisions.
    
- Keep sensitive file uploads secure.
    

---

## 📚 Resources

- [Multer GitHub Repo](https://github.com/expressjs/multer)
    
- [Multer on npm](https://www.npmjs.com/package/multer)
    
- [Express Documentation](https://expressjs.com/en/resources/middleware/multer.html)
    

---

## 🧾 Conclusion

Multer is a simple yet powerful tool for managing file uploads in Node.js applications. With support for various configurations, filters, limits, and storage strategies, it is an essential middleware when working with form-based uploads.

By following this documentation, you’ll be able to implement secure and efficient file upload features in your Express applications.