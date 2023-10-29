function updateBio() {
    const form = document.getElementById("bioForm");
    const formData = new FormData(form);

    fetch("{% url 'user_profile_page:update_bio_ajax' %}", {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: formData,
    })
    .then(response => response.text())  // Get the new bio from the response
    .then(bio => {
        if (bio) {
            document.getElementById("bioContent").innerHTML = `<strong>${bio}</strong>`;  // Update the bio in the DOM
            $('#editBioModal').modal('hide');  // Hide the modal
        } else {
            throw new Error("Failed to update bio");
        }
    })
    .catch(error => console.error("Error:", error));
}


// Function to get CSRF token from cookies
function getCookie(name) {
    var value = "; " + document.cookie;
    var parts = value.split("; " + name + "=");
    if (parts.length === 2) return parts.pop().split(";").shift();
}

document.getElementById("editBioButton").addEventListener("click", () => {
    document.getElementById("form").reset();
    const bioTextarea = document.getElementById("bioTextarea");
    bioTextarea.value = document.getElementById("bioContent").textContent;
});