document.addEventListener('DOMContentLoaded', () => {
    const scrollingText = document.querySelector('.scrolling-text');

    // Function to show the scrolling text
    function showScrollingText() {
        scrollingText.style.left = '-100%'; // Start off screen to the left
        scrollingText.style.display = 'block'; // Display the scrolling text
        scrollingText.style.animation = 'scrollText 10s linear infinite'; // Apply scroll animation
    }

    // Function to hide the scrolling text
    function hideScrollingText() {
        scrollingText.style.display = 'none'; // Hide the scrolling text
    }

    // Show the scrolling text when the page loads
    showScrollingText();

    // Toggle the visibility of the scrolling text on click
    scrollingText.addEventListener('click', () => {
        if (scrollingText.style.display === 'none') {
            showScrollingText(); // Show the scrolling text
        } else {
            hideScrollingText(); // Hide the scrolling text
        }
    });
});