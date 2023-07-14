document.addEventListener('DOMContentLoaded', function() {
    var password2Input = document.getElementById('id_password2');
    var password1Input = document.getElementById('id_password1');
    var usernameInput = document.getElementById('id_username');
    var emailInput = document.getElementById('id_email');

    
    password2Input.placeholder = 'Şifre tekrarı';
    password1Input.placeholder = 'Şifre';
    usernameInput.placeholder = 'Kullanıcı adı';
    emailInput.placeholder = 'E-posta';
    
    
});
