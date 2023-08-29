var swiper = new Swiper(".mySwiper", {
      grabCursor: true,
      effect: "coverflow",
      speed: 800,
      loop: true,
      autoplay: {
        delay: 4000,
        disableOnInteraction: false,
      },
      creativeEffect: {
        prev: {
          shadow: true,
          translate: [0, 0, -400],
        },
        next: {
          translate: ["100%", 0, 0],
        },
      },
    });