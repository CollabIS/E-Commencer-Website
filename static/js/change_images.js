var i = 0;
var prevHeart;
var autoChangeInterval;

var urlsImages = [
    "https://mensflair.com/wp-content/uploads/2022/07/90s-mens-fashion-2.jpg",
    "https://assets.gqindia.com/photos/60ae4e6e6a698dd23ccd17fc/16:9/w_2560%2Cc_limit/final-top-image.jpg",
    "https://www.lux-review.com/wp-content/uploads/2022/03/Y2K-Fashion.jpg",
    "https://porc.netcdn.ro/media/mageing/slider/slideritem/l/a/landing_19092023-min.jpg"
];

var hearts;

function changeImageAuto() {
    var bdy = document.body;
    bdy.style.transition = "background-image 0.5s ease";
    bdy.style.backgroundImage = "url(" + urlsImages[i] + ")";

    if (prevHeart) {
        prevHeart.classList.replace("fa-solid", "fa-regular");
    }

    hearts[i].classList.replace("fa-regular", "fa-solid");

    prevHeart = hearts[i];
    i = (i + 1) % urlsImages.length;
}

document.addEventListener("DOMContentLoaded", function () {
    // Get hearts after the DOM has fully loaded
    hearts = document.getElementsByClassName("fa-heart");

    // Set initial background image
    document.body.style.backgroundImage = "url(" + urlsImages[i] + ")";

    // Start the interval after the DOM has fully loaded
    autoChangeInterval = setInterval(changeImageAuto, 2000);
});
