document.addEventListener("DOMContentLoaded", function (){
    const religionSelection = document.querySelector("#religion-selection");
    const religionButtons = religionSelection.querySelectorAll("button");
    const likeButton = document.querySelector("#like-button");
    const isLogin = isLoggedIn();

    // remove all selected class and add selected class to Buddhism button
    religionButtons.forEach(b => b.classList.remove("selected"));
    religionSelection.firstElementChild.classList.add("selected");

    // get the value from the selected button
    let selectedReligion = document.querySelector("#religion-selection .selected").value;
    let guidance_id = updateGuidance(selectedReligion);

    // Display the text in likeButton 
    // If user not login: display `Like`
    if (!isLogin){
        likeButton.textContent = "Like"
    } else {
        // if user like this Guidance, display `Unlike`, otherwise diplay `Like
        if (guidance_id in getFavGuidances()) {
            likeButton.textContent = "Unlike"
        } else {
            likeButton.textContent = "Like"
        }
    }

    //  Add event listener for the religion_buttons in the navigation bar
    religionButtons.forEach(button => {
        button.addEventListener("click", function() {
            // remove `selected` for all buttons
            religionButtons.forEach(b => b.classList.remove("selected"));
            // set the `selected` class for the clicked button
            button.classList.add("selected");

            // updated the new random guidance
            selectedReligion = document.querySelector("#religion-selection .selected").value;
            guidance_id = updateGuidance(selectedReligion);
        });
    });

    // Add Click EventListener to Continue Random Guidance button
    randomButton = document.querySelector("#random-button");
    randomButton.addEventListener("click", function () {
        // updated the new random guidance
        selectedReligion = document.querySelector("#religion-selection .selected").value;
        updateGuidance(selectedReligion);
    });

    // Add Click EventListener to Like button 
    likeButton.addEventListener("click", async function (){
        // if user's not login, open the error modal 
        if (!isLogin){
            new bootstrap.Modal(document.querySelector("#login-modal")).show()
            return;
        }

        if (likeButton.textContent === "Like") {
            // Update the user favorite using API 
            isLike = likeGuidance(guidance_id);
            if (isLike) {
                // Change the textContent to be 'Unlike'
                likeButton.textContent = 'Unlike';
            }
          
        } else {
            // Update the user favorite using API 
            isUnlike = unlikeGuidance(guidance_id);
            if (isUnlike) {
                // Change the textContent to be 'Unlike'
                likeButton.textContent = 'Like';
            }
        }     
    });
});

function updateGuidance(religion) {

    // get all elements for updating data
    const title = document.querySelector("#title");
    const image = document.querySelector("#guidance-image");
    const content = document.querySelector("#content");
    const like_number = document.querySelector("#like-display span");

    // get the data from api and update content
    fetch(`/api/guidances/random/?religion=${religion}`)
    .then(response => response.json())
    .then(guidance => {
        title.innerHTML = guidance.title;
        image.src = guidance.image;
        content.innerHTML = guidance.content;
        like_number.innerHTML = guidance.favorite_count;

        return guidance.id;
    });

}

function isLoggedIn() {
    return localStorage.getItem("authToken") !== null;
}

async function likeGuidance(id) {
    response = await fetch(`/api/guidances/${id}/like/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("authToken")}`,
            "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin"
    })
    return response.ok
}

async function unlikeGuidance(id) {
    response = await fetch(`/api/guidances/${id}/unlike/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("authToken")}`,
            "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin"
    })
    return response.ok
}

async function getFavGuidances() {
    response = await fetch(`/api/profile/`)
    profile = response.json()
    return profile.favorite_guidances
}