document.getElementById("blurb-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const blurb = document.getElementById("blurb").value;
    const resultsContainer = document.getElementById("results");
    const submitButton = document.querySelector(".submit-button");
    const buttonLoader = document.querySelector(".button-loader");


   // Show loading spinner and disable the button
   buttonLoader.style.display = "inline-block";
   submitButton.disabled = true;
   resultsContainer.classList.remove("active");


    fetch("/recommend-books/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: `blurb=${encodeURIComponent(blurb)}`,
    })
        .then((response) => response.json())
        .then((data) => {
           resultsContainer.innerHTML = "";
            if (Array.isArray(data)) {
                data.forEach((rec) => {
                    const result = document.createElement("div");
                    result.classList.add("result-card");
                    // Dynamically add span to make the book title purple
                    result.innerHTML = `<h3><span style="color: purple;">${rec.book_original_title}</span></h3><p>${rec.book_desc}</p>`;
                    console.log(rec)
                    resultsContainer.appendChild(result);
                });
            } else {
                 const result = document.createElement("p");
                result.textContent=data;
                resultsContainer.appendChild(result)
             
            }
            // Show results and hide loading spinner
            resultsContainer.classList.add("active");
            buttonLoader.style.display = "none";
            submitButton.disabled = false;
        })
        .catch((error) => {
           console.error("Error:", error);
           resultsContainer.innerHTML = "<p>An error occurred, please try again.</p>";
           resultsContainer.classList.add("active");
           buttonLoader.style.display = "none";
            submitButton.disabled = false;
        });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}