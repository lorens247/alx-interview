# 0x06 - Star Wars API

## Introduction
This project explores working with the Star Wars API (SWAPI) to retrieve and display information about characters, planets, starships, and more from the Star Wars universe. It covers essential concepts such as making HTTP requests in JavaScript, working with RESTful APIs, asynchronous programming, command-line arguments in Node.js, and array manipulation and iteration.

## Concepts Needed

### HTTP Requests in JavaScript
- **Understanding**: Making HTTP requests to external services using the request module or alternatives like fetch in Node.js.
- **Resource**: [A Complete Guide to Making HTTP Requests in Node.js](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)

### Working with APIs
- **Understanding**: Basics of RESTful APIs and how to interact with them, parsing JSON data returned by APIs, and working with APIs in JavaScript.
- **Resource**: [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

### Asynchronous Programming
- **Understanding**: Managing asynchronous operations with callbacks, promises, and async/await syntax, handling API response data asynchronously.
- **Resource**: [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

### Command Line Arguments in Node.js
- **Understanding**: Using the `process.argv` array to access command-line arguments passed to a Node.js script.
- **Resource**: [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/how-to-parse-command-line-arguments-in-nodejs)

### Array Manipulation and Iteration
- **Understanding**: Iterating over arrays and manipulating data structures to format and display character names.
- **Resource**: [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Usage
1. Clone the repository:
   
   git clone https://github.com/lorens247/alx-interview/0x06-star-wars-api.git

2. Navigate to the project directory:

    cd 0x06-star-wars-api

3.  Install dependencies (if any):

    npm install

4.  Run the application:

    node 0-starwars_characters.js <command> [arguments]

5.  Commands

    Display Character Details: Retrieve and display details of a specific Star Wars character.

    ./0-starwars_characters.js 3 <character-name>

6.  List Characters: List all Star Wars characters.

   ./0-starwars_characters.js 
