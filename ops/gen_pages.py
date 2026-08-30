#!/usr/bin/env python3
"""Generate The Alpha Nova service / industries / booking pages.

Emits plain static HTML into the repo, the site has no build step, so these
files are committed and hand-edited from here on. This script exists only to
make the first pass consistent (identical nav, footer, schema, CTA blocks).
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GTAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KQY5692DSS"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KQY5692DSS');
  </script>"""


def head(title, desc, slug, extra_schema=''):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="The Alpha Nova">
  <link rel="canonical" href="https://thealphanova.com/{slug}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://thealphanova.com/{slug}">
  <meta property="og:image" content="https://thealphanova.com/img/wp/alphanova-1024x768.jpg">
  <meta property="og:site_name" content="The Alpha Nova">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://thealphanova.com/img/wp/alphanova-1024x768.jpg">
  <link rel="icon" href="img/wp/cropped-fav-32x32.jpg" sizes="32x32">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="css/style.css?v=20260814b">
{extra_schema}{GTAG}
</head>
<body>
"""


def header(active=''):
    def cls(name):
        return ' class="active"' if name == active else ''
    return f"""
  <header class="header">
    <div class="container">
      <a href="/" class="logo"><img src="img/wp/tan-e1764091769895.png" alt="The Alpha Nova"></a>
      <nav>
        <ul class="nav-links">
          <li><a href="/services"{cls('services')}>Services</a></li>
          <li><a href="/industries"{cls('industries')}>Industries</a></li>
          <li><a href="/case-studies"{cls('work')}>Work</a></li>
          <li class="nav-dropdown">
            <a href="/products" class="nav-drop-toggle{' active' if active == 'products' else ''}">Products <i class="fas fa-chevron-down"></i></a>
            <ul class="nav-dropdown-menu">
              <li><a href="/cogito-ai">COGITO AI</a></li>
              <li><a href="/case-vanguardian">VanGuardian</a></li>
              <li><a href="/products">All Products</a></li>
            </ul>
          </li>
          <li><a href="https://labs.thealphanova.com/">Labs</a></li>
          <li><a href="/about"{cls('about')}>About</a></li>
          <li><a href="/book" class="nav-cta" data-calendly>Book a Call</a></li>
        </ul>
      </nav>
      <button class="mobile-menu-btn" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </header>
"""


BOOK_CTA = """
  <!-- Booking CTA -->
  <section class="section">
    <div class="container">
      <div class="book-cta scroll-reveal">
        <h2>Have a software or AI project in mind?</h2>
        <p>Tell us what you're trying to build. We'll spend 30 minutes understanding the problem and tell you how we'd approach it.</p>
        <a href="/book" class="btn btn-primary" data-calendly>Book a 30-Minute Discovery Call <i class="fas fa-arrow-right"></i></a>
        <div class="book-cta-alt">
          Procurement, RFP or enterprise enquiry? Email <a href="mailto:info@thealphanova.com">info@thealphanova.com</a> or call <a href="tel:+14374245384">+1 437 424 5384</a>
        </div>
      </div>
    </div>
  </section>
"""

FOOTER = """
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="logo"><img src="img/wp/tan-e1764091769895.png" alt="The Alpha Nova"></a>
          <p>Your Canadian partner for AI, software and IoT. We design, build and integrate technology for intelligent products and industrial systems.</p>
          <p style="margin-top: 12px; font-size: 13px;">
            &#127464;&#127462; Proudly built in Canada
          </p>
          <div class="grant-badge">
            <a href="https://elevenlabs.io/startup-grants" target="_blank" rel="noopener">
              <img src="https://eleven-public-cdn.elevenlabs.io/payloadcms/cy7rxce8uki-IIElevenLabsGrants%201.webp" alt="ElevenLabs Grants">
            </a>
          </div>
        </div>
        <div>
          <h4>Services</h4>
          <ul class="footer-links">
            <li><a href="/ai-development">AI Development</a></li>
            <li><a href="/industrial-iot">Industrial &amp; IoT</a></li>
            <li><a href="/custom-software-development">Custom Software</a></li>
            <li><a href="/mobile-app-development">Mobile App Development</a></li>
            <li><a href="/software-modernization">Software Modernization</a></li>
            <li><a href="/services">All Services</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="/about">About Us</a></li>
            <li><a href="/case-studies">Case Studies</a></li>
            <li><a href="/industries">Industries</a></li>
            <li><a href="/products">Products</a></li>
            <li><a href="https://labs.thealphanova.com/">AN Labs</a></li>
            <li><a href="/public-sector">Public Sector</a></li>
            <li><a href="/software-development-sudbury">Software Development Sudbury</a></li>
            <li><a href="/book">Book a Call</a></li>
          </ul>
        </div>
        <div class="footer-contact">
          <h4>Contact</h4>
          <p>1545 Maley Drive, Greater Sudbury,<br>ON, P3A 4R7, Canada</p>
          <p><a href="mailto:info@thealphanova.com">info@thealphanova.com</a></p>
          <p><a href="tel:+14374245384">+1 437 424 5384</a></p>
          <div class="footer-social">
            <a href="https://www.facebook.com/theAlphaNova/" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="https://www.instagram.com/thealphanova" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://www.linkedin.com/company/the-alpha-nova" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        &copy; 2026 The Alpha Nova - Get Stuff Done. All rights reserved.
      </div>
    </div>
  </footer>

  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css">
  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
  <script src="js/main.js"></script>
</body>
</html>
"""


def faq_schema(faqs):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(data, indent=2).replace('\n', '\n  ')
            + '\n  </script>\n')


def service_schema(name, desc, slug):
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": desc,
        "serviceType": name,
        "url": f"https://thealphanova.com/{slug}",
        "provider": {
            "@type": "ProfessionalService",
            "name": "The Alpha Nova",
            "url": "https://thealphanova.com",
            "telephone": "+1-437-424-5384",
            "email": "info@thealphanova.com",
        },
        "areaServed": [{"@type": "Country", "name": "Canada"}],
    }
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(data, indent=2).replace('\n', '\n  ')
            + '\n  </script>\n')


def faq_html(faqs):
    items = []
    for q, a in faqs:
        items.append(f"""        <div class="faq-item">
          <button class="faq-item-q" aria-expanded="false">{q}</button>
          <div class="faq-item-a"><p>{a}</p></div>
        </div>""")
    return '\n'.join(items)


def service_page(s):
    caps = '\n'.join(
        f"""        <div class="cap-card">
          <i class="fas {c['icon']}"></i>
          <h3>{c['title']}</h3>
          <p>{c['body']}</p>
        </div>""" for c in s['capabilities'])

    projects = '\n'.join(
        f"""        <a href="/{p['slug']}" class="case-card">
          <div class="case-card-image"><img src="{p['img']}" alt="{p['title']}"></div>
          <div class="case-card-content">
            <h3>{p['title']}</h3>
            <p>{p['body']}</p>
            <span class="read-more">Read More <i class="fas fa-arrow-right"></i></span>
          </div>
        </a>""" for p in s['projects'])

    chips = '\n'.join(f'        <span class="tech-chip">{t}</span>' for t in s['tech'])

    steps = '\n'.join(
        f"""        <div class="process-step">
          <h3>{st['title']}</h3>
          <p>{st['body']}</p>
        </div>""" for st in s['process'])

    t = s['testimonial']

    schema = service_schema(s['h1'], s['desc'], s['slug']) + faq_schema(s['faqs'])

    return (
        head(s['title'], s['desc'], s['slug'], schema)
        + header('services')
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">{s['label']}</span>
      <h1>{s['h1']}</h1>
      <p style="max-width:760px; margin:18px auto 0;">{s['intro']}</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Book a Discovery Call <i class="fas fa-arrow-right"></i></a>
        <a href="/case-studies" class="btn btn-secondary">View Our Work</a>
      </div>
    </div>
  </section>

  <!-- Capabilities -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Capabilities</span>
        <h2>{s['cap_heading']}</h2>
        <p>{s['cap_sub']}</p>
      </div>
      <div class="cap-grid scroll-reveal">
{caps}
      </div>
    </div>
  </section>

  <!-- Relevant projects -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Relevant Work</span>
        <h2>Projects Like Yours</h2>
        <p>{s['projects_sub']}</p>
      </div>
      <div class="case-studies-grid scroll-reveal">
{projects}
      </div>
    </div>
  </section>

  <!-- Technologies -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Technology</span>
        <h2>What We Build With</h2>
        <p>We choose tools to fit the problem and your team's ability to maintain them, not the other way round.</p>
      </div>
      <div class="tech-chips scroll-reveal">
{chips}
      </div>
    </div>
  </section>

  <!-- Process -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">How We Work</span>
        <h2>From First Call to Production</h2>
        <p>No long discovery invoices before anyone writes code. We aim to have you looking at working software early.</p>
      </div>
      <div class="process-steps scroll-reveal">
{steps}
      </div>
    </div>
  </section>

  <!-- Testimonial -->
  <section class="section">
    <div class="container">
      <div class="hero-quote scroll-reveal">
        <blockquote>&ldquo;{t['quote']}&rdquo;</blockquote>
        <div class="hero-quote-author">
          <img src="{t['img']}" alt="{t['name']}">
          <div>
            <h4>{t['name']}</h4>
            <p>{t['role']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">FAQ</span>
        <h2>Frequently Asked Questions</h2>
      </div>
      <div class="faq-list">
{faq_html(s['faqs'])}
      </div>
    </div>
  </section>
"""
        + BOOK_CTA
        + FOOTER
    )


# ── Shared fragments ────────────────────────────────────────────────
T_MORITZ = {
    'quote': "Their understanding of complex healthcare requirements and ability to translate them into engaging gamified experiences was outstanding. We wouldn't be where we are today without them.",
    'name': 'Prof. Steffen Moritz', 'role': 'UKE Hamburg &middot; COGITO',
    'img': 'img/wp/Steffen_Moritz-e1764169958116-1.png',
}
T_LEHMANN = {
    'quote': 'The Alpha Nova consistently delivers high-quality software solutions with professionalism and precision. Their technical depth and collaborative approach make them an invaluable partner.',
    'name': 'Dr. Markus Lehmann', 'role': 'comAlpine Information System GmbH',
    'img': 'img/wp/Markus-v5.jpg',
}
T_BABYAK = {
    'quote': "After working with multiple agencies, I can confidently say The Alpha Nova is one of the most talented teams I've worked with so far. Their attention to detail and technical excellence is unmatched.",
    'name': 'Shaunna Babyak', 'role': 'Wheelit Transportation',
    'img': 'img/wp/Screenshot-2026-01-16-211156.png',
}
T_ALMUTAIRI = {
    'quote': 'Their team is nothing short of fantastic - extremely helpful, incredibly quick, and utterly professional in every interaction. The quality of their work speaks volumes about their creativity and skill.',
    'name': 'Abdulelah Almutairi', 'role': 'Aviation Executive',
    'img': 'img/wp/saudi.jpg',
}
T_BORSUTZKY = {
    'quote': 'Working with The Alpha Nova has been an excellent experience. The team is reliable, technically strong, and consistently focused on delivering practical solutions.',
    'name': 'Dr. Swantje Marie Borsutzky', 'role': 'Gl&uuml;cklich',
    'img': 'img/swantje.jpg',
}

P_COTE = {'slug': 'case-cote-gold', 'title': 'Côté Gold AI Challenge', 'img': 'img/cote-gold-winners.jpg',
          'body': 'Won 1st place analyzing open-pit mining blasts from drone footage, beating 29 teams from across Ontario.'}
P_COGITO = {'slug': 'case-cogito', 'title': 'COGITO with UKE Hamburg', 'img': 'img/wp/alpha-nova-cogito-pic.png',
            'body': 'A gamified mental-health platform built with one of Europe\'s leading university hospitals.'}
P_VANG = {'slug': 'case-vanguardian', 'title': 'VanGuardian Fall Detection', 'img': 'img/vanguardian-frame1.jpg',
          'body': 'AI-powered fall detection without wearables, running vision inference at the edge.'}
P_FLIGHT = {'slug': 'case-flight', 'title': 'AI Flight Data Platform', 'img': 'img/wp/Dribbble-shot-HD-8.jpg',
            'body': 'Real-time AI processing and analysis of complex aviation operations data.'}
P_CAMBRIAN = {'slug': 'case-cambrian', 'title': 'Cambrian Alumni App', 'img': 'img/wp/sambrian.png',
              'body': 'A cross-platform mobile app connecting an entire college alumni network.'}
P_WOBLU = {'slug': 'case-woblu', 'title': 'Woblu', 'img': 'img/woblu-team.jpg',
           'body': 'Award-winning on-demand home services app. 1st place and $18K in accelerator funding.'}
P_RESERVATION = {'slug': 'case-reservation', 'title': 'Reservation &amp; Fleet Management', 'img': 'img/wp/Dribbble-shot-HD-8.jpg',
                 'body': 'Real-time fleet tracking and reservation management for transportation operators.'}
