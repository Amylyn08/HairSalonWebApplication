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
            if (menuItem.textContent == "Clients"){
                contentSections[0].classList.add('active');
            }
            if (menuItem.textContent == "Employees"){
                contentSections[1].classList.add('active');
            }
            if (menuItem.textContent == "Appointments"){
                contentSections[2].classList.add('active');
            }
            if (menuItem.textContent == "Logs"){
                contentSections[3].classList.add('active');
            }
        });
    });

    document.querySelectorAll('.access button').forEach(td =>{
        td.addEventListener('click', function(e){
            const buttonAnchor = td.querySelector('button').querySelector('a');

            if(buttonAnchor.textContent == 'Activated'){
                buttonAnchor.textContent = 'Deactivated';
                td.classList.add('deactivated');
            }
            else{
                buttonAnchor.textContent = 'Activated';
                td.classList.remove('deactivated');
            }
        })
    })

    document.querySelectorAll('.flag button').forEach(td =>{
        td.addEventListener('click', function(e){
            const buttonAnchor = td.querySelector('button').querySelector('a');
            if(buttonAnchor.textContent == 'Unflagged'){
                buttonAnchor.textContent = 'Flagged';
                td.classList.add('flagged');
            }
            else{
                buttonAnchor.textContent = 'Unflagged';
                td.classList.remove('flagged');
            }
        });
    });

    const userTypeSelect = document.getElementById("user-create");
    const nonProDiv = document.getElementById("non-client-fields");
    userTypeSelect.addEventListener("change", function() {
        if (userTypeSelect.value === "client") {
            nonProDiv.style.display = "none";
        } else {
            nonProDiv.style.display = "block";
        }
    });

   
});
