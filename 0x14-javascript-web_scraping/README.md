Scripting API Java

Learning Objectives
At the end of this project, i am expected to be able to explain to know:

How to manipulate JSON data
How to use request and fetch API
How to read and write a file using fs module


** Parsig JSON **
const jsonData = '{"name": "John", "age": 25}';
const parsedData = JSON.parse(jsonData);

** Accessing properties **
console.log(parsedData.name); // Output: John
console.log(parsedData.age);  // Output: 25


** Stringfying JSON **
const dataObject = { name: 'Alice', age: 30 };
const jsonString = JSON.stringify(dataObject);

console.log(jsonString); // Output: {"name":"Alice","age":30}


** Using request **
const request = require('request');

request('https://jsonplaceholder.typicode.com/posts/1', (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data);
  } else {
    console.error('Error:', error);
  }
});



** Using Fetch API **
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));


** Reading a file **
const fs = require('fs');

fs.readFile('example.txt', 'utf-8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log('File content:', data);
  }
});


** Writing a file **
const fs = require('fs');

const contentToWrite = 'This is the content to be written to the file.';

fs.writeFile('output.txt', contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing to file:', err);
  } else {
    console.log('File has been written successfully.');
  }
});


	TASKS
0. Readme
Write a script that reads and prints the content of a file.

The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object

1. Write me
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object

2. Status code
Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module request

3. Star wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

The first argument is the movie ID
You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
You must use the module request

4. Star wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request

5. Loripsum
Write a script that gets the contents of a webpage and stores it in a file.

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request

6. How many completed?
Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request

7. Who was playing in this movie?
Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request

8. Right order
Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line in the same order of the list “characters” in the /films/ response
You must use the Star wars API
You must use the module request

