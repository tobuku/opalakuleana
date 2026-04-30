/* ==========================================
   ŌPALA KULEANA — MAIN JS
   opalakuleana.com | Oahu Junk Removal
   ========================================== */

(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------
     SCROLL PROGRESS BAR
  ------------------------------------------ */
  var progressBar = document.getElementById('scroll-progress');

  if (progressBar && !reducedMotion) {
    window.addEventListener('scroll', function () {
      var scrolled  = window.scrollY;
      var maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      var pct = maxScroll > 0 ? (scrolled / maxScroll) * 100 : 0;
      progressBar.style.width = pct + '%';
    }, { passive: true });
  }

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
        y: 22,
        opacity: 0,
        stagger: 0.06,
        duration: 0.42,
        delay: 0.1,
        ease: 'back.out(1.5)'
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
     HERO TRUCK SCENE ANIMATION
  ------------------------------------------ */
  function initHeroScene() {
    var truck  = document.getElementById('scene-truck');
    var bed    = document.getElementById('truck-bed');
    var tBox   = document.getElementById('t-box');
    var tBag   = document.getElementById('t-bag');
    var tChair = document.getElementById('t-chair');
    var wheels = ['wf','wra','wrb'].map(function(id){
      return document.getElementById(id);
    }).filter(Boolean);

    if (!truck || !bed) return;

    /* Bed pivot: front-bottom of the bed rectangle */
    gsap.set(bed, { transformOrigin: '0% 100%' });

    function runScene() {
      /* Reset all positions */
      gsap.set(truck,  { x: 1450, y: 0 });
      gsap.set(bed,    { rotation: 0 });
      gsap.set(tBox,   { opacity: 0, x: 310, y: -55, rotation: 0 });
      gsap.set(tBag,   { opacity: 0, x: -80, y: 80,  rotation: 0 });
      gsap.set(tChair, { opacity: 0, x: 650, y: 80,  rotation: 0 });
      gsap.set(wheels, { rotation: 0 });

      var tl = gsap.timeline({
        onComplete: function () { gsap.delayedCall(2.5, runScene); }
      });

      /* 1 — Drive in from right, wheels spinning */
      tl.to(truck,  { x: 280,  duration: 3.6, ease: 'power2.out' }, 0);
      tl.to(wheels, { rotation: 740, duration: 3.6, ease: 'none' }, 0);

      /* 2 — Bounce to a stop */
      tl.to(truck, { y: 8,  duration: 0.1, ease: 'power2.out' }, 3.6);
      tl.to(truck, { y: 0,  duration: 0.3, ease: 'bounce.out' }, 3.7);

      /* 3 — Bed raises (pivot front-bottom, rear/tailgate lifts right) */
      tl.to(bed, { rotation: 40, duration: 1.8, ease: 'power2.inOut' }, 4.3);

      /* 4 — Trash items fly in from different directions */
      tl.to(tBox,   { opacity: 1, x: 310, y: 80, rotation: -18, duration: 0.7, ease: 'power3.in' }, 4.8);
      tl.to(tBag,   { opacity: 1, x: 370, y: 90, rotation:  25, duration: 0.75, ease: 'power2.in' }, 5.2);
      tl.to(tChair, { opacity: 1, x: 250, y: 85, rotation: -10, duration: 0.8,  ease: 'power3.in' }, 5.5);

      /* 5 — Bed lowers back to flat */
      tl.to(bed, { rotation: 0, duration: 1.5, ease: 'power2.inOut' }, 6.8);

      /* 6 — Drives off left, wheels spinning */
      tl.to(truck,  { x: -850, duration: 2.8, ease: 'power2.in'  }, 8.6);
      tl.to(wheels, { rotation: 1340, duration: 2.8, ease: 'none' }, 8.6);
      tl.to([tBox, tBag, tChair], { opacity: 0, duration: 0.4 }, 8.6);
    }

    runScene();
  }

  /* ------------------------------------------
     GSAP ANIMATIONS
  ------------------------------------------ */
  function initGSAP() {
    if (typeof gsap === 'undefined') return;
    gsap.registerPlugin(ScrollTrigger);
    if (typeof ScrollToPlugin !== 'undefined') {
      gsap.registerPlugin(ScrollToPlugin);
    }

    if (!reducedMotion) {
      initNavEntrance();
      initHeroAnimation();
      initHeroFloat();
      initHeroParallax();
      initHeroScene();
      initScrollReveals();
      initCounters();
    }
  }

  /* ------------------------------------------
     NAV ENTRANCE
  ------------------------------------------ */
  function initNavEntrance() {
    var navLogo  = document.querySelector('.nav-logo');
    var navItems = document.querySelectorAll('.nav-links li');
    var navCta   = document.querySelector('.nav-cta .btn-primary');

    if (!navLogo) return;

    var tl = gsap.timeline({ delay: 0.05 });
    tl.from(navLogo, { y: -20, opacity: 0, duration: 0.5, ease: 'power2.out' });

    if (navItems.length) {
      tl.from(navItems, {
        y: -16,
        opacity: 0,
        stagger: 0.07,
        duration: 0.4,
        ease: 'power2.out'
      }, '-=0.3');
    }

    if (navCta) {
      tl.from(navCta, { scale: 0.85, opacity: 0, duration: 0.4, ease: 'back.out(2)' }, '-=0.2');
    }
  }

  /* ------------------------------------------
     HERO ENTRANCE
  ------------------------------------------ */
  function initHeroAnimation() {
    var heroLabel   = document.querySelector('.hero-label');
    var heroLines   = document.querySelectorAll('.hero-title-line');
    var heroSub     = document.querySelector('.hero-subtitle');
    var heroActions = document.querySelector('.hero-actions');
    var trustItems  = document.querySelectorAll('.trust-item');
    var heroCard    = document.querySelector('.hero-card');

    if (!heroLabel) return;

    var tl = gsap.timeline({ delay: 0.3 });

    tl.from(heroLabel, {
      y: 24,
      opacity: 0,
      duration: 0.55,
      ease: 'back.out(1.8)'
    });

    if (heroLines.length) {
      tl.from(heroLines, {
        y: 52,
        opacity: 0,
        duration: 0.72,
        stagger: 0.15,
        ease: 'power3.out'
      }, '-=0.25');
    }

    if (heroSub) {
      tl.from(heroSub, { y: 26, opacity: 0, duration: 0.6, ease: 'power2.out' }, '-=0.4');
    }

    if (heroActions && heroActions.children.length) {
      tl.from(heroActions.children, {
        y: 24,
        opacity: 0,
        duration: 0.52,
        stagger: 0.11,
        ease: 'back.out(1.6)'
      }, '-=0.38');
    }

    if (trustItems.length) {
      tl.from(trustItems, {
        x: -18,
        opacity: 0,
        stagger: 0.09,
        duration: 0.45,
        ease: 'power2.out'
      }, '-=0.3');
    }

    if (heroCard) {
      tl.from(heroCard, {
        x: 52,
        opacity: 0,
        scale: 0.94,
        duration: 0.78,
        ease: 'power3.out'
      }, '-=0.9');
    }
  }

  /* ------------------------------------------
     HERO CARD FLOAT LOOP
  ------------------------------------------ */
  function initHeroFloat() {
    var heroCard = document.querySelector('.hero-card');
    if (!heroCard) return;

    gsap.to(heroCard, {
      y: -14,
      duration: 3.2,
      ease: 'sine.inOut',
      yoyo: true,
      repeat: -1,
      delay: 1.4
    });
  }

  /* ------------------------------------------
     HERO PARALLAX (mouse move)
  ------------------------------------------ */
  function initHeroParallax() {
    var hero     = document.querySelector('.hero');
    var heroText = document.querySelector('.hero-text');
    var heroCard = document.querySelector('.hero-card');

    if (!hero) return;

    hero.addEventListener('mousemove', function (e) {
      var rect = hero.getBoundingClientRect();
      var dx   = (e.clientX - rect.left - rect.width  / 2) / (rect.width  / 2);
      var dy   = (e.clientY - rect.top  - rect.height / 2) / (rect.height / 2);

      if (heroText) {
        gsap.to(heroText, {
          x: dx * 10,
          y: dy * 6,
          duration: 1,
          ease: 'power2.out',
          overwrite: 'auto'
        });
      }
      /* Only move card on x-axis — y is handled by the float loop */
      if (heroCard) {
        gsap.to(heroCard, {
          x: dx * -16,
          duration: 1,
          ease: 'power2.out',
          overwrite: 'auto'
        });
      }
    });

    hero.addEventListener('mouseleave', function () {
      if (heroText) {
        gsap.to(heroText, { x: 0, y: 0, duration: 0.8, ease: 'power2.out', overwrite: 'auto' });
      }
      if (heroCard) {
        gsap.to(heroCard, { x: 0, duration: 0.8, ease: 'power2.out', overwrite: 'auto' });
      }
    });
  }

  /* ------------------------------------------
     SCROLL REVEALS — enhanced per section type
  ------------------------------------------ */
  function initScrollReveals() {

    /* Standard .reveal elements */
    gsap.utils.toArray('.reveal').forEach(function (el) {
      gsap.from(el, {
        y: 38,
        opacity: 0,
        duration: 0.8,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: 'top 88%',
          once: true
        }
      });
    });

    /* .reveal-stagger containers — differentiated by class */
    gsap.utils.toArray('.reveal-stagger').forEach(function (container) {
      var items = container.querySelectorAll('.stagger-item');
      if (!items.length) return;

      var isTestimonials = container.classList.contains('testimonials-grid');
      var isServices     = container.classList.contains('services-grid');
      var isProcess      = container.classList.contains('process-steps');
      var isAreas        = container.classList.contains('areas-grid');

      if (isTestimonials) {
        /* Alternate left / right slide per card */
        items.forEach(function (card, i) {
          gsap.from(card, {
            x: i % 2 === 0 ? -44 : 44,
            y: 18,
            opacity: 0,
            scale: 0.96,
            duration: 0.72,
            ease: 'power3.out',
            delay: i * 0.13,
            scrollTrigger: {
              trigger: container,
              start: 'top 85%',
              once: true
            }
          });
        });

      } else if (isServices) {
        /* Spring pop for service cards */
        gsap.from(items, {
          y: 40,
          opacity: 0,
          scale: 0.9,
          duration: 0.65,
          stagger: 0.07,
          ease: 'back.out(1.6)',
          scrollTrigger: {
            trigger: container,
            start: 'top 84%',
            once: true
          }
        });

      } else if (isProcess) {
        /* Scale + slide for process steps */
        gsap.from(items, {
          y: 44,
          scale: 0.92,
          opacity: 0,
          duration: 0.7,
          stagger: 0.16,
          ease: 'back.out(1.5)',
          scrollTrigger: {
            trigger: container,
            start: 'top 85%',
            once: true
          }
        });

      } else if (isAreas) {
        /* Fast wave for area tags */
        gsap.from(items, {
          y: 22,
          opacity: 0,
          scale: 0.88,
          duration: 0.38,
          stagger: 0.035,
          ease: 'back.out(1.5)',
          scrollTrigger: {
            trigger: container,
            start: 'top 84%',
            once: true
          }
        });

      } else {
        /* Default */
        gsap.from(items, {
          y: 28,
          opacity: 0,
          duration: 0.62,
          stagger: 0.09,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: container,
            start: 'top 84%',
            once: true
          }
        });
      }
    });

    /* Stat cards — pop-in with elastic */
    var statsGrid = document.querySelector('.stats-grid');
    if (statsGrid) {
      var statCards = statsGrid.querySelectorAll('.stat-card');
      if (statCards.length) {
        gsap.from(statCards, {
          scale: 0.75,
          opacity: 0,
          duration: 0.65,
          stagger: 0.13,
          ease: 'back.out(2)',
          scrollTrigger: {
            trigger: statsGrid,
            start: 'top 85%',
            once: true
          }
        });
      }
    }

    /* Footer columns */
    var footerCols = document.querySelectorAll('.footer-grid > div');
    if (footerCols.length) {
      gsap.from(footerCols, {
        y: 30,
        opacity: 0,
        duration: 0.65,
        stagger: 0.1,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: '.site-footer',
          start: 'top 90%',
          once: true
        }
      });
    }

    /* CTA banner scale-in */
    var ctaBanner = document.querySelector('.cta-banner');
    if (ctaBanner) {
      gsap.from(ctaBanner, {
        scale: 0.97,
        opacity: 0,
        duration: 0.7,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: ctaBanner,
          start: 'top 88%',
          once: true
        }
      });
    }

    /* Logo background marks — slow fade + drift */
    gsap.utils.toArray('.logo-bg-mark').forEach(function (mark) {
      gsap.from(mark, {
        opacity: 0,
        scale: 0.88,
        duration: 1.8,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: mark,
          start: 'top 90%',
          once: true
        }
      });
      /* Slow continuous drift */
      gsap.to(mark, {
        y: -18,
        duration: 8,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        delay: Math.random() * 2
      });
    });

    /* Page hero (inner pages) */
    var pageHero = document.querySelector('.page-hero');
    if (pageHero) {
      var ph = gsap.timeline({ delay: 0.2 });
      var phLabel = pageHero.querySelector('.post-category');
      var phH1    = pageHero.querySelector('h1');
      var phLead  = pageHero.querySelector('.page-lead');
      if (phLabel) ph.from(phLabel, { y: 16, opacity: 0, duration: 0.5, ease: 'back.out(1.8)' });
      if (phH1)    ph.from(phH1,    { y: 30, opacity: 0, duration: 0.6, ease: 'power3.out' }, '-=0.2');
      if (phLead)  ph.from(phLead,  { y: 20, opacity: 0, duration: 0.5, ease: 'power2.out' }, '-=0.3');
    }
  }

  /* ------------------------------------------
     COUNTER ANIMATION
  ------------------------------------------ */
  function initCounters() {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var target   = parseFloat(el.dataset.count);
      var suffix   = el.dataset.suffix   || '';
      var prefix   = el.dataset.prefix   || '';
      var decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;

      ScrollTrigger.create({
        trigger: el,
        start: 'top 85%',
        once: true,
        onEnter: function () {
          var obj = { val: 0 };
          gsap.to(obj, {
            val: target,
            duration: 2,
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
      var item   = question.closest('.faq-item');
      var answer = item.querySelector('.faq-answer');
      var isOpen = item.classList.contains('open');

      /* Close all open items */
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        if (openItem === item) return;
        openItem.classList.remove('open');
        var a = openItem.querySelector('.faq-answer');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.to(a, { height: 0, duration: 0.3, ease: 'power2.inOut' });
        } else {
          a.style.height = '0';
        }
      });

      /* Toggle current */
      if (isOpen) {
        item.classList.remove('open');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.to(answer, { height: 0, duration: 0.3, ease: 'power2.inOut' });
        } else {
          answer.style.height = '0';
        }
      } else {
        item.classList.add('open');
        if (!reducedMotion && typeof gsap !== 'undefined') {
          gsap.set(answer, { height: 'auto' });
          var h = answer.offsetHeight;
          gsap.fromTo(answer, { height: 0 }, { height: h, duration: 0.38, ease: 'power3.out' });
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
      var href   = anchor.getAttribute('href');
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
    window.addEventListener('load', function () {
      if (typeof gsap !== 'undefined') initGSAP();
    });
  }

})();
