gsap.from("html", {
  "--myvar": "pink",
  duration: 1,
  yoyo: true,
  repeat: -1,
});

tls = gsap.timeline({ default: { duration: 1 } });

tls
  .fromTo("#particles-js", { x: "500", opacity: 0 }, { x: "0", opacity: 1 })
  .fromTo("header", { x: "-500", opacity: 0 }, { x: "0", opacity: 1 })
  .from("#message", { y: -200, opacity: 0, ease: "bounce" })
  .fromTo(
    "#message",
    { borderTopColor: "rgba(0, 0, 0, 0)" },
    { borderTopColor: "white", repeat: -1, repeatDelay: 1, yoyo: true }
  )
  .fromTo(
    "#message",
    { borderRightColor: "rgba(0, 0, 0, 0)" },
    { borderRightColor: "pink", repeat: -1, repeatDelay: 1, yoyo: true }
  )
  .fromTo(
    "#message",
    { borderBottomColor: "rgba(0, 0, 0, 0)" },
    { borderBottomColor: "red", repeat: -1, repeatDelay: 1, yoyo: true }
  )
  .fromTo(
    "#message",
    { borderLeftColor: "rgba(0, 0, 0, 0)" },
    { borderLeftColor: "brown", repeat: -1, repeatDelay: 1, yoyo: true }
  );

/// cursor effects
let mouseCursor = document.querySelector(".cursor");
let navLinks = document.querySelectorAll(".nav-bar li");

window.addEventListener("mousemove", cursor);

function cursor(e) {
  mouseCursor.style.top = e.pageY + "px";
  mouseCursor.style.left = e.pageX + "px";
}

// navLinks.forEach((link) => {
//   link.addEventListener("mouseover", () => {
//     mouseCursor.classList.add("link-grow");
//   });
//   link.addEventListener("mouseleave", () => {
//     mouseCursor.classList.remove("link-grow");
//   });
// });
