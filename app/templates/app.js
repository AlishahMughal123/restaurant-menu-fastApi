// Make an HTTP GET request to the FastAPI endpoint
fetch('http://127.0.0.1:8000/breakfasts', {
    headers: {
        'Access-Control-Allow-Origin' : 'no-cors'
    },
}).then(response => response.json()).then(data => {
    // Update the HTML table with the data
    const tableBody = document.querySelector('#breakfast-table tbody');
    data.forEach(breakfast => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${breakfast.name}</td>
        <td>${breakfast.description}</td>
        <td>${breakfast.price}</td>
      `;
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error(error));
