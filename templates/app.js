document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    var form = document.querySelector('form');

    // Add event listener to the form for form submission
    form.addEventListener('submit', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Get the user input textarea element
        var userInput = form.querySelector('textarea[name="user_input"]');

        // Get the value of the user input
        var userInputValue = userInput.value.trim();

        // Check if the user input is empty
        if (userInputValue === '') {
            // Display an alert message if the user input is empty
            alert('Please enter some text before generating.');
            return;
        }

        // If the user input is not empty, submit the form
        form.submit();
    });
});