P_XML = {'slug': 'case-cogito-xml', 'title': 'COGITO XML Engine', 'img': 'img/wp/alpha-nova-cogito-pic.png',
         'body': 'An enterprise XML processing engine for industrial automation, transforming and integrating data across manufacturing and clinical research systems.'}

STD_PROCESS = [
    {'title': 'Discovery Call', 'body': 'Thirty minutes. You describe the problem, we ask hard questions and tell you how we would approach it, including if we are not the right team.'},
    {'title': 'Scope &amp; Architecture', 'body': 'We define the smallest version that proves the hard part, agree the technical approach, and give you a fixed plan with milestones.'},
    {'title': 'Build in Increments', 'body': 'Working software in front of you on a regular cadence, so direction changes stay cheap and surprises surface early.'},
    {'title': 'Launch &amp; Maintain', 'body': 'Deployment, monitoring and ongoing support. We build systems we expect to still be maintaining in three years.'},
]

SERVICES = [
    {
        'slug': 'ai-development',
        'title': 'AI Development & Computer Vision | The Alpha Nova',
        'desc': 'Applied AI, machine learning and computer vision systems built for production against real-world data. Award-winning mining vision work, clinical platforms and edge intelligence.',
        'label': 'AI Development',
        'h1': 'Applied AI &amp; Computer Vision',
        'intro': 'Most AI projects die between the notebook and production. We build the systems that survive the crossing, models that run against messy real-world data, on real hardware, with the monitoring to prove they still work next quarter.',
        'cap_heading': 'What We Build',
        'cap_sub': 'Applied machine learning for organizations with real data problems, not demo datasets.',
        'capabilities': [
            {'icon': 'fa-eye', 'title': 'Computer Vision', 'body': 'Object detection, segmentation and tracking on imagery from drones, fixed cameras and inspection rigs. Our Côté Gold blast-analysis system took first place against 29 teams.'},
            {'icon': 'fa-microchip', 'title': 'Edge Intelligence', 'body': 'Inference that runs on-device where bandwidth is scarce or latency matters, rather than shipping every frame to a cloud that may not be reachable.'},
            {'icon': 'fa-chart-line', 'title': 'Predictive Analytics', 'body': 'Forecasting and anomaly detection over telemetry and operational history, built so the output lands in the tools your team already uses.'},
            {'icon': 'fa-comments', 'title': 'Language &amp; Document AI', 'body': 'Extraction, classification and summarization over the documents and free text your operation generates, with human review where accuracy is non-negotiable.'},
            {'icon': 'fa-vial', 'title': 'Proof of Concept', 'body': 'A focused build that answers whether the hard part is achievable at all, before anyone commits to a full programme. Typically weeks, not quarters.'},
            {'icon': 'fa-shield-halved', 'title': 'Production Hardening', 'body': 'Monitoring, drift detection, retraining pipelines and fallbacks, the work that separates a model that demos from a model that operates.'},
        ],
        'projects_sub': 'Vision and AI systems we have taken from problem statement to working deployment.',
        'projects': [P_COTE, P_VANG, P_FLIGHT],
        'tech': ['Python', 'PyTorch', 'TensorFlow', 'OpenCV', 'YOLO', 'ONNX Runtime', 'NVIDIA Jetson', 'CUDA', 'FastAPI', 'Docker', 'AWS', 'Azure'],
        'process': STD_PROCESS,
        'testimonial': T_MORITZ,
        'faqs': [
            ('Do we need a large labelled dataset before we start?', 'Not always. We often begin by assessing what data you already have and whether a smaller labelled set, transfer learning or synthetic augmentation can carry a first version. Part of the discovery call is working out whether your data can support the result you want.'),
            ('Can the model run without a reliable internet connection?', 'Yes. Edge deployment is a core part of our work, running inference on-device for environments where connectivity is intermittent or absent, which is the normal case in mining and industrial settings.'),
            ('How do you prove the AI actually works before we commit?', 'We scope a proof of concept against your data with agreed success criteria defined up front. If it does not clear the bar, you have an inexpensive and definitive answer rather than a half-finished programme.'),
            ('Who owns the models and the code?', 'You do. Ownership of the code and trained models transfers to you, and we document them so another team could pick them up.'),
        ],
    },
    {
        'slug': 'custom-software-development',
        'title': 'Custom Software Development | The Alpha Nova',
        'desc': 'Custom software engineering for organizations with complex requirements. Platforms, APIs and data systems built to your requirements and maintained long term.',
        'label': 'Custom Software',
        'h1': 'Custom Software Development',
        'intro': 'When the off-the-shelf product almost fits, the gap is usually where your actual advantage lives. We build the software that closes it, platforms, APIs and data systems designed around how your organization really works.',
        'cap_heading': 'What We Build',
        'cap_sub': 'Systems designed for the requirements you actually have, and for the team who will maintain them.',
        'capabilities': [
            {'icon': 'fa-diagram-project', 'title': 'Platform &amp; Product Engineering', 'body': 'Multi-tenant platforms, internal tools and customer-facing products, architected so adding the next feature does not require rewriting the last one.'},
            {'icon': 'fa-plug', 'title': 'APIs &amp; Integration', 'body': 'Connecting systems that were never designed to talk to each other, including legacy databases, third-party services and industrial equipment.'},
            {'icon': 'fa-database', 'title': 'Data Engineering', 'body': 'Schema design, pipelines and reporting layers that keep data trustworthy as volume grows and requirements change.'},
            {'icon': 'fa-pen-ruler', 'title': 'Product Design &amp; UX', 'body': 'Interface and workflow design grounded in how the work is actually done, so the software gets used rather than worked around.'},
            {'icon': 'fa-lock', 'title': 'Security &amp; Compliance', 'body': 'Authentication, access control, audit trails and data handling appropriate to regulated environments including healthcare and research.'},
            {'icon': 'fa-arrows-rotate', 'title': 'Long-Term Maintenance', 'body': 'Ongoing support, dependency upkeep and feature work. Most of our clients stay with us well past the initial launch.'},
        ],
        'projects_sub': 'Platforms and systems we have designed, built and continue to support.',
        'projects': [P_COGITO, P_RESERVATION, P_FLIGHT],
        'tech': ['React', 'Node.js', 'TypeScript', 'Python', 'PostgreSQL', 'MongoDB', 'Redis', 'GraphQL', 'Docker', 'Kubernetes', 'AWS', 'Azure'],
        'process': STD_PROCESS,
        'testimonial': T_LEHMANN,
        'faqs': [
            ('How do you price a custom build?', 'After the discovery call we scope the work and give you a fixed plan with milestones rather than an open-ended hourly arrangement. If the scope genuinely changes mid-project, we re-baseline openly instead of absorbing it silently.'),
            ('What happens if our requirements change halfway through?', 'They usually do. We build in increments precisely so that changing direction is cheap, you see working software regularly and can redirect the next increment rather than discovering a mismatch at handover.'),
            ('Can you work alongside our existing in-house team?', 'Yes. We regularly work as an extension of an internal team, taking a defined component or supplying the specialist capability the team lacks, with shared repositories and review process.'),
            ('What do we get at the end?', 'The code, the infrastructure definitions, the documentation and a system your own developers can maintain. No proprietary lock-in and no black boxes.'),
        ],
    },
    {
        'slug': 'mobile-app-development',
        'title': 'Mobile App Development | iOS & Android | The Alpha Nova',
        'desc': 'Cross-platform and native mobile app development for iOS and Android. Healthcare, education and consumer apps shipped for universities, colleges and startups.',
        'label': 'Mobile Development',
        'h1': 'Mobile App Development',
        'intro': 'Mobile is where most people will actually meet your product. We build apps for iOS and Android that hold up under real use, offline, on old devices, on bad connections, and that you can keep shipping updates to for years.',
        'cap_heading': 'What We Build',
        'cap_sub': 'Apps that survive the app store review, the security questionnaire and the second year of maintenance.',
        'capabilities': [
            {'icon': 'fa-mobile-screen', 'title': 'Cross-Platform Apps', 'body': 'One codebase serving iOS and Android at native quality, which is usually the right economics unless you have a specific reason to go native.'},
            {'icon': 'fa-apple', 'title': 'Native iOS &amp; Android', 'body': 'Fully native builds where the app depends on deep platform integration, demanding performance or specialised hardware access.'},
            {'icon': 'fa-wifi', 'title': 'Offline-First Design', 'body': 'Local persistence and sync so the app keeps working underground, in transit or anywhere the signal drops, then reconciles cleanly when it returns.'},
            {'icon': 'fa-bell', 'title': 'Notifications &amp; Engagement', 'body': 'Scheduled and event-driven notifications that respect the user rather than nagging them, with the analytics to see what actually drives return visits.'},
            {'icon': 'fa-heart-pulse', 'title': 'Regulated &amp; Clinical Apps', 'body': 'Applications handling health and research data, built with the consent flows, audit trails and data handling those settings require.'},
            {'icon': 'fa-rocket', 'title': 'Store Launch &amp; Iteration', 'body': 'Release pipelines, store submission, staged rollout and the ongoing update cadence that keeps an app from quietly rotting.'},
        ],
        'projects_sub': 'Mobile applications delivered for universities, colleges, health researchers and startups.',
        'projects': [P_CAMBRIAN, P_COGITO, P_WOBLU],
        'tech': ['Flutter', 'React Native', 'Swift', 'Kotlin', 'Dart', 'Firebase', 'Node.js', 'PostgreSQL', 'App Store Connect', 'Google Play'],
        'process': STD_PROCESS,
        'testimonial': T_BABYAK,
        'faqs': [
            ('Should we build cross-platform or native?', 'Cross-platform is the right default for most products, one codebase, both platforms, materially lower cost to maintain. We recommend native when the app leans hard on platform-specific capability or needs performance that a shared runtime cannot deliver. We will tell you which case you are in on the call.'),
            ('Do you handle App Store and Google Play submission?', 'Yes, including the review process, store listings, staged rollouts and the inevitable rejection round-trips. We can publish under your developer accounts so you retain ownership.'),
            ('Can the app work without an internet connection?', 'Yes. Offline-first architecture is something we build routinely, with local storage and conflict-aware sync rather than an app that simply fails when the signal drops.'),
            ('What does maintaining an app actually involve?', 'Roughly: keeping up with annual iOS and Android releases, dependency and security updates, and store policy changes. Budgeting for ongoing maintenance is the difference between an app that lasts and one that breaks in eighteen months.'),
        ],
    },
    {
        'slug': 'industrial-iot',
        'title': 'Industrial IoT & Edge Systems | The Alpha Nova',
        'desc': 'Industrial IoT, telemetry and edge intelligence for mining, heavy industry and safety-critical operations. Built for environments where connectivity is poor and downtime is expensive.',
        'label': 'Industrial &amp; IoT',
        'h1': 'Industrial &amp; IoT Systems',
        'intro': 'Industrial software fails for unglamorous reasons: the network drops, the sensor lies, the device is covered in dust and nobody can reach it. We build monitoring and edge systems that assume all of that and keep working anyway.',
        'cap_heading': 'What We Build',
        'cap_sub': 'Systems for environments where a failed deployment means a truck roll, or worse.',
        'capabilities': [
            {'icon': 'fa-satellite-dish', 'title': 'Telemetry &amp; Monitoring', 'body': 'Collecting, validating and storing sensor data at scale, with the gap-handling and clock-skew tolerance that field deployments always turn out to need.'},
            {'icon': 'fa-microchip', 'title': 'Edge Computing', 'body': 'Processing on-site so decisions do not wait on a round trip, and so a lost connection degrades the system rather than stopping it.'},
            {'icon': 'fa-video', 'title': 'Industrial Computer Vision', 'body': 'Automated inspection and site analysis from fixed cameras and drone imagery, the discipline behind our first-place Côté Gold blast-analysis work.'},
            {'icon': 'fa-triangle-exclamation', 'title': 'Safety &amp; Alerting', 'body': 'Detection and escalation paths for safety-critical events, including our VanGuardian fall-detection work that requires no wearable device.'},
            {'icon': 'fa-gauge-high', 'title': 'Operational Dashboards', 'body': 'Interfaces built for a control room and a phone in a truck, not just for a desk, readable at a glance and honest about stale data.'},
            {'icon': 'fa-screwdriver-wrench', 'title': 'Legacy Equipment Integration', 'body': 'Getting data out of machinery and control systems that predate the internet, without disturbing the process they are running.'},
        ],
        'projects_sub': 'Industrial and safety-critical systems built for demanding physical environments.',
        'projects': [P_COTE, P_VANG, P_FLIGHT],
        'tech': ['Python', 'MQTT', 'InfluxDB', 'TimescaleDB', 'Grafana', 'NVIDIA Jetson', 'Docker', 'Rust', 'Node.js', 'AWS IoT', 'Azure IoT'],
        'process': STD_PROCESS,
        'testimonial': T_ALMUTAIRI,
        'faqs': [
            ('Our site has almost no connectivity. Is that a problem?', 'It is the normal case, and it shapes the architecture rather than blocking it. We design for local processing and store-and-forward sync, so the system operates on-site and reconciles when a link is available.'),
            ('Can you integrate with equipment we already have?', 'Usually. We work with existing sensors, PLCs and control systems, reading data out through whatever interface is available rather than requiring you to replace working machinery.'),
            ('How do you handle safety-critical alerting?', 'With explicit failure modes: defined escalation paths, alerting on the absence of data as well as on bad data, and a clear position on what the system does when it is uncertain. We design these rules with your operations team, not for them.'),
            ('Do you work on-site?', 'For industrial deployments, yes, commissioning and field validation generally require being there. Our Sudbury base puts us in the middle of Ontario mining country.'),
        ],
    },
    {
        'slug': 'software-modernization',
        'title': 'Legacy Software Modernization | The Alpha Nova',
        'desc': 'Modernize legacy software without a risky rewrite. Incremental migration, re-architecture and integration for systems you cannot afford to switch off.',
        'label': 'Modernization',
        'h1': 'Software Modernization',
        'intro': 'The system works, nobody wants to touch it, and the people who wrote it have left. Rewriting from scratch is how most of these projects fail. We modernize incrementally, so the business keeps running while the software gets better.',
        'cap_heading': 'What We Do',
        'cap_sub': 'Reducing risk on systems that are load-bearing for your operation.',
        'capabilities': [
            {'icon': 'fa-magnifying-glass-chart', 'title': 'Assessment &amp; Roadmap', 'body': 'An honest read on what you have, what is genuinely at risk, and what the sequence should be, including the parts we would advise leaving alone.'},
            {'icon': 'fa-layer-group', 'title': 'Incremental Migration', 'body': 'Moving functionality piece by piece behind a stable interface, so value arrives continuously instead of on a single high-risk cutover date.'},
            {'icon': 'fa-cloud-arrow-up', 'title': 'Cloud &amp; Infrastructure', 'body': 'Containerization, deployment automation and hosting moves that reduce operational fragility rather than simply relocating it.'},
            {'icon': 'fa-database', 'title': 'Data Migration', 'body': 'Moving and reconciling data between old and new systems with validation at each step, because this is where most modernizations actually come apart.'},
            {'icon': 'fa-vials', 'title': 'Test Coverage', 'body': 'Building a safety net around undocumented behaviour first, so changes can be made with evidence rather than hope.'},
            {'icon': 'fa-book', 'title': 'Documentation &amp; Handover', 'body': 'Capturing the knowledge that currently lives in one person\'s head, so the next change does not depend on their availability.'},
        ],
        'projects_sub': 'Systems we have re-architected, integrated and brought back under control.',
        'projects': [P_XML, P_RESERVATION, P_COGITO],
        'tech': ['Python', 'Node.js', 'TypeScript', 'PostgreSQL', 'Docker', 'Kubernetes', 'Terraform', 'GitHub Actions', 'AWS', 'Azure'],
        'process': STD_PROCESS,
        'testimonial': T_BORSUTZKY,
        'faqs': [
            ('Should we rewrite from scratch instead?', 'Almost never, and we will say so plainly. Full rewrites tend to run long, and the new system has to reproduce years of accumulated behaviour nobody documented. Incremental migration behind a stable interface is slower to sound impressive and much more likely to finish.'),
            ('Can you work on a system in a language nobody here still uses?', 'Frequently, yes. Much of the work is reading carefully and building tests around current behaviour before changing anything. Tell us what it is written in on the call and we will be straight about whether we are the right team.'),
            ('Will the system stay available during the work?', 'That is the point of the incremental approach. Functionality moves behind a stable interface with the option to route back, so there is no single cutover on which everything depends.'),
            ('How do you decide what to modernize first?', 'By risk and cost of failure rather than by how unpleasant the code is. The assessment ranks components by what breaking them would actually do to the business.'),
        ],
    },
]


def build_service_pages():
    for s in SERVICES:
        path = os.path.join(ROOT, s['slug'] + '.html')
        with open(path, 'w') as f:
            f.write(service_page(s))
        print('wrote', path)


if __name__ == '__main__':
    build_service_pages()
