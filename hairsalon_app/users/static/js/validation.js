document.addEventListener("DOMContentLoaded", function(){
    let formFields = [
        'username', 'full_name', 'email', 'password', 'confirm-password',
        'phone_number', 'address', 'age', 'pay_rate', 'specialty'
    ];

    // Function to validate form fields
    function validateFields() {
        formFields.forEach(fieldName => {
            let field = document.getElementById(fieldName);
            validateField(field);
        });
    }

    // Function to validate a single form field
    function validateField(field) {
        let errorMessageId = field.id + "-error";
        let errorMessageElement = document.getElementById(errorMessageId);

        if (field.value.trim() === "") {
            // Set border color to red
            field.style.borderColor = "red";
            field.style.boxShadow = "0 0 5px red";

            // Create error message element if not exists
            if (!errorMessageElement) {
                errorMessageElement = document.createElement("p");
                errorMessageElement.id = errorMessageId;
                errorMessageElement.style.color = "red";
                errorMessageElement.textContent = "This field is required";
                field.parentNode.insertBefore(errorMessageElement, field.nextSibling);
            }
        } else {
            // Reset border color
            field.style.borderColor = "";
            field.style.boxShadow = "";

            // Remove error message element if exists
            if (errorMessageElement) {
                errorMessageElement.parentNode.removeChild(errorMessageElement);
            }
        }
    }

    // Listen for input event on each form field
    formFields.forEach(fieldName => {
        let field = document.getElementById(fieldName);
        field.addEventListener('input', validateFields);
        field.addEventListener('blur', validateFields);
    });

    validateFields();
});
