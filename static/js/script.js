document.addEventListener("DOMContentLoaded", function () {
  var controller = new ScrollMagic.Controller();

  const tl1 = gsap.timeline();
  tl1
//    .fromTo(
//      ".logo",
//      { opacity: 0, y: -50, scale: 0.5, rotation: -30 },
//      {
//        opacity: 1,
//        y: 0,
//        scale: 1,
//        rotation: 0,
//        duration: 2,
//        ease: "elastic.out(1, 0.5)",
//      }
//    )
//    .fromTo(
//      ".menu-title",
//      {
//        x: 100,
//        opacity: 0,
//      },
//      {
//        x: 0,
//        opacity: 1,
//      },
//      1
//    )
//    .fromTo(
//      ".menu-subTittle",
//      {
//        opacity: 0,
//        y: 50,
//      },
//      {
//        opacity: 1,
//        y: 0,
//      },
//      1.5
//    )
    .fromTo(
      ".bottom-image",
      {
        scale: 1,
        opacity: 1,
      },
      {
        scale: 1.1,
        opacity: 0.7,
        duration: 2,
        repeat: -1,
        yoyo: true,
        ease: "power1.inOut",
      }
    );
  new ScrollMagic.Scene({
    triggerElement: ".first-part",
    triggerHook: 0.7,
    reverse: true,
  })
    .setTween(tl1)
    .addTo(controller);

  const tl2 = gsap.timeline();

  tl2.fromTo(
    ".shadow-box",
    {
      opacity: 0,
      y: 50,
      stagger: 0.5,
      duration: 2,
    },
    {
      opacity: 1,
      y: 50,
      stagger: 0.2,
      duration: 2,
    }
  );

  new ScrollMagic.Scene({
    triggerElement: ".second-part",
    triggerHook: 0.6,
    reverse: true,
  })
    .setTween(tl2)
    .addTo(controller);
});
