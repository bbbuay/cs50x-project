document.addEventListener("DOMContentLoaded", function (){
    // get the register form element
    const registerForm = document.querySelector("#register-form");

    registerForm.addEventListener("submit", function(e){
        e.preventDefault();

        const register_data = {
            username: registerForm.querySelector("#username").value,
            email: registerForm.querySelector("#email").value,
            first_name: registerForm.querySelector("#first_name").value,
            last_name: registerForm.querySelector("#last_name").value,
            password: registerForm.querySelector("#password").value,
            password_confirmation: registerForm.querySelector("#password_confirmation").value,
        };
        
        // send the data to the register api 
        fetch(registerForm.action, {
            method: registerForm.method,
            headers: {
                "Content-Type": "application/json" 
            },
            body: JSON.stringify(register_data), // convert the data to JSON
        })
        .then(response => {
            if (!response.ok){
                showFailRegisterModal();
            } else {
                showSuccessfulRegisterModal();
            }
        })
        
    });
});

function showSuccessfulRegisterModal() {
    new bootstrap.Modal(document.querySelector("#successfulModal")).show();
}

function showFailRegisterModal() {
    const failModal = document.querySelector("#FailModal");

    // Add the error message to modal body
    const body = failModal.querySelector(".modal-body");
    body.textContent = "Registration failed. Please try again."

    // Show Modal
    new bootstrap.Modal(failModal).show()
}
