document.addEventListener('DOMContentLoaded', function() { 
    var password1Input = document.getElementById('inputPassword1');
    var password2Input = document.getElementById('inputPassword2');

    password2Input.placeholder = 'Şifre tekrarı';
    password1Input.placeholder = 'Şifre';
    
});


document.addEventListener('DOMContentLoaded', function() {
    const ortalamaInput = document.getElementById('inputOrtalama');

    // Function to validate if the input value is a positive float number
    function validateOrtalama() {
      const ortalamaValue = parseFloat(ortalamaInput.value);
      if (isNaN(ortalamaValue) || ortalamaValue <= 0) {
        // Display error message
        document.getElementById('ortalamaError').textContent = 'Ortalamanız pozitif bir değer olmalıdır.';
        return false;
      } else {
        // Clear error message
        document.getElementById('ortalamaError').textContent = '';
        return true;
      }
    }

    // Function to prevent negative values and zero
    function preventNegativeValues(event) {
      const keyCode = event.keyCode || event.which;
      if (keyCode === 45 || keyCode === 43 || keyCode === 46 || keyCode === 101 || keyCode === 69) {
        event.preventDefault();
      }
    }

    // Add event listener for input changes
    ortalamaInput.addEventListener('input', validateOrtalama);

    // Add event listener for key press to prevent negative values and zero
    ortalamaInput.addEventListener('keypress', preventNegativeValues);
  });
