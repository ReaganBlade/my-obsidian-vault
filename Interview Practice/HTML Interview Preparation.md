### 1. Can we display a web page inside a web page? Is nesting of web pages possible?

Yes, nesting of web pages is possible using the `<iframe>` tag.  
The `<iframe>` element allows embedding another HTML page within the current page. It acts as a window displaying another document, enabling multiple levels of nesting if needed.
	Follow up question: how does `<iframe>` tag work?
		The `<iframe>` (Inline Frame) tag in HTML is used to embed another HTML page within the current page.

		How it works:
		- The `<iframe>` acts like a small window on your webpage that displays another webpage inside it.
		- You set the `src` attribute to the URL of the page you want to display.
		- You can control its size with `width` and `height` attributes.
		- You can also style and control its behavior with CSS and other attributes like `allowfullscreen`, `frameborder`, etc.

		**Example:**
		```html
		<iframe src="https://example.com" width="600" height="400"></iframe>
		```
		
		This will show the `example.com` webpage inside your current page, within a 600x400 box.
		

---

### 2. What are Tags and Attributes in HTML?

Tags are the primary building blocks of an HTML document. They define the structure, formatting, and organization of the web content, such as headings, paragraphs, links, images, and more.  
Attributes provide additional information about HTML elements. They are always specified in the opening tag and usually come in name/value pairs like `name="value"`, helping to modify the behavior or appearance of the element.

---

### 3. What are Void Elements in HTML?

Void elements are HTML elements that do not have any closing tag and are self-contained. They perform their function without requiring a closing tag because they do not enclose any content.  
**Examples include:**

- `<br>` (line break)
- `<img />` (image embedding)
- `<hr />` (horizontal rule)

---

### 4. What is the advantage of collapsing white space?

In HTML, a sequence of multiple white space characters (spaces, tabs, newlines) is treated as a single space character. This behavior is known as **collapsing white space**.  
The advantage of collapsing white space is that developers can freely format and indent HTML code for better readability and organization without worrying about affecting the visual layout of the webpage. It simplifies maintaining and editing code.

---

### 5. What are HTML Entities?

HTML entities are special codes used to represent characters that either have reserved meaning in HTML or are not readily available on the keyboard.  
Entities begin with an ampersand (`&`) and end with a semicolon (`;`). They ensure that browsers display the intended symbols.  
**Examples:**

- `&lt;` for `<`
- `&gt;` for `>`
- `&amp;` for `&`
- `&nbsp;` for a non-breaking space

---

### 6. What are different types of lists in HTML?

HTML supports three main types of lists:

- **Ordered List (`<ol>`)**: A list where items are numbered.
- **Unordered List (`<ul>`)**: A list where items are bulleted.
- **Description List (`<dl>`)**: A list consisting of terms and their descriptions.

Each type helps organize information in a specific way suited to different types of content.

---

### 7. What is the ‘class’ attribute in HTML?

The `class` attribute is used to assign one or more class names to an HTML element.  
Classes are primarily used to apply CSS styles or JavaScript functionality to groups of elements that share the same class name.  
Multiple elements can share the same class, making it easier to style or manipulate them collectively.

---

### 8. What is the difference between the ‘id’ attribute and the ‘class’ attribute of HTML elements?

- The `id` attribute uniquely identifies an individual HTML element. No two elements should have the same `id` in a single page.
- The `class` attribute can be shared by multiple elements, allowing them to be grouped and styled together.  
    In short, `id` is **unique**, whereas `class` is **reusable**.

---

### 9. Define multipart form data.

`multipart/form-data` is an encoding type used when submitting forms that include files, such as images or documents, to the server.  
It allows binary data (like files) and text data to be transmitted together in multiple parts within a single form submission.  
This encoding type is specified using the `enctype` attribute in the `<form>` tag:  
`<form enctype="multipart/form-data" method="post">`

---

### 10. Describe HTML layout structure.

