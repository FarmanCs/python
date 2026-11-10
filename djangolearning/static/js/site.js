document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".nav-toggle");
  const menu = document.querySelector(".main-nav");

  if (menuButton && menu) {
    menuButton.addEventListener("click", () => {
      const isExpanded = menuButton.getAttribute("aria-expanded") === "true";
      menuButton.setAttribute("aria-expanded", String(!isExpanded));
      menu.classList.toggle("is-open", !isExpanded);
    });

    menu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        menuButton.setAttribute("aria-expanded", "false");
        menu.classList.remove("is-open");
      });
    });

    window.addEventListener("resize", () => {
      if (window.matchMedia("(min-width: 701px)").matches) {
        menuButton.setAttribute("aria-expanded", "false");
        menu.classList.remove("is-open");
      }
    });
  }

  document.querySelectorAll("[data-current-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const contactForm = document.querySelector("[data-contact-form]");
  const formMessage = document.querySelector("[data-form-message]");

  if (contactForm && formMessage) {
    contactForm.addEventListener("submit", (event) => {
      event.preventDefault();
      formMessage.textContent = "Your message was not sent. This form is not connected to a message service yet.";
    });
  }
});
