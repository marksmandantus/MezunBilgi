$('#profilePhotoInput').change(function() {
    var file = this.files[0];
    var reader = new FileReader();

    reader.onloadend = function() {
        var newProfilePhoto = reader.result;
        $('#profilePhoto').attr('src', newProfilePhoto);
            // You can also use AJAX to upload the new profile photo to the server
            // and save it in the database.
        }
    if (file) {
        reader.readAsDataURL(file);
    }
    });

