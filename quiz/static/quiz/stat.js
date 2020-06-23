let msg = document.querySelector(".message"),
    buton = document.querySelector("#button"),
    hbutton = document.querySelector(".hbutt"),
    harea = document.querySelector(".hint");

hbutton.addEventListener("click", points);

function points() {
    let r = window.confirm(
        "you will loose ponits \n are u sure \n u want to continue"
    );
    if (r == true) {
        harea.style.backgroundColor = "red";
        harea.style.color = "yellow";
        harea.style.fontFamily = "Roboto";
        harea.style.fontSize = "1.3em";
        harea.innerHTML = `You have lost some points \n your hint is \n
      {{question.hint}}`;
    } else {
        buton.addEventListener("click", show);

        function show() {
            msg.innerHTML = "your answer is submitted ";
            msg.style.backgroundColor = "red";
        }
    }
}