document.addEventListener("DOMContentLoaded", async function () {

    // get the profile data from the API 
    const token = localStorage.getItem("authToken");
    const response = await fetch("/api/user/", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        }
    });
    const profile = await response.json();

    // update the user profile's detail
    document.querySelector("#username").textContent = profile.username;
    document.querySelector("#email").textContent = profile.email;
    document.querySelector("#full-name").textContent = `${profile.first_name} ${profile.last_name}`;

    // if user had profile img, put the url in the img src
    const img_url = profile.profile_image;
    if (img_url) {
        document.querySelector("#profile-img").src = img_url;
    } 

    const imgForm = document.querySelector("#upload-img-form");
    imgForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        let profileImage = imgForm.querySelector("#profile_image").files[0];

        if(!profileImage) {
            showFailModal("Please provide the image file.");
            return;
        }

        const formData = new FormData();
        formData.append("profile_img", profileImage);

        try {
            const response = await fetch("/api/profile/", {
                method: "PATCH",
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem("authToken")}`,
                },
                body: formData,
            });

            if (response.ok) {
                // reload profile page
                window.location.href = "/profile/";
            }  else {
                new bootstrap.Modal(document.querySelector("#FailModal")).show();
            }   

        } catch (error) {
            new bootstrap.Modal(document.querySelector("#FailModal")).show();
        }
    });
});
