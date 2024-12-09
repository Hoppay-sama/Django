function changeImage(phones) {
    const mainImage = document.getElementById('mainImage');
    mainImage.src = phones.src; 
}

function selectOption(categoryId, selectedOption) {
    
    const container = document.getElementById(categoryId);

    const options = container.getElementsByClassName('option');
        for (let option of options) {
            option.classList.remove('active');
        }

    selectedOption.classList.add('active');

    const paymentSection = document.getElementById('payment-options');
    if (selectedOption.classList.contains('yes')) {
        paymentSection.style.display = 'none';
    } else if (selectedOption.classList.contains('no')){
        paymentSection.style.display = 'block';
    }
}

const colorCircles = document.querySelectorAll('.color-circle');
colorCircles.forEach((circle) => {
  const color = circle.getAttribute('data-color');
  circle.style.backgroundColor = color;
});

