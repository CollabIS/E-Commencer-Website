document.addEventListener('DOMContentLoaded', function () {
        const menuIcon = document.querySelector('.menu');
        const sidebar = document.querySelector('.side-bar-container');

        function showSidebar() {
        sidebar.style.transform = 'translateX(0)';
        }

        function hideSidebar() {
        sidebar.style.transform = 'translateX(-180px)';
        sidebar.style.padding = '0';
        }

        // Hide sidebar at the start of the page
        hideSidebar('mouseout', hideSidebar);

        // Add event listeners
        menuIcon.addEventListener('mouseover', showSidebar);
        menuIcon.addEventListener('mouseout', hideSidebar);
        sidebar.addEventListener('mouseover', showSidebar);
        sidebar.addEventListener('mouseout', hideSidebar);
    });