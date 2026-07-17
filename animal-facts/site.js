(() => {
  const navigation = document.querySelector(".site-header nav");
  const menuToggle = document.querySelector(".menu-toggle");
  const navPanel = document.querySelector(".nav-panel");

  const closeMenu = (restoreFocus = false) => {
    if (!navigation || !menuToggle) return;
    navigation.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
    if (restoreFocus) menuToggle.focus();
  };

  if (navigation && menuToggle && navPanel) {
    menuToggle.addEventListener("click", () => {
      const opening = menuToggle.getAttribute("aria-expanded") !== "true";
      navigation.classList.toggle("is-open", opening);
      menuToggle.setAttribute("aria-expanded", String(opening));
      if (opening) {
        requestAnimationFrame(() => navPanel.querySelector("a")?.focus());
      }
    });

    navPanel.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeMenu();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && navigation.classList.contains("is-open")) {
        closeMenu(true);
      }
    });

    document.addEventListener("click", (event) => {
      if (!navigation.contains(event.target)) closeMenu();
    });
  }

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const revealItems = document.querySelectorAll(".reveal");

  if (reducedMotion.matches || !("IntersectionObserver" in window)) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });

    revealItems.forEach((item) => observer.observe(item));

    window.setTimeout(() => {
      revealItems.forEach((item) => item.classList.add("is-visible"));
    }, 1800);
  }

  const parallaxItems = document.querySelectorAll("[data-parallax]");
  let ticking = false;

  const updateParallax = () => {
    if (reducedMotion.matches) return;
    const y = window.scrollY;
    parallaxItems.forEach((item) => {
      const speed = Number(item.dataset.parallax);
      item.style.translate = `0 ${y * speed}px`;
    });
    ticking = false;
  };

  window.addEventListener("scroll", () => {
    if (!ticking) {
      requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });
})();
