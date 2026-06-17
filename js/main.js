/* ========================================
   The Alpha Nova - Main JS
   ======================================== */

// Hero typed text animation
if (document.querySelector('.typed-text')) {
  new Typed('.typed-text', {
    strings: ['Future', 'Future', 'Web', 'Mobile', 'Chatbot'],
    typeSpeed: 80,
    backSpeed: 50,
    backDelay: 1000,
    startDelay: 0,
    loop: true,
    cursorChar: '|'
  });
}

// Header scroll effect
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
});

// Mobile menu toggle
const menuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');
if (menuBtn) {
  menuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    menuBtn.classList.toggle('active');
  });
  // Close on link click
  navLinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => navLinks.classList.remove('open'));
  });
}

// Counter animation
function animateCounters() {
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    const duration = 2000;
    const start = performance.now();

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(target * eased) + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  });
}

// Intersection Observer for counter animation
document.querySelectorAll('.stats-grid, .metrics-grid').forEach(section => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('[data-count]').forEach(el => {
          const target = parseInt(el.dataset.count);
          const suffix = el.dataset.suffix || '';
          const duration = 2000;
          const start = performance.now();
          function update(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(target * eased) + suffix;
            if (progress < 1) requestAnimationFrame(update);
          }
          requestAnimationFrame(update);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  observer.observe(section);
});

// Tabs (About page)
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const target = btn.dataset.tab;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(target).classList.add('active');
  });
});

// Scroll reveal animation
const scrollRevealElements = document.querySelectorAll('.scroll-reveal');
const scrollRevealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      scrollRevealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
scrollRevealElements.forEach(el => scrollRevealObserver.observe(el));

// Contact form status message
const urlParams = new URLSearchParams(window.location.search);
const formStatus = document.getElementById('form-status');
if (formStatus && urlParams.get('status')) {
  const status = urlParams.get('status');
  if (status === 'success') {
    formStatus.textContent = 'Message sent successfully! We\'ll get back to you soon.';
    formStatus.style.display = 'block';
    formStatus.style.background = '#ecfdf5';
    formStatus.style.color = '#065f46';
    formStatus.style.border = '1px solid #a7f3d0';
  } else if (status === 'failed') {
    formStatus.textContent = 'Message delivery failed. Please try again or email us directly.';
    formStatus.style.display = 'block';
    formStatus.style.background = '#fef2f2';
    formStatus.style.color = '#991b1b';
    formStatus.style.border = '1px solid #fecaca';
  } else if (status === 'captcha') {
    formStatus.textContent = 'Please complete the reCAPTCHA verification and try again.';
    formStatus.style.display = 'block';
    formStatus.style.background = '#fffbeb';
    formStatus.style.color = '#92400e';
    formStatus.style.border = '1px solid #fde68a';
  }
  // Clean URL
  history.replaceState(null, '', window.location.pathname + window.location.hash);
}

// Active nav link
const currentPage = window.location.pathname.split('/').filter(Boolean).pop() || 'index';
document.querySelectorAll('.nav-links a').forEach(a => {
  const href = a.getAttribute('href').replace('.html', '').split('/').filter(Boolean).pop() || 'index';
  if (href === currentPage || (currentPage === 'index' && href === 'index')) {
    a.classList.add('active');
  }
});
