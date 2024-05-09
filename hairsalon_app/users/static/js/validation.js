    document.addEventListener("DOMContentLoaded", function(){
        let username = document.getElementById('username');
        let fullName = document.getElementById('full_name');
        let email = document.getElementById('email');
        let password = document.getElementById('password');
        let confirmPassword = document.getElementById('confirm-password');
        let phoneNumber = document.getElementById('phone_number');
        let address = document.getElementById('address');
        let age = document.getElementById('age');
        let payRate = document.getElementById('pay_rate');
        let specialty = document.getElementById('specialty');

        // Function to validate form fields
        function validateFields() {
            // Validate each form field individually
            validateField(username);
            validateField(fullName);
            validateField(email);
            validateField(password);
            validateField(confirmPassword);
            validateField(phoneNumber);
            validateField(address);
            validateField(age);
            validateField(payRate);
            validateField(specialty);
        }

        // Function to validate a single form field
        function validateField(field) {
            // Check if the field is empty
            if (field.value.trim() === "") {
                // Set border color to red
                field.style.borderColor = "red";
                field.style.boxShadow = "0 0 5px red";
                // Set custom error message
                field.setCustomValidity("This field is required");
            } else {
                // Reset border color
                field.style.borderColor = "";
                // Clear custom error message
                field.setCustomValidity("");
            }
        }

        // Listen for input event on each form field
        username.addEventListener('input', validateFields);
        fullName.addEventListener('input', validateFields);
        email.addEventListener('input', validateFields);
        password.addEventListener('input', validateFields);
        confirmPassword.addEventListener('input', validateFields);
        phoneNumber.addEventListener('input', validateFields);
        address.addEventListener('input', validateFields);
        age.addEventListener('input', validateFields);
        payRate.addEventListener('input', validateFields);
        specialty.addEventListener('input', validateFields);

        username.addEventListener('blur', validateFields);
        fullName.addEventListener('blur', validateFields);
        email.addEventListener('blur', validateFields);
        password.addEventListener('blur', validateFields);
        confirmPassword.addEventListener('blur', validateFields);
        phoneNumber.addEventListener('blur', validateFields);
        address.addEventListener('blur', validateFields);
        age.addEventListener('blur', validateFields);
        payRate.addEventListener('blur', validateFields);
        specialty.addEventListener('blur', validateFields);

        validateFields();

    });
       