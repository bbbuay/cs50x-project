document.addEventListener("DOMContentLoaded", function (){
    // get the register form element
    const registerForm = document.querySelector("#register-form");

    registerForm.addEventListener("submit", function(e){
        e.preventDefault();

        const registerData = {
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
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify(registerData), // convert the data to JSON
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}