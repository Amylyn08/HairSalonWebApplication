document.addEventListener('DOMContentLoaded', function(){
    // Get the toggle checkbox
    const toggleCheckbox = document.getElementById('toggle');

    // Get the register form
    const registerForm = document.querySelector('#register-div form');

    // Get the professional fields section
    const proFields = document.getElementById('pro-fields');

    // Add event listener to toggle checkbox
    toggleCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // If Professional is selected
            proFields.removeAttribute('hidden');
        } else {
            // If Client is selected
            proFields.setAttribute('hidden', true);
        }
    });

    // Initial state
    if (toggleCheckbox.checked) {
        // If Professional is selected initially
        proFields.removeAttribute('hidden');
    } else {
        // If Client is selected initially
        proFields.setAttribute('hidden', true);
    }
});
