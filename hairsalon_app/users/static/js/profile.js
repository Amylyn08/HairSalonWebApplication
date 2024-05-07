document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('hoverButton');
    const hiddenElement = document.getElementById('hoverElement');

    button.addEventListener('mouseenter', (event) => {
        hiddenElement.style.visibility = 'visible';
    });

    button.addEventListener('mouseleave', (event) => {
        hiddenElement.style.visibility = 'hidden';
    });
});