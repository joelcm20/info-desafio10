const counter = document.querySelector(".counter");
const num = document.querySelector(".counter strong")

num.append(0)

let init = 0;

counter.addEventListener("click", () => {
    init++
    num.removeChild(num.firstChild)
    num.append(init)
});