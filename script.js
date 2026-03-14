// Fade-in on scroll
const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.style.animationPlayState = 'running';
            obs.unobserve(e.target);
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in').forEach(el => {
    el.style.animationPlayState = 'paused';
    obs.observe(el);
});
document.querySelectorAll('section:first-of-type .fade-in').forEach(el => {
    el.style.animationPlayState = 'running';
});

// Hero image carousel — auto-cycles + advances on scroll
(function () {
    const imgs = document.querySelectorAll('[data-carousel-img]');
    if (!imgs.length) return;
    let current = 0;
    let autoTimer;

    function showImage(index) {
        imgs.forEach((img, i) => {
            img.style.opacity = i === index ? '1' : '0';
        });
        current = index;
    }

    function next() {
        showImage((current + 1) % imgs.length);
    }

    // Auto-cycle every 3.5 seconds
    function startAuto() {
        clearInterval(autoTimer);
        autoTimer = setInterval(next, 3500);
    }
    startAuto();

    // Advance on scroll (throttled)
    let lastScroll = 0;
    let scrollAccum = 0;
    const scrollThreshold = 400; // pixels of scroll to trigger next image

    window.addEventListener('scroll', function () {
        const scrollY = window.scrollY;
        const delta = Math.abs(scrollY - lastScroll);
        lastScroll = scrollY;
        scrollAccum += delta;

        if (scrollAccum >= scrollThreshold) {
            scrollAccum = 0;
            next();
            startAuto();
        }
    }, { passive: true });
})();

// Mobile Menu Toggle logic
(function () {
    const btn = document.querySelector('.hamburger-btn');
    const menu = document.querySelector('.mobile-menu');
    const links = document.querySelectorAll('.mobile-nav-link');
    const nav = document.querySelector('nav');

    let isOpen = false;
    function toggleMenu() {
        isOpen = !isOpen;
        if (isOpen) {
            menu.classList.add('open');
            nav.classList.add('menu-open');
            btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-ink"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
        } else {
            menu.classList.remove('open');
            nav.classList.remove('menu-open');
            btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>`;
        }
    }

    btn.addEventListener('click', toggleMenu);
    links.forEach(l => l.addEventListener('click', toggleMenu));
})();

// Nav State (Scroll transparency + active link tracking)
(function () {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    const nav = document.querySelector('nav');

    function updateActiveNav() {
        const scrollY = window.scrollY + 200; // offset so earlier detection
        let currentSection = '';

        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            if (scrollY >= top && scrollY < top + height) {
                currentSection = section.id;
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + currentSection) {
                link.classList.add('active');
            }
        });

        // Toggle transparent vs solid background on scroll
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', updateActiveNav, { passive: true });
    updateActiveNav();
})();

// --- Premium Scroll Animations ---
const revealElements = document.querySelectorAll('.reveal-up');

// Create the observer
const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        // If element is in view
        if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            // Optional: Stop observing once revealed to only animate once
            observer.unobserve(entry.target);
        }
    });
}, {
    root: null, // Use viewport
    rootMargin: '0px',
    threshold: 0.15 // Trigger when 15% of the element is visible
});

// Start observing all .reveal-up elements
revealElements.forEach(el => revealObserver.observe(el));
