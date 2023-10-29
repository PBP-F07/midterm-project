$(document).ready(function () {
    var selectedBook = null;

    $(".add-to-wishlist-form").submit(function (event) {
        event.preventDefault();
        var form = $(this);
        selectedBook = form.closest('.card');
        $('#confirmationModal').modal('show');
    });

    $("#cancelAddToWishlist").click(function () {
        $('#confirmationModal').modal('hide');
    });

    $("#confirmAddToWishlist").click(function () {
        ajaxAddToWishlist(selectedBook);
    });
});

function ajaxAddToWishlist(selectedBook) {
    $.ajax({
        url: "{% url 'wishlist_page:add_to_wishlist' %}",
        method: "POST",
        data: selectedBook.find('.add-to-wishlist-form').serialize(),
        success: function (response) {
            $(".success-message").html("Book added to your wishlist!");
            $(".success-message").show();

            selectedBook.remove();
            refreshWishlist();
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });
    $('#confirmationModal').modal('hide');
}

async function refreshWishlist() {
    try {
        const response = await fetch("{% url 'wishlist_page:load_wishlist' %}");
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
                const data = await response.json();
                const wishlistData = data.wishlist;

                document.getElementById("wishlist-table").innerHTML = "";
                let htmlString = `
                    <tr>
                        <th>No.</th>
                        <th>Judul</th>
                        <th>Status</th>
                        <th>Aksi</th>
                    </tr>
                `;

            wishlistData.forEach((item, index) => {
                console.log(wishlistData)
                htmlString += `
                    <tr>
                        <td>${index + 1}</td>
                        <td>${item.title}</td>
                        <td>${item.status}</td>
                        <td><button type="button" class="btn btn-danger" onclick="deleteProduct(${item.id})">hapus</button></td>
                    </tr>
                `;
            });

            document.getElementById("wishlist-table").innerHTML = htmlString;
        } catch (error) {
            console.error('Error refreshing wishlist:', error);
            // Handle the error, e.g., display an error message to the user
        }
    }

    refreshWishlist()
            
function deleteProduct(itemId) {
        var myModal = new bootstrap.Modal(document.getElementById('confirmRemoveModal'));
        myModal.show();

        document.getElementById("confirmDeleteBtn").addEventListener("click", function() {
    fetch(`delete-item-ajax/${itemId}/`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": document.querySelector('input[name="csrfmiddlewaretoken"]').value,
        },
    })
            .then(refreshWishlist);

            myModal.hide();
        });
    }