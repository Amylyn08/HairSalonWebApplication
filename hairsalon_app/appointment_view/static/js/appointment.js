"use strict";

document.addEventListener("DOMContentLoaded", function(e){
    const date = document.getElementById('date');
    const messageParagraph = document.createElement('p');
    messageParagraph.textContent = 'Please select a date';
    messageParagraph.style.color = 'red';
    messageParagraph.style.fontSize = '13px';

    function validateDate() {
        if (date.value === '') {
            date.style.borderColor = "red";
            date.style.boxShadow = "0 0 5px red";
            date.setCustomValidity("Please select a date");

            // Append the message paragraph after the date field
            if (!date.parentNode.contains(messageParagraph)) {
                date.parentNode.insertBefore(messageParagraph, date.nextSibling);
            }
        } else {
            date.style.borderColor = ""; // Reset border color
            date.style.boxShadow = ""; // Reset box shadow
            date.setCustomValidity("");

            // Remove the message paragraph if it exists
            if (messageParagraph && messageParagraph.parentNode === date.parentNode) {
                date.parentNode.removeChild(messageParagraph);
            }
        }
    }

    validateDate(date);

    // Listen for input event
    date.addEventListener('input', validateDate);

    // Listen for blur event
    date.addEventListener('blur', validateDate);
});
