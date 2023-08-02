
    function showTab(tabName) {
        var tabs = document.getElementsByClassName("tab-pane");
        for (var i = 0; i < tabs.length; i++) {
            tabs[i].style.display = "none";
        }
        document.getElementById(tabName).style.display = "block";

        // Remove the "active" class from all tabs
        var navItems = document.getElementsByClassName("nav-item");
        for (var i = 0; i < navItems.length; i++) {
            navItems[i].classList.remove("active");
        }

        // Add the "active" class to the clicked tab
        var activeTab = document.querySelector('a[href="#' + tabName + '"]');
        activeTab.parentElement.classList.add("active");
    }

    function toggleButtonText(input) {
        const button = document.getElementById('profil-submit-button');
        if (input.files.length > 0) {
            button.style.display = 'block';
        } else {
            button.style.display = 'none';
        }
    }
