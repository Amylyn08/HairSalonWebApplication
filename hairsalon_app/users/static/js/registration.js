
document.addEventListener('DOMContentLoaded', function(){
    // Get the toggle checkbox
    const toggleCheckbox = document.getElementById('toggle');

    // Get the register forms
    const registerClient = document.getElementById('register_client');
    const registerPro = document.getElementById('register_pro');

    // Add event listener to toggle checkbox
    toggleCheckbox.addEventListener('change', function() {
        if (this.checked) {
            // Show professional registration form
            registerPro.removeAttribute('hidden');
            // Hide client registration form
            registerClient.setAttribute('hidden', true);
        } else {
            // Show client registration form
            registerClient.removeAttribute('hidden');
            // Hide professional registration form
            registerPro.setAttribute('hidden', true);
        }
    });

    // Initial state
    if (toggleCheckbox.checked) {
        // Show professional registration form
        registerPro.removeAttribute('hidden');
        // Hide client registration form
        registerClient.setAttribute('hidden', true);
    } else {
        // Show client registration form
        registerClient.removeAttribute('hidden');
        // Hide professional registration form
        registerPro.setAttribute('hidden', true);
    }
})

