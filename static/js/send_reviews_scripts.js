// JS код для Swiper
var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 300,
      modifier: 1,
      slideShadows: false,
    },
    pagination: {
      el: ".swiper-pagination",
    },
  });
  
  // JS код для оценки
  document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll(".rating span");
    const ratingInput = document.getElementById("rating-input");
  
    stars.forEach((star, index) => {
      star.addEventListener("click", function () {
        stars.forEach((s, i) => {
          if (i <= index) {
            s.classList.add("active");
          } else {
            s.classList.remove("active");
          }
        });
        ratingInput.value = index + 1; // Устанавливаем значение рейтинга
      });
  
      star.addEventListener("mouseover", function () {
        stars.forEach((s, i) => {
          if (i <= index) {
            s.classList.add("hover");
          } else {
            s.classList.remove("hover");
          }
        });
      });
  
      star.addEventListener("mouseout", function () {
        stars.forEach((s) => {
          s.classList.remove("hover");
        });
      });
    });
  
    if (!ratingInput.value) {
      ratingInput.value = 0;
    }
  });
  