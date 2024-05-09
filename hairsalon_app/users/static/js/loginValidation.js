"use strict";

document.addEventListener("DOMContentLoaded", function (e) {
    const username = document.querySelector("#username");
    const password = document.querySelector("#password");

    function validateFields() {
        validateField(username);
        validateField(password);
    }

    function validateField(field){
        const errorMessageId = `${field.id}-error`;
        let errorMessageElement = document.getElementById(errorMessageId);

        if(field.value.trim() === ""){
            field.style.borderColor = "red";
            field.style.boxShadow = "0 0 5px red";
            field.setCustomValidity("This field is required");
            
            // Create error message element if not exists
            if (!errorMessageElement) {
                errorMessageElement = document.createElement("p");
                errorMessageElement.id = errorMessageId;
                errorMessageElement.style.color = "red";
                errorMessageElement.textContent = "This field is required";
                field.parentNode.insertBefore(errorMessageElement, field.nextSibling);
            }
        }
        else{
            field.style.borderColor = "";
            field.style.boxShadow = "";
            field.setCustomValidity("");
            
            // Remove error message element if exists
            if (errorMessageElement) {
                errorMessageElement.parentNode.removeChild(errorMessageElement);
            }
        }
    }
        
    username.addEventListener('input', validateFields);
    username.addEventListener('blur', validateFields);
    password.addEventListener('input', validateFields);
    password.addEventListener('blur', validateFields);

    validateFields();
});
