
  document.addEventListener("DOMContentLoaded", function () {
    const section = document.querySelector("#modalBox");
    section.classList.add("active");
    const overlay = document.querySelector(".overlay");
    const closeBtn = document.querySelector(".close-btn");
  
    document.querySelector(".show-modal").addEventListener("click", function () {
      section.classList.add("active");
    });
  
    overlay.addEventListener("click", function () {
      section.classList.remove("active");
    });
  
    closeBtn.addEventListener("click", function () {
      section.classList.remove("active");
    });
  });
  

  

