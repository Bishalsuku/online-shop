//slider
const slides = document.querySelector(".slider").children;
const trending = document.querySelectorAll(".slide");
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const indicator = document.querySelector(".indicator");
let index = 0;

trending[0].classList.add("active");
prev.addEventListener("click", function () {
  prevSlide();
  updateCircleIndicator();
  resetTimer();
});

next.addEventListener("click", function () {
  nextSlide();
  updateCircleIndicator();
  resetTimer();
});

// create circle indicators
function circleIndicator() {
  for (let i = 0; i < slides.length; i++) {
    const div = document.createElement("div");
    div.innerHTML = i + 1;
    div.setAttribute("onclick", "indicateSlide(this)");
    div.id = i;
    if (i == 0) {
      div.className = "active";
    }
    indicator.appendChild(div);
  }
}
circleIndicator();

function indicateSlide(element) {
  index = element.id;
  changeSlide();
  updateCircleIndicator();
  resetTimer();
}

function updateCircleIndicator() {
  for (let i = 0; i < indicator.children.length; i++) {
    indicator.children[i].classList.remove("active");
  }
  indicator.children[index].classList.add("active");
}

function prevSlide() {
  if (index == 0) {
    index = trending.length - 1;
  } else {
    index--;
  }
  changeSlide();
}

function nextSlide() {
  if (index == trending.length - 1) {
    index = 0;
  } else {
    index++;
  }
  changeSlide();
}

function changeSlide() {
  for (let i = 0; i < trending.length; i++) {
    trending[i].classList.remove("active");
  }

  trending[index].classList.add("active");
}

function resetTimer() {
  // when click to indicator or controls button
  // stop timer
  clearInterval(timer);
  // then started again timer
  timer = setInterval(autoPlay, 4000);
}

function autoPlay() {
  nextSlide();
  updateCircleIndicator();
}

let timer = setInterval(autoPlay, 10000);

//contact
function check() {
  if (document.myForm.Name.value == "") {
    alert("Please provide your name!");
    document.myForm.Name.focus();
    return false;
  }
  var emailID = document.myForm.EMail.value;
  atpos = emailID.indexOf("@");
  dotpos = emailID.lastIndexOf(".");

  if (atpos < 1 || dotpos - atpos < 2) {
    alert("Please enter correct email ID");
    document.myForm.EMail.focus();
    return false;
  }
  return true;
}

function mySub() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}
