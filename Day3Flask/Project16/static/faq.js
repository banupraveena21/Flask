// Simple JS toggle fallback (optional, Bootstrap 5 handles this already)
document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".accordion-button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const collapse = button.closest(".accordion-item").querySelector(".accordion-collapse");
      collapse.classList.toggle("show");
    });
  });
});
