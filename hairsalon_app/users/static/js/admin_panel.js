document.addEventListener("DOMContentLoaded", function () {
    const menuItems = document.querySelectorAll('#adminnav-menu li');
    const contentSections = document.querySelectorAll('.content');

    menuItems.forEach((menuItem, index) => {
        menuItem.addEventListener('click', () => {
            // Remove 'active' class from all menu items
            menuItems.forEach(item => item.classList.remove('active'));
            // Add 'active' class to the clicked menu item
            menuItem.classList.add('active');

            // Hide all content sections
            contentSections.forEach(section => section.classList.remove('active'));
            // Show the corresponding content section based on the index
            contentSections[index].classList.add('active');
        });
    });

    // Intercept form submissions
    document.querySelectorAll('.access form').forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission behavior

            const td = form.parentElement;
            const button = form.querySelector('input[type="submit"]');

            // Toggle button value and class
            if (button.value === 'Activated') {
                button.value = 'Deactivated';
                td.classList.remove('access');
                td.classList.add('access', 'deactivated');
            } else {
                button.value = 'Activated';
                td.classList.remove('access', 'deactivated');
                td.classList.add('access');
            }

            // Submit the form asynchronously
            fetch(form.action, {
                method: 'POST',
                body: new FormData(form)
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
            }).catch(error => {
                console.error('Error submitting form:', error);
            });
        });
    });
});
