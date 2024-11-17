
function goToItemDetail(itemId, itemName, itemPrice, itemDescription) {
    const url = `item-detail.html?name=${encodeURIComponent(itemName)}&price=${encodeURIComponent(itemPrice)}&description=${encodeURIComponent(itemDescription)}`;
    window.location.href = url;
}

window.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.clothing-item');
    items.forEach(item => {
        const itemId = item.getAttribute('data-id');
        const itemName = item.querySelector('.card-title').innerText;
        const itemPrice = item.getAttribute('data-price');
        const itemDescription = item.getAttribute('data-description');

        item.addEventListener('click', () => goToItemDetail(itemId, itemName, itemPrice, itemDescription));
    });

    loadItemDetails();
});

function loadItemDetails() {
    const urlParams = new URLSearchParams(window.location.search);
    const itemName = urlParams.get('name');
    const itemPrice = urlParams.get('price');
    const itemDescription = urlParams.get('description');

    if (document.getElementById('item-name')) {
        document.getElementById('item-name').innerText = itemName || "Item not found";
        document.getElementById('item-price').innerText = `Price: ${itemPrice || "N/A"}`;
        document.getElementById('item-description').innerText = itemDescription || "No description available.";
    }
}



