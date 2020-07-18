let mouseCursor = document.querySelector(".cursor");
let navLinks = document.querySelectorAll(".nav_head li");

window.addEventListener("mousemove", cursor);

let rule = document.querySelector(".rules"),
    btnrule = document.querySelector(".rulebtn");

function cursor(e) {
    mouseCursor.style.top = e.pageY + "px";
    mouseCursor.style.left = e.pageX + "px";
}

navLinks.forEach((link) => {
    link.addEventListener("mouseover", () => {
        mouseCursor.classList.add("link-grow");
    });
    link.addEventListener("mouseleave", () => {
        mouseCursor.classList.remove("link-grow");
    });
});

let tl2 = gsap.timeline({ default: { duration: 1.22 } });

tl2
    .fromTo(".veil", { height: "100%" }, { height: "0" })
    .fromTo(".container", { x: "-500", opacity: 0 }, { x: "0", opacity: 1 })
    .fromTo("header", { x: "500", opacity: 0 }, { x: "0", opacity: 1 })
    .fromTo(
        ".nonauth",
        { height: "0", opacity: 0 },
        { height: "100%", opacity: 1 }
    )
    .fromTo(
        ".content",
        { width: "0", opacity: 0 },
        { width: "40%", opacity: 1 }
    )
    .from(".texthead", {
        opacity: 0,
        y: -100,
        ease: "bounce",
        stagger: 0.6,
    })
    .from(".box-text1", {
        opacity: 0,
        x: 100,
        ease: "rough",
    })
    .from(".dare", {
        opacity: 0,
        y: -100,
        ease: "power2.out",
    }).from(".socialLogin", {
        opacity: 0,
        y: 100,
        ease: "power2.out",
    });



btnrule.addEventListener("click", showrules);
function showrules() {
    let tlr = gsap.timeline({ default: { duraration: 1, } });

    tlr.to(".details", { opacity: 0, pointerEvents: "none" })
        .to(".rules", { opacity: 1, pointerEvents: "all" });
}

