async function getWishlistedBooks() {
    return fetch("{% url 'user_profile_page:get_wishlisted_books_json' %}").then((res) => res.json())
}

async function getBorrowedBooks() {
    return fetch("{% url 'user_profile_page:get_borrowed_books_json' %}").then((res) => res.json())
}



async function refreshWishlistedBooks() {
    const cardContainer = document.getElementById("wishlisted_books");
    cardContainer.innerHTML = "";
    const books = await getWishlistedBooks();

    const row = document.createElement("div");
    row.className = "card-row"; // A new class for flexbox container

    books.forEach((book) => {
        const card = document.createElement("div");
        card.className = "card border-dark mb-3";

        card.innerHTML = `
            <img src="${book.fields.image}" class="card-img-top" alt="${book.fields.title}">
            <div class="card-body">
                <h5 class="card-title">${book.fields.title}</h5>
                <p class="card-text"><strong>Author:</strong> ${book.fields.author}</p>
            </div>
        `;

        row.appendChild(card); // Append the card to the row
    });

    cardContainer.appendChild(row); // Append the row to the main container
}

async function refreshBorrowedBooks() {
    const cardContainer = document.getElementById("borrowed_books");
    cardContainer.innerHTML = "";
    const books = await getBorrowedBooks();

    const row = document.createElement("div");
    row.className = "card-row"; // A new class for flexbox container

    books.forEach((book) => {
        const card = document.createElement("div");
        card.className = "card border-dark mb-3";

        card.innerHTML = `
            <img src="${book.fields.image}" class="card-img-top" alt="${book.fields.title}">
            <div class="card-body">
                <h5 class="card-title">${book.fields.title}</h5>
                <p class="card-text"><strong>Author:</strong> ${book.fields.author}</p>
                <p class="card-text"><strong>Return Date:</strong> ${book.fields.return_date}</p>
                <button class="return-button" data-toggle="modal" data-target="#returnModal" id="returnButton" onclick="returnBook(${book.pk})">
                    Return
                </button>
                
            </div>
        `;

        row.appendChild(card); // Append the card to the row
    });

    cardContainer.appendChild(row); // Append the row to the main container
}



refreshBorrowedBooks()
refreshWishlistedBooks()


function returnBook(bookId) {
    fetch(`/user_profile_page/return_book/${bookId}/`, {
                method: 'POST',
            })
            .then(response => {
                if (response.ok) {
                alert('Book returned successfully');
                refreshBorrowedBooks();
                } else {
                alert(result.message);
                }
            });
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