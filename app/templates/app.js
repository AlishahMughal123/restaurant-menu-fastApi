// Define a variable to store the selected menu option
let selectedOption = '';

// Attach an event listener to the dropdown menu items
$(".dropdown-menu a").click(function() {
  selectedOption = $(this).attr("data-value");
  $("#dropdownMenuButton").text($(this).text());
  $("#dropdownMenuButton").val(selectedOption);

  // Make a new HTTP GET request to the appropriate endpoint based on the selected menu option
  let endpoint = '';
  if (selectedOption === 'Breakfast') {
    endpoint = 'http://127.0.0.1:8000/breakfasts';
  } else if (selectedOption === 'Lunch') {
    endpoint = 'http://127.0.0.1:8000/lunchs';
  } else if (selectedOption === 'Dinner') {
    endpoint = 'http://127.0.0.1:8000/dinners';
  }

  fetch(endpoint, {
    headers: {
      'Access-Control-Allow-Origin' : 'no-cors'
    },
  })
  .then(response => response.json())
  .then(data => {
    // Clear the table body
    const tableBody = document.querySelector('#breakfast-table tbody');
    tableBody.innerHTML = '';

    // Update the table body with the new data
    data.forEach(menuItem => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${menuItem.name}</td>
        <td>${menuItem.description}</td>
        <td>${menuItem.price}</td>
      `;
      tableBody.appendChild(row);
    });
  })
  .catch(error => console.error(error));
});
