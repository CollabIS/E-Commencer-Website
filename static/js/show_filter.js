document.addEventListener('DOMContentLoaded', function () {
    // Hide all options by default
    document.querySelectorAll('.options').forEach(function (element) {
        element.style.display = 'none';
    });

    // Add event listener to each filter button
    document.querySelectorAll('.filter-buttons div').forEach(function (element) {
        element.addEventListener('click', function () {
            showOptions(element.dataset.target);
        });
    });
});

function showOptions(option) {
    // Hide all options
    document.querySelectorAll('.options').forEach(function (element) {
        element.style.display = 'none';
    });

    // Show the selected option
    document.querySelector('.' + option).style.display = 'block';

    // Reset background color and font color for all buttons
    document.querySelectorAll('.filter-buttons div').forEach(function (element) {
        element.classList.remove('active');
    });

    // Set background color and font color for the selected button
    event.target.classList.add('active');
}

function submitForm() {
      document.forms[0].submit();
   }