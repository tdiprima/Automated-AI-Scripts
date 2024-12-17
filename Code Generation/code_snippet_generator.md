# Fetching Data from API with Error Handling

Below is an example of a JavaScript function that fetches data from an API using the `fetch` API and includes error handling to ensure a smooth user experience.

```javascript
/**
 * Fetches data from the provided URL.
 *
 * @param {string} url - The URL of the API endpoint.
 * @returns {Promise<object>} A promise that resolves with the fetched data or rejects with an error.
 */
async function fetchData(url) {
  try {
    // Using the fetch function to make a GET request
    const response = await fetch(url);

    // Checking if the response is OK (200-299)
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    // Parsing the JSON response data
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error; // Re-throw the error to allow it to propagate up the call stack
  }
}

// Example usage:
const apiUrl = 'https://api.example.com/data';
fetchData(apiUrl)
  .then((data) => console.log(data))
  .catch((error) => console.error('Failed to fetch data:', error));
```

**Explanation:**

*   We import the `fetch` function, which is used to make HTTP requests.
*   The `fetchData` function takes a URL as an argument and returns a promise that resolves with the fetched data or rejects with an error.
*   Inside the `try-catch` block, we use the `fetch` function to make a GET request to the provided URL.
*   We check if the response is OK (200-299) by checking the `ok` property. If it's not, we throw an error with the HTTP status code.
*   If the response is OK, we parse the JSON response data using the `json()` method and return it.
*   In the `catch` block, we log the error to the console and re-throw it to allow it to propagate up the call stack.

This example demonstrates a basic implementation of fetching data from an API with error handling. You can modify and extend this code to suit your specific use case and requirements.

<br>
