console.log("El archivo JavaScript está conectado correctamente.");
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the default way


    // Get the form values
    

    // Obtén el formulario completo
    const form = event.target; 
    const category = form.elements.category.value;
    const name = form.elements.name.value;
    const price = form.elements.price.value;
    const amount = form.elements.amount.value;
    const photoInput = form.elements.photo;

    if (photoInput.files.length === 0) {
        alert('Por favor, selecciona una imagen.');
        return;
    }

    const lettersPattern = /^[A-Za-z\s]+$/;
    const allowedExtensions = ['jpg', 'jpeg', 'png','webp'];
    const fileName = photoInput.files[0].name.toLowerCase();
    const fileExtension = fileName.split('.').pop();
    if (!allowedExtensions.includes(fileExtension)) {
        alert('Por favor, selecciona un archivo de imagen válido (JPEG , PNG o WEBP).');
        return;
    }
    


    if (category === '' || !lettersPattern.test(category)) {
        alert('Por favor, ingresa una categoria valida (solo letras y espacios).');
        return;
    }
    
    if (name === '' || !/^[A-Za-z\d\s]+$/.test(name)) {
        alert('Por favor, ingresa un nombre valido (solo letras y espacios).');
        return;
    }

    if (price === '' || !/^\d+$/.test(price)) {
        alert('Por favor, ingresa un precio valido (solo números).');
        return;
    }

    if (amount === '' || !/^\d+$/.test(amount)) {
        alert('Por favor, ingresa una cantidad valida (solo números).');
        return;
    }

    document.querySelector('.registro button').addEventListener('click', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada

        const category = document.getElementById('category').value;
        const name = document.getElementById('name').value;
        const price = document.getElementById('price').value;
        const amount = document.getElementById('amount').value;
        const photoInput = document.getElementById('photo');

        if (category === '' || name === '' || price === '' || amount === '' || photoInput === '') {
            alert('Por favor, completa todos los campos antes de registrar.');
            return; // Evita enviar el formulario al servidor
        }

        // Si todas las condiciones se cumplen, envía el formulario al servidor
        document.getElementById('contactForm').submit();
        alert('Registro completo');
    });

    
    document.querySelector('.volver button').addEventListener('click', function() {
        window.location.href = '{{ url_for("index") }}';
    });

    
})
    
        
    
    
    





