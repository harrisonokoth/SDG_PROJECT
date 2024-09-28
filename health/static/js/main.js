$(document).ready(function() {
    // Show the toast on form submission (for demonstration purposes)
    $('form').on('submit', function(event) {
        event.preventDefault();
        // Assuming you would handle form submission here
        $('#successToast').toast('show');
        // Optionally submit the form here
        // this.submit();
    });

    // Example validation for the form
    (function() {
        'use strict';
        var forms = document.querySelectorAll('.needs-validation');
        Array.prototype.slice.call(forms)
            .forEach(function(form) {
                form.addEventListener('submit', function(event) {
                    if (!form.checkValidity()) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
    })();
});
