# JavaScript - DOM Manipulation

▶ **Introduction** 

JavaScript DOM Manipulation refers to the process of using JavaScript to interact with and modify the Document Object Model (DOM) of a web page. The DOM is a tree-like structure representing the content, structure, and elements of an HTML document. By manipulating the DOM, developers can dynamically change the content, style, and behavior of web pages in response to user actions or data fetched from external sources. In this project, JavaScript DOM Manipulation is used to create interactive web pages, update elements, handle events, and fetch data from APIs.

▶ **Table of Contents**

- [Overview](#overview)
- [Concepts](#concepts)
- [Example](#example)
- [Installation](#installation)
- [Author](#author)

▶ **Overview** 

This project demonstrates practical usage of JavaScript to manipulate the DOM. It covers selecting elements, updating styles and text, handling user events, dynamically adding elements, toggling classes, and fetching data from APIs to update the page content. Each script in this folder corresponds to a specific DOM manipulation task, providing hands-on examples for learning and reference.

▶ **Concepts**

- **DOM (Document Object Model):** A programming interface for HTML and XML documents, representing the page so programs can change the document structure, style, and content.
- **Element Selection:** Using methods like `document.querySelector` to select HTML elements for manipulation.
- **Event Handling:** Responding to user actions using event listeners such as `addEventListener`.
- **Class Manipulation:** Adding, removing, or toggling CSS classes on elements to change their appearance or behavior.
- **Dynamic Content Creation:** Creating and appending new elements to the DOM using methods like `createElement` and `appendChild`.
- **Fetch API:** Retrieving data from external sources asynchronously and updating the DOM with the results.
- **Promises:** Handling asynchronous operations, such as API requests, with `.then()` and `.catch()`.

▶ **Example** 


**To change header color on click:**

```javascript
document.querySelector('#red_header').addEventListener('click', function() {
  document.querySelector('header').style.color = '#FF0000';
});
```


▶ **Installation**

Clone this repository in your terminal:

```bash
git clone https://github.com/kamisos3/holbertonschool-higher_level_programming/tree/main/javascript-dom_manipulation
```

▶ **Author**

Kami Sostre [https://github.com/kamisos3]