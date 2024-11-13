document.addEventListener("DOMContentLoaded", async function (){
    const religionSelection = document.querySelector("#religion-selection");
    const religionButtons = religionSelection.querySelectorAll("button");
    const likeButton = document.querySelector("#like-button");
    const isLogin = isLoggedIn();
    
    // remove all selected class and add selected class to Buddhism button
    religionButtons.forEach(b => b.classList.remove("selected"));
    religionSelection.firstElementChild.classList.add("selected");

    // get the value from the selected button
    let selectedReligion = document.querySelector("#religion-selection .selected").value;
    let guidance_id = await updateGuidance(selectedReligion);

    // Display the text in likeButton 
    updateLikeButton(likeButton, guidance_id);

    //  Add event listener for the religion_buttons in the navigation bar
    religionButtons.forEach(button => {
        button.addEventListener("click", async function() {
            // remove `selected` for all buttons
            religionButtons.forEach(b => b.classList.remove("selected"));
            // set the `selected` class for the clicked button
            button.classList.add("selected");

            // updated the new random guidance
            selectedReligion = document.querySelector("#religion-selection .selected").value;
            guidance_id = await updateGuidance(selectedReligion);
            updateLikeButton(likeButton, guidance_id);
        });
    });

    // Add Click EventListener to Continue Random Guidance button
    randomButton = document.querySelector("#random-button");
    randomButton.addEventListener("click", async function () {
        // updated the new random guidance
        selectedReligion = document.querySelector("#religion-selection .selected").value;
        guidance_id = await updateGuidance(selectedReligion);
        updateLikeButton(likeButton, guidance_id);
    });

    // Add Click EventListener to Like button 
    likeButton.addEventListener("click", async function (){
        // if user's not login, open the error modal 
        if (!isLogin){
            new bootstrap.Modal(document.querySelector("#login-modal")).show()
            return;
        }

        const like_number = document.querySelector("#like-display span");

        if (likeButton.textContent === "Like") {
            // Update the user favorite using API 
            isLike = await likeGuidance(guidance_id);
            if (isLike) {
                // Update like amount display
                like_number.textContent = await getLikeAmount(guidance_id);
                // Change the textContent to be 'Unlike'
                likeButton.textContent = 'Unlike';
            }
          
        } else {
            // Update the user favorite using API 
            isUnlike = await unlikeGuidance(guidance_id);
            if (isUnlike) {
                // Update like amount display
                like_number.textContent = await getLikeAmount(guidance_id);
                // Change the textContent to be 'Unlike'
                likeButton.textContent = 'Like';
            }
        }     
    });
});

async function updateGuidance(religion) {
    // get all elements for updating data
    const title = document.querySelector("#title");
    const image = document.querySelector("#guidance-image");
    const content = document.querySelector("#content");
    const like_number = document.querySelector("#like-display span");

    // get the data from API and update content
    response = await fetch(`/api/guidances/random/?religion=${religion}`);
    guidance = await response.json()
    title.innerHTML = guidance.title;
    image.src = guidance.image;
    content.innerHTML = guidance.content;
    like_number.innerHTML = guidance.favorite_count;

    return await guidance.id;
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
            }
    })
    return response.ok
}

async function unlikeGuidance(id) {
    response = await fetch(`/api/guidances/${id}/unlike/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("authToken")}`,
            }
    })
    return response.ok
}

async function getFavGuidances() {
    const token = localStorage.getItem("authToken");
    response = await fetch(`/api/profile/`, {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        }
    })
    profile = await response.json()
    return profile.favorite_guidances
}

async function getLikeAmount(guidance_id) {
    const response = await fetch(`api/guidances/${guidance_id}/`);
    const guidance = await response.json();
    return guidance.favorite_count;
}

async function updateLikeButton(button, guidance_id){
    // If user not login: display `Like`
    if (!isLoggedIn()){
        button.textContent = "Like"
    } else {
        // if user like this Guidance, display `Unlike`, otherwise diplay `Like
        favorite_guidances = await getFavGuidances()
        if (favorite_guidances.includes(guidance_id)) {
            button.textContent = "Unlike"
        } else {
            button.textContent = "Like"
        }
    }
}