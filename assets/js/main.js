/* ==========================================
   ŌPALA KULEANA — MAIN JS
   opalakuleana.com | Oahu Junk Removal
   ========================================== */

(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------
     NAV: scroll behavior
  ------------------------------------------ */
  var nav = document.getElementById('site-nav');

  function updateNav() {
    if (!nav) return;
    if (window.scrollY > 40) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', updateNav, { passive: true });
  updateNav();

  /* ------------------------------------------
     MOBILE MENU
  ------------------------------------------ */
  var hamburger   = document.querySelector('.nav-hamburger');
  var mobileNav   = document.getElementById('nav-mobile');
  var mobileClose = document.querySelector('.nav-mobile-close');

  function openMenu() {
    if (!mobileNav) return;
    mobileNav.classList.add('open');
    document.body.style.overflow = 'hidden';
    if (hamburger) hamburger.setAttribute('aria-expanded', 'true');

    if (!reducedMotion && typeof gsap !== 'undefined') {
      gsap.fromTo(mobileNav, { opacity: 0 }, { opacity: 1, duration: 0.28, ease: 'power2.out' });
      gsap.from('.nav-mobile a, .nav-mobile .btn', {
        y: 18,
        opacity: 0,
        stagger: 0.055,
        duration: 0.38,
        delay: 0.08,
        ease: 'power2.out'
      });
    } else {
      mobileNav.style.opacity = '1';
    }
  }

  function closeMenu() {
    if (!mobileNav) return;
    if (hamburger) hamburger.setAttribute('aria-expanded', 'false');

    if (!reducedMotion && typeof gsap !== 'undefined') {
      gsap.to(mobileNav, {
        opacity: 0,
        duration: 0.22,
        ease: 'power2.in',
        onComplete: function () {
          mobileNav.classList.remove('open');
          mobileNav.style.opacity = '';
          document.body.style.overflow = '';
        }
      });
    } else {
      mobileNav.classList.remove('open');
      mobileNav.style.opacity = '';
      document.body.style.overflow = '';
    }
  }

  if (hamburger) hamburger.addEventListener('click', openMenu);
  if (mobileClose) mobileClose.addEventListener('click', closeMenu);

  document.querySelectorAll('.nav-mobile a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });

  /* ------------------------------------------
     GSAP ANIMATIONS
  ------------------------------------------ */
  function initGSAP() {
    if (typeof gsap === 'undefined') return;
    gsap.registerPlugin(ScrollTrigger);

    if (!reducedMotion) {
      initHeroAnimation();
      initScrollReveals();
      initCounters();
    }
  }

  /* Hero entrance animation */
  function initHeroAnimation() {
    var heroLabel    = document.querySelector('.hero-label');
    var heroLines    = document.querySelectorAll('.hero-title-line');
    var heroSub      = document.querySelector('.hero-subtitle');
    var heroActions  = document.querySelector('.hero-actions');
    var heroTrust    = document.querySelector('.hero-trust');
    var heroCard     = document.querySelector('.hero-card');

    if (!heroLabel) return;

    var tl = gsap.timeline({ delay: 0.15 });

    tl.from(heroLabel, { y: 16, opacity: 0, duration: 0.5, ease: 'power2.out' });

    if (heroLines.length) {
      tl.from(heroLines, { y: 36, opacity: 0, duration: 0.65, stagger: 0.14, ease: 'power2.out' }, '-=0.2');
    }

    if (heroSub) {
      tl.from(heroSub, { y: 22, opacity: 0, duration: 0.55, ease: 'power2.out' }, '-=0.3');
    }

    if (heroActions) {
      tl.from(heroActions, { y: 18, opacity: 0, duration: 0.5, ease: 'power2.out' }, '-=0.3');
    }

    if (heroTrust) {
      tl.from(heroTrust, { opacity: 0, duration: 0.5, ease: 'power2.out' }, '-=0.25');
    }

    if (heroCard) {
      tl.from(heroCard, { x: 36, opacity: 0, duration: 0.7, ease: 'power2.out' }, '-=0.75');
    }
  }

  /* Scroll reveal: single elements + stagger groups */
  function initScrollReveals() {
    gsap.utils.toArray('.reveal').forEach(function (el) {
      gsap.from(el, {
        y: 30,
        opacity: 0,
        duration: 0.72,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          once: true
        }
      });
    });

    gsap.utils.toArray('.reveal-stagger').forEach(function (container) {
      var items = container.querySelectorAll('.stagger-item');
      if (!items.length) return;

      gsap.from(items, {
        y: 28,
        opacity: 0,
        duration: 0.6,
        stagger: 0.09,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: container,
          start: 'top 84%',
          once: true
        }
      });
    });
  }

  /* Counter animation for stat numbers */
  function initCounters() {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var target = parseFloat(el.dataset.count);
      var suffix = el.dataset.suffix || '';
      var prefix = el.dataset.prefix || '';
      var decimals = (el.dataset.decimals) ? parseInt(el.dataset.decimals) : 0;

      ScrollTrigger.create({
        trigger: el,
        start: 'top 85%',
        once: true,
        onEnter: function () {
          var obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 1.8,
            ease: 'power2.out',
            onUpdate: function () {
              el.textContent = prefix + obj.val.toFixed(decimals) + suffix;
            }
          });
        }
      });
    });
  }

  /* ------------------------------------------
     FAQ ACCORDION
  ------------------------------------------ */
  document.querySelectorAll('.faq-question').forEach(function (question) {
    question.addEventListener('click', function () {
      var item    = question.closest('.faq-item');
      var answer  = item.querySelector('.faq-answer');
      var isOpen  = item.classList.contains('open');

      /* Close all open items */
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        if (openItem === item) return;
        openItem.classList.remove('open');
        var a = openItem.querySelector('.faq-answer');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.to(a, { height: 0, duration: 0.28, ease: 'power2.inOut' });
        } else {
          a.style.height = '0';
        }
      });

      /* Toggle current */
      if (isOpen) {
        item.classList.remove('open');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.to(answer, { height: 0, duration: 0.28, ease: 'power2.inOut' });
        } else {
          answer.style.height = '0';
        }
      } else {
        item.classList.add('open');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.set(answer, { height: 'auto' });
          var h = answer.offsetHeight;
          gsap.fromTo(answer, { height: 0 }, { height: h, duration: 0.34, ease: 'power2.out' });
        } else {
          answer.style.height = 'auto';
        }
      }
    });
  });

  /* ------------------------------------------
     SMOOTH SCROLL (anchor links)
  ------------------------------------------ */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = anchor.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      var navHeight = parseInt(
        getComputedStyle(document.documentElement).getPropertyValue('--nav-h')
      ) || 72;
      var top = target.getBoundingClientRect().top + window.scrollY - navHeight - 8;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
  });

  /* ------------------------------------------
     CONTACT FORM: button state
  ------------------------------------------ */
  var contactForm = document.querySelector('.contact-form-el');
  if (contactForm) {
    contactForm.addEventListener('submit', function () {
      var btn = contactForm.querySelector('[type="submit"]');
      if (btn) {
        btn.textContent = 'Sending...';
        btn.disabled = true;
      }
    });
  }

  /* ------------------------------------------
     GSAP INIT (after scripts load)
  ------------------------------------------ */
  if (typeof gsap !== 'undefined') {
    initGSAP();
  } else {
    /* GSAP loaded with defer — wait for it */
    window.addEventListener('load', function () {
      if (typeof gsap !== 'undefined') initGSAP();
    });
  }

})();