An HTML layout typically consists of several semantic elements that organize and structure a webpage clearly.  
Common structural elements include:

- `<header>`: Represents introductory content or navigation links.
- `<nav>`: Defines a block of navigation links.
- `<main>`: Specifies the main content of the document.
- `<section>`: Represents a standalone section of related content.
- `<article>`: Represents a self-contained piece of content.
- `<aside>`: Contains content tangentially related to the main content, like sidebars.
- `<footer>`: Defines the footer for a document or section.

These elements help make the structure more meaningful and improve accessibility and SEO.

---

### 11. How to optimize website assets loading?

Website asset loading can be optimized by:

- **Minifying** CSS, JavaScript, and HTML files.
- **Compressing images** without losing quality.
- **Using lazy loading** for images and videos.
- **Implementing caching** strategies.
- **Using Content Delivery Networks (CDNs)** for faster delivery.
- **Reducing the number of HTTP requests** by combining files.
- **Using asynchronous loading** for non-essential JavaScript files.

---

### 12. What are the various formatting tags in HTML?

HTML provides several formatting tags to style text:

- `<b>`: Bold text (without extra emphasis)
- `<strong>`: Important text (with semantic emphasis)
- `<i>`: Italic text (without extra emphasis)
- `<em>`: Emphasized text (semantic emphasis)
- `<mark>`: Highlighted text
- `<u>`: Underlined text
- `<small>`: Smaller text
- `<del>`: Deleted (strikethrough) text
- `<ins>`: Inserted text (underlined)

---

### 13. What are the different kinds of Doctypes available?

Commonly used Doctypes in HTML include:

- **HTML5 Doctype**: `<!DOCTYPE html>` (simplified and recommended)
- **HTML 4.01 Strict**: `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`
- **HTML 4.01 Transitional**: `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`
- **XHTML 1.0 Strict**: `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">`

Each Doctype tells the browser how to interpret the HTML code.

---

### 14. Please explain how to indicate the character set being used by a document in HTML?

You can specify the character set using the `<meta>` tag inside the `<head>` section.  
For example, to declare UTF-8 encoding, use:

```html
<meta charset="UTF-8">
```

This ensures the correct display of characters from different languages.

---

### 15. What is the difference between `<strong>`, `<b>` tags and `<em>`, `<i>` tags?

- `<strong>` and `<b>` both make text bold, but `<strong>` has semantic importance, indicating that the text is important. `<b>` is purely visual.
- `<em>` and `<i>` both italicize text, but `<em>` conveys emphasis semantically, while `<i>` is used for styling without meaning.

---

### 16. What is the significance of `<head>` and `<body>` tag in HTML?

- The `<head>` tag contains meta-information about the document (title, metadata, links to stylesheets, scripts). It does not display anything directly on the webpage.
- The `<body>` tag contains the actual content that is rendered on the webpage (text, images, links, etc.).

---

### 17. Are the HTML tags and elements the same thing?

No, they are different:

- **Tags** are the markup symbols that define elements (e.g., `<p>`, `</p>`).
- **Elements** consist of the start tag, the content, and the end tag together (e.g., `<p>Hello</p>` is a paragraph element).

---

### 18. How is Cell Padding different from Cell Spacing?

- **Cell Padding**: It defines the space **inside** the cell between the cell content and the cell border.
- **Cell Spacing**: It defines the space **between** individual table cells.

Both are attributes that help control table layout.

---

### 19. How can we club two or more rows or columns into a single row or column in an HTML table?

- Use the `rowspan` attribute to merge multiple rows.
- Use the `colspan` attribute to merge multiple columns.

Example:

```html
<td rowspan="2">Merged Row</td>
<td colspan="3">Merged Columns</td>
```

---

### 20. Is it possible to change an inline element into a block-level element?

Yes, it is possible using CSS by setting the `display` property.  
Example:

```css
span {
  display: block;
}
```

This makes the normally inline `<span>` element behave like a block element.

