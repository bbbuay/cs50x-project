document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector("#login-form");

    loginForm.addEventListener("submit", async function(e) {
        e.preventDefault();

        const loginData = {
            username: loginForm.querySelector("#username").value,
            password: loginForm.querySelector("#password").value,
        }

        // Login User
        const response = await fetch("/api/token/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify(loginData),
        });


        if (response.ok) {
            // Save the access token to local storage
            const data = await response.json()
            localStorage.setItem("authToken", data.access);

            // Redirect to home page
            window.location.href = "/";
        } else {
            // Notification Modal for Login Error
            new bootstrap.Modal(document.querySelector("#FailModal")).show()
        }

    });
});


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