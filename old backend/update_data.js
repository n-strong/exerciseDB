function fetchEntityData(fieldName) {
  var selectElement = document.getElementById("input-entity2-html");
  var selectedValue = selectElement.value;

  // Make an AJAX request to fetch the existing entity data based on the selected value
  // Update the input field with the fetched data

  fetch("/fetch-entity-data?entity_id=" + selectedValue)
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      // Update the input field with the fetched data
      var inputElement = document.getElementById("input-entity-name");
      inputElement.value = data[fieldName];
    })
    .catch(function(error) {
      console.log(error);
    });
}
