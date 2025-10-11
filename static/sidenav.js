document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll("#sidenav a");

  window.addEventListener("scroll", () => {
    let current = "";
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 200;
      if (scrollY >= sectionTop) current = section.getAttribute("id");
    });

    navLinks.forEach((link) => {
      link.classList.remove("active");
      if (link.getAttribute("href") === "#" + current) {
        link.classList.add("active");
      }
    });
  });
});
