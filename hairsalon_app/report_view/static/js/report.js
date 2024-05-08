"use strict";

document.addEventListener("DOMContentLoaded", function (e) {
    const title = document.getElementById('title');
    const errorMsg = document.createElement('p');
    errorMsg.textContent = "Required a title";
    errorMsg.style.color = "red";
    errorMsg.style.fontSize = "12px";

    function validateTitle() {
        if (title.value === "") {
            title.style.borderColor = "red";
            title.style.boxShadow = "0 0 5px red";
            title.setCustomValidity("Required a title");

            if (!title.parentNode.contains(errorMsg)) {
                title.parentNode.insertBefore(errorMsg, title.nextSibling);
            }
        } else {
            title.style.borderColor = "";
            title.style.boxShadow = "";
            title.setCustomValidity("");

            if (errorMsg && errorMsg.parentNode === title.parentNode) {
                title.parentNode.removeChild(errorMsg);
            }
        }
    }

    // Listen for input event
    title.addEventListener('input', validateTitle);

    // Listen for blur event
    title.addEventListener('blur', validateTitle);
});
