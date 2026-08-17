#!/usr/bin/env python3
"""Generate the bespoke pages: /services, /industries, /book, /software-development-sudbury."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_pages import (  # noqa: E402
    ROOT, head, header, FOOTER, BOOK_CTA, faq_schema, faq_html,
    T_MORITZ, T_LEHMANN,
)

# ── /services ───────────────────────────────────────────────────────
SERVICE_CARDS = [
    ('ai-development', 'fa-brain', 'AI Development &amp; Computer Vision',
     'Production machine learning and vision systems that run against messy real-world data, drone footage, sensor streams, clinical instruments.'),
    ('custom-software-development', 'fa-cubes', 'Custom Software Development',
     'Platforms, APIs and data systems built around how your organization actually works, and maintained for the long term.'),
    ('mobile-app-development', 'fa-mobile-screen', 'Mobile App Development',
     'iOS and Android apps that hold up offline, on old devices and in regulated settings, and that you can keep shipping updates to.'),
    ('industrial-iot', 'fa-industry', 'Industrial &amp; IoT Systems',
     'Telemetry, edge intelligence and monitoring for mining, heavy industry and safety-critical operations.'),
    ('software-modernization', 'fa-arrows-rotate', 'Software Modernization',
     'Incremental migration and re-architecture for systems you cannot afford to switch off, without a risky full rewrite.'),
    ('case-studies', 'fa-pen-ruler', 'Product Design &amp; UX',
     'Interface and workflow design grounded in how the work is really done, delivered as part of every build we take on.'),
]


def services_page():
    cards = '\n'.join(f"""        <a href="/{slug}" class="path-card">
          <div class="path-icon"><i class="fas {icon}"></i></div>
          <h3>{title}</h3>
          <p>{body}</p>
          <span class="read-more">Learn More <i class="fas fa-arrow-right"></i></span>
        </a>""" for slug, icon, title, body in SERVICE_CARDS)

    return (
        head('Services | Software Engineering & Applied AI | The Alpha Nova',
             'Custom software development, applied AI and computer vision, mobile apps, industrial IoT and legacy modernization from The Alpha Nova.',
             'services')
        + header('services')
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">Services</span>
      <h1>Software Engineering &amp; Applied AI</h1>
      <p style="max-width:760px; margin:18px auto 0;">We work with organizations solving difficult problems, where the requirements are specific, the environment is unforgiving, or the answer does not exist off the shelf.</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Book a Discovery Call <i class="fas fa-arrow-right"></i></a>
        <a href="/case-studies" class="btn btn-secondary">View Our Work</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="paths-grid scroll-reveal">
{cards}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="hero-quote scroll-reveal">
        <blockquote>&ldquo;{T_LEHMANN['quote']}&rdquo;</blockquote>
        <div class="hero-quote-author">
          <img src="{T_LEHMANN['img']}" alt="{T_LEHMANN['name']}">
          <div>
            <h4>{T_LEHMANN['name']}</h4>
            <p>{T_LEHMANN['role']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
        + BOOK_CTA + FOOTER)


# ── /industries ─────────────────────────────────────────────────────
INDUSTRIES = [
    ('fa-hard-hat', 'Mining &amp; Heavy Industry',
     'Open-pit and underground operations needing computer vision, telemetry and edge systems that work where connectivity does not. Our Côté Gold blast-analysis system won first place against 29 teams across Ontario.',
     'case-cote-gold', 'Côté Gold AI Challenge'),
    ('fa-heart-pulse', 'Healthcare &amp; Clinical Research',
     'Clinical and research applications built with the consent flows, audit trails and data handling those settings demand. COGITO was built with UKE Hamburg, one of Europe\'s leading university hospitals.',
     'case-cogito', 'COGITO with UKE Hamburg'),
    ('fa-plane', 'Aviation &amp; Transportation',
     'Operational platforms processing complex, high-volume data in real time, where a wrong number has consequences beyond a dashboard.',
     'case-flight', 'AI Flight Data Platform'),
    ('fa-graduation-cap', 'Education &amp; Institutions',
     'Platforms serving entire institutional communities, alumni networks, student services and engagement tools built to scale across a campus.',
     'case-cambrian', 'Cambrian Alumni App'),
    ('fa-shield-halved', 'Defence &amp; Security',
     'Autonomous systems, spatial AI and real-time edge intelligence through The Alpha Nova Labs, our Canadian R&amp;D division.',
     'case-vanguardian', 'VanGuardian Fall Detection'),
    ('fa-store', 'Startups &amp; Growth Companies',
     'Founders who need a technical partner rather than a body shop. Woblu took first place and $18K in accelerator funding.',
     'case-woblu', 'Woblu'),
]


def industries_page():
    cards = '\n'.join(f"""        <div class="path-card">
          <div class="path-icon"><i class="fas {icon}"></i></div>
          <h3>{title}</h3>
          <p>{body}</p>
          <a href="/{slug}" class="read-more">{link_label} <i class="fas fa-arrow-right"></i></a>
        </div>""" for icon, title, body, slug, link_label in INDUSTRIES)

    return (
        head('Industries We Serve | The Alpha Nova',
             'Software and applied AI for mining, healthcare, aviation, education, defence and growth companies. See the work we have delivered in each sector.',
             'industries')
        + header('industries')
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">Industries</span>
      <h1>Where We Work Best</h1>
      <p style="max-width:760px; margin:18px auto 0;">We are not sector-agnostic. Our work concentrates in environments where the engineering is hard, the data is messy and the cost of getting it wrong is real.</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Book a Discovery Call <i class="fas fa-arrow-right"></i></a>
        <a href="/case-studies" class="btn btn-secondary">View Our Work</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="paths-grid scroll-reveal">
{cards}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="hero-quote scroll-reveal">
        <blockquote>&ldquo;{T_MORITZ['quote']}&rdquo;</blockquote>
        <div class="hero-quote-author">
          <img src="{T_MORITZ['img']}" alt="{T_MORITZ['name']}">
          <div>
            <h4>{T_MORITZ['name']}</h4>
            <p>{T_MORITZ['role']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
        + BOOK_CTA + FOOTER)


# ── /book ───────────────────────────────────────────────────────────
def book_page():
    return (
        head('Book a Discovery Call | The Alpha Nova',
             'Book a free 30-minute project discovery call with The Alpha Nova. Tell us what you are trying to build and we will tell you how we would approach it.',
             'book')
        + header()
        + """
  <section class="page-hero" style="padding-bottom:48px;">
    <div class="container">
      <span class="section-label">Discovery Call</span>
      <h1>Book a 30-Minute Discovery Call</h1>
      <p style="max-width:720px; margin:18px auto 0;">Tell us what you're trying to build. We'll spend 30 minutes understanding the problem and tell you how we'd approach it, including whether we think we're the right team for it. No charge, no obligation, no sales sequence.</p>
    </div>
  </section>

  <section class="section" style="padding-top:20px;">
    <div class="container">
      <!-- Calendly inline embed. Hidden until CALENDLY_URL is set in js/main.js -->
      <div id="calendly-inline" style="display:none; min-width:320px; height:700px; margin-bottom:40px;"></div>

      <div id="calendly-fallback" class="contact-layout scroll-reveal">
        <div class="contact-info">
          <h3>What to expect</h3>
          <p style="color:var(--secondary-text); line-height:1.7; margin-bottom:26px;">A straight technical conversation, not a pitch. Come with the problem; you don't need a spec.</p>
          <div class="contact-info-item">
            <div class="contact-info-icon"><i class="fas fa-clock"></i></div>
            <div>
              <span class="contact-info-label">LENGTH</span>
              <p>30 minutes, by video or phone</p>
            </div>
          </div>
          <div class="contact-info-item">
            <div class="contact-info-icon"><i class="fas fa-comments"></i></div>
            <div>
              <span class="contact-info-label">WHO YOU'LL SPEAK TO</span>
              <p>An engineer who would work on it, not an account manager</p>
            </div>
          </div>
          <div class="contact-info-item">
            <div class="contact-info-icon"><i class="fas fa-envelope"></i></div>
            <div>
              <span class="contact-info-label">EMAIL</span>
              <p><a href="mailto:info@thealphanova.com">info@thealphanova.com</a></p>
            </div>
          </div>
          <div class="contact-info-item">
            <div class="contact-info-icon"><i class="fas fa-phone"></i></div>
            <div>
              <span class="contact-info-label">PHONE</span>
              <p><a href="tel:+14374245384">+1 437 424 5384</a></p>
            </div>
          </div>
        </div>

        <form class="contact-form-v2 lead-form" action="sendemail.php" method="POST">
          <h3>Request a call</h3>
          <p>Six questions. We'll come back with times, usually within one business day.</p>
          <div class="form-row">
            <div class="form-field">
              <label>Name *</label>
              <input type="text" name="name" placeholder="Your name" required>
            </div>
            <div class="form-field">
              <label>Company *</label>
              <input type="text" name="organization" placeholder="Your organization" required>
            </div>
          </div>
          <div class="form-field">
            <label>Work email *</label>
            <input type="email" name="email" placeholder="you@company.com" required>
          </div>
          <div class="form-field">
            <label>What do you need? *</label>
            <textarea name="message" placeholder="The problem you're trying to solve, and anything already in place." required></textarea>
          </div>
          <div class="form-row">
            <div class="form-field">
              <label>Approximate budget</label>
              <select name="budget">
                <option value="">Not sure yet</option>
                <option value="Under $25K">Under $25K</option>
                <option value="$25K - $75K">$25K &ndash; $75K</option>
                <option value="$75K - $150K">$75K &ndash; $150K</option>
                <option value="$150K - $500K">$150K &ndash; $500K</option>
                <option value="$500K+">$500K+</option>
              </select>
            </div>
            <div class="form-field">
              <label>Target timeline</label>
              <select name="timeline">
                <option value="">Not sure yet</option>
                <option value="ASAP">As soon as possible</option>
                <option value="1-3 months">1 &ndash; 3 months</option>
                <option value="3-6 months">3 &ndash; 6 months</option>
                <option value="6+ months">6+ months</option>
                <option value="Exploring only">Just exploring</option>
              </select>
            </div>
          </div>
          <input type="hidden" name="subject" value="Discovery call request">
          <button type="submit" class="btn btn-contact">Request a Discovery Call</button>
          <div id="form-status" style="display:none; margin-top: 16px; padding: 12px 16px; border-radius: 8px; font-size: 14px; font-weight: 500;"></div>
        </form>
      </div>
    </div>
  </section>
""" + FOOTER.replace(
            '  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>',
            '  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css">\n'
            '  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>\n'
            '  <script src="https://www.google.com/recaptcha/api.js?render=6Lf98IUtAAAAAEGESxXnH2-A8A_IdRRtOL344JK_"></script>\n'
            '  <script>\n'
            '    (function () {\n'
            "      var SITEKEY = '6Lf98IUtAAAAAEGESxXnH2-A8A_IdRRtOL344JK_';\n"
            '      document.querySelectorAll(\'form[action*="sendemail.php"]\').forEach(function (form) {\n'
            "        var hidden = document.createElement('input');\n"
            "        hidden.type = 'hidden'; hidden.name = 'g-recaptcha-response';\n"
            '        form.appendChild(hidden);\n'
            "        form.addEventListener('submit', function (e) {\n"
            "          if (form.dataset.rcDone === '1') return;\n"
            '          e.preventDefault();\n'
            '          grecaptcha.ready(function () {\n'
            "            grecaptcha.execute(SITEKEY, { action: 'submit' }).then(function (token) {\n"
            '              hidden.value = token;\n'
            "              form.dataset.rcDone = '1';\n"
            '              form.submit();\n'
            '            });\n'
            '          });\n'
            '        });\n'
            '      });\n'
            '    })();\n'
            '  </script>'))


# ── /software-development-sudbury ───────────────────────────────────
SUDBURY_FAQS = [
    ('What software development services does The Alpha Nova offer in Sudbury?',
     'The Alpha Nova offers custom mobile app development, web application development, AI and machine learning solutions, database engineering, UI/UX design and enterprise software development from our Greater Sudbury office. We serve clients across Northern Ontario, Canada and internationally.'),
    ('Where is The Alpha Nova located in Sudbury?',
     'The Alpha Nova is headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. Our Sudbury office is the home base for everything we design, build and ship as a proudly Canadian company.'),
    ('How much does custom software development cost in Sudbury?',
     'Costs vary with project complexity, features and timeline. We provide transparent pricing and work with organizations of all sizes across Northern Ontario. Book a discovery call or contact info@thealphanova.com for a quote tailored to your project.'),
    ('What industries does The Alpha Nova serve in Northern Ontario?',
     'We serve mining, healthcare, education, transportation, aviation and enterprise clients. Our Sudbury location gives us direct insight into Northern Ontario mining and resource operations, including our first-place finish in the Côté Gold Blast Captain Challenge.'),
    ('How long does it take to develop custom software?',
     'Simple mobile apps typically take 2-3 months; complex enterprise systems run 6-12 months. We work in agile increments with regular milestones and transparent communication throughout.'),
    ('Do you work with startups and small businesses in Sudbury?',
     'Yes. We work with organizations of all sizes, from startups to enterprises. Several of our projects began as startup ideas, including our own VanGuardian fall-detection system.'),
]


def sudbury_page():
    local_schema = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": "https://thealphanova.com/software-development-sudbury",
    "name": "The Alpha Nova",
    "url": "https://thealphanova.com/software-development-sudbury",
    "logo": "https://thealphanova.com/img/wp/tan-e1764091769895.png",
    "image": "https://thealphanova.com/img/wp/alphanova-1024x768.jpg",
    "description": "Software development company in Greater Sudbury, Ontario, specializing in custom mobile apps, web development, AI solutions and enterprise software for Northern Ontario businesses.",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "1545 Maley Drive",
      "addressLocality": "Greater Sudbury",
      "addressRegion": "ON",
      "postalCode": "P3A 4R7",
      "addressCountry": "CA"
    },
    "geo": { "@type": "GeoCoordinates", "latitude": "46.5453", "longitude": "-80.9930" },
    "telephone": "+1-437-424-5384",
    "email": "info@thealphanova.com",
    "areaServed": [
      { "@type": "City", "name": "Greater Sudbury" },
      { "@type": "AdministrativeArea", "name": "Northern Ontario" }
    ],
    "priceRange": "$$",
    "openingHours": "Mo-Fr 09:00-17:00",
    "sameAs": [
      "https://www.facebook.com/theAlphaNova/",
      "https://www.instagram.com/thealphanova",
      "https://www.linkedin.com/company/the-alpha-nova"
    ]
  }
  </script>
"""
    return (
        head('Software Development Sudbury | Custom Apps & AI | The Alpha Nova',
             'Sudbury-based software development company specializing in custom mobile apps, web development, AI solutions and enterprise software. Serving Northern Ontario businesses.',
             'software-development-sudbury',
             local_schema + faq_schema(SUDBURY_FAQS))
        + header()
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">Greater Sudbury, Ontario</span>
      <h1>Software Development in Sudbury</h1>
      <p style="max-width:760px; margin:18px auto 0;">We are a software company headquartered on Maley Drive in Greater Sudbury, building custom applications, AI systems and enterprise software for Northern Ontario organizations, and for clients across Canada and Europe from here.</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Book a Discovery Call <i class="fas fa-arrow-right"></i></a>
        <a href="/case-studies" class="btn btn-secondary">View Our Work</a>
      </div>
    </div>
  </section>

  <div class="cred-strip">
    <div class="container">
      <p>Trusted by teams at <strong>UKE Hamburg</strong> &middot; <strong>Cambrian College</strong> &middot; <strong>comAlpine</strong> &middot; and growing companies across Canada and Europe</p>
    </div>
  </div>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Local Work</span>
        <h2>Built in Northern Ontario</h2>
        <p>Being based in Sudbury means we understand mining and resource operations from the inside, not from a case study.</p>
      </div>
      <div class="case-studies-grid scroll-reveal">
        <a href="/case-cote-gold" class="case-card">
          <div class="case-card-image"><img src="img/cote-gold-winners.jpg" alt="Côté Gold Blast Captain Challenge"></div>
          <div class="case-card-content">
            <h3>Côté Gold AI Challenge</h3>
            <p>First place in an Ontario-wide AI competition analyzing open-pit mining blasts from drone footage, against 29 competing teams.</p>
            <span class="read-more">Read More <i class="fas fa-arrow-right"></i></span>
          </div>
        </a>
        <a href="/case-cambrian" class="case-card">
          <div class="case-card-image"><img src="img/wp/sambrian.png" alt="Cambrian Alumni App"></div>
          <div class="case-card-content">
            <h3>Cambrian College Alumni App</h3>
            <p>A cross-platform mobile app connecting the alumni network of a Sudbury college with events, careers and community.</p>
            <span class="read-more">Read More <i class="fas fa-arrow-right"></i></span>
          </div>
        </a>
        <a href="/case-vanguardian" class="case-card">
          <div class="case-card-image"><img src="img/vanguardian-frame1.jpg" alt="VanGuardian"></div>
          <div class="case-card-content">
            <h3>VanGuardian Fall Detection</h3>
            <p>AI-powered fall detection requiring no wearable device, developed through our Canadian R&amp;D division.</p>
            <span class="read-more">Read More <i class="fas fa-arrow-right"></i></span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Services in Sudbury</span>
        <h2>What We Build for Northern Ontario</h2>
      </div>
      <div class="cap-grid scroll-reveal">
        <div class="cap-card"><i class="fas fa-mobile-screen"></i><h3>Mobile App Development</h3><p>iOS and Android applications for Northern Ontario organizations, built to work offline and on the devices your people actually carry.</p></div>
        <div class="cap-card"><i class="fas fa-globe"></i><h3>Web &amp; Platform Development</h3><p>Web applications, customer portals and internal tools designed around how your operation actually runs.</p></div>
        <div class="cap-card"><i class="fas fa-brain"></i><h3>AI &amp; Machine Learning</h3><p>Applied AI and computer vision, including mining and industrial imagery analysis proven in competition.</p></div>
        <div class="cap-card"><i class="fas fa-database"></i><h3>Database Engineering</h3><p>Schema design, migrations and reporting layers that keep data trustworthy as your operation grows.</p></div>
        <div class="cap-card"><i class="fas fa-industry"></i><h3>Industrial &amp; IoT Systems</h3><p>Telemetry and edge systems for mining and heavy industry, designed for sites where connectivity is unreliable.</p></div>
        <div class="cap-card"><i class="fas fa-pen-ruler"></i><h3>UI/UX &amp; Product Design</h3><p>Interface and workflow design grounded in how the work is really done on site and in the office.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">FAQ</span>
        <h2>Software Development in Sudbury, Common Questions</h2>
      </div>
      <div class="faq-list">
{faq_html(SUDBURY_FAQS)}
      </div>
    </div>
  </section>

  <div class="map-section">
    <iframe src="https://maps.google.com/maps?q=1545%20Maley%20Dr%2C%20Greater%20Sudbury%2C%20ON%20P3A%203V8%2C%20Canada&t=m&z=15&output=embed&iwloc=near" loading="lazy" title="Office Location"></iframe>
  </div>
"""
        + BOOK_CTA + FOOTER)


PAGES = {
    'services.html': services_page,
    'industries.html': industries_page,
    'book.html': book_page,
    'software-development-sudbury.html': sudbury_page,
}

if __name__ == '__main__':
    for name, fn in PAGES.items():
        path = os.path.join(ROOT, name)
        with open(path, 'w') as f:
            f.write(fn())
        print('wrote', path)
