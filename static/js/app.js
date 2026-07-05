// =========================================
// AI Productivity Tool
// Minimal JavaScript
// =========================================

// Confirm before deleting a task
document.addEventListener("DOMContentLoaded", function () {

    const deleteButtons = document.querySelectorAll(
        'a[href*="/delete/"]'
    );

    deleteButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const confirmed = confirm(
                "Are you sure you want to delete this task?"
            );

            if (!confirmed) {
                event.preventDefault();
            }

        });

    });

});