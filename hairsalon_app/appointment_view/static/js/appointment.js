"use strict";

document.addEventListener("DOMContentLoaded", function(e){
    const date = document.getElementById('date');
    console.log(date.value);
    if (date.value === '') {
        console.log("here");
        date.style.borderColor = "red";
        date.style.boxShadow = "0 0 5px red";
        date.setCustomValidity("Please select a date");
    } else {
        date.style.borderColor = ""; // Reset border color
        date.style.boxShadow = ""; // Reset box shadow
        date.setCustomValidity("");
    }
});