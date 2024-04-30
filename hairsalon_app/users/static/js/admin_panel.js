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

});
