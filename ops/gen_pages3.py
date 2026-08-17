#!/usr/bin/env python3
"""Generate /products and /cogito-ai."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_pages import (  # noqa: E402
    ROOT, head, header, FOOTER, BOOK_CTA, faq_schema, faq_html, T_MORITZ,
)

PRODUCTS = [
    ('Flagship', 'COGITO AI', '/cogito-ai',
     'A private, personalized AI companion for everyday mental wellbeing, developed with researchers at University Medical Center Hamburg-Eppendorf (UKE). Privacy-first and on-device, so sensitive conversations never need to leave the phone.'),
    ('Edge AI', 'VanGuardian', '/case-vanguardian',
     'Fall detection with no wearable device, using computer vision running at the edge. Built for environments where a missed fall has real consequences.'),
]


def products_page():
    cards = '\n'.join(f"""        <div class="product-card">
          <span class="product-stage">{stage}</span>
          <h3>{name}</h3>
          <p>{body}</p>
          <a href="{slug}" class="read-more">Explore {name} <i class="fas fa-arrow-right"></i></a>
        </div>""" for stage, name, slug, body in PRODUCTS)

    return (
        head('Products | COGITO AI & VanGuardian | The Alpha Nova',
             'Products built by The Alpha Nova: COGITO AI for mental-health technology, and VanGuardian for edge computer vision.',
             'products')
        + header('products')
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">Products</span>
      <h1>Technology We Build for Ourselves</h1>
      <p style="max-width:760px; margin:18px auto 0;">Most of our work is built for clients. These are the problems we chose ourselves, where we took the same engineering and pushed it further than a project brief would allow.</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Book a Discovery Call <i class="fas fa-arrow-right"></i></a>
        <a href="/case-studies" class="btn btn-secondary">See Our Work</a>
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
      <div class="section-header">
        <span class="section-label">Why It Matters</span>
        <h2>Products Sharpen the Practice</h2>
        <p>Owning a product means living with the decisions. The offline-first architecture behind COGITO AI, and the edge inference behind VanGuardian, both came back into client work, which is the point.</p>
      </div>
    </div>
  </section>
"""
        + BOOK_CTA + FOOTER)


COGITO_FAQS = [
    ('What is COGITO AI?',
     'COGITO AI is an intelligent mental wellbeing companion developed in collaboration with researchers at University Medical Center Hamburg-Eppendorf (UKE), Germany. It builds on the principles and research behind the COGITO self-help app, exploring how artificial intelligence can make evidence-based mental health exercises more personalized, engaging and accessible.'),
    ('How is it private if it uses AI?',
     'By not sending your conversations anywhere. Unlike traditional cloud-based AI assistants, COGITO AI is designed with a privacy-first, on-device approach, personalization happens on your own device, without shipping sensitive conversations or personal information to external AI servers.'),
    ('Is it a chatbot?',
     'No. The experience is built around focused guidance rather than unrestricted AI chat. The companion helps you work through evidence-informed activities, remembers what you have already done, and supports regular check-ins, it is deliberately constrained.'),
    ('Does it diagnose or treat anything?',
     'No. AI interactions are intentionally constrained and designed for wellbeing support, not diagnosis or clinical treatment. Safety-first design is a deliberate constraint on what the companion will do.'),
    ('What does it remember?',
     'Completed activities, previous sessions and your preferences, so guidance carries continuity between sessions rather than starting cold each time, and recommendations reflect what you have actually engaged with.'),
    ('What is The Alpha Nova\'s role?',
     'We work with the COGITO research team on the technical development and AI architecture: privacy-preserving AI, personalization, on-device intelligence, user experience, multilingual capabilities and scalable mobile technology.'),
]


def cogito_ai_page():
    caps = [
        ('fa-mobile-screen', 'On-Device AI', 'Designed to keep sensitive information on the user&rsquo;s device, rather than routing personal conversations through external AI servers.'),
        ('fa-wand-magic-sparkles', 'Personalized Guidance', 'Recommends exercises based on previous interactions and preferences, so the next suggestion reflects what has actually helped.'),
        ('fa-clock-rotate-left', 'Context and Memory', 'Remembers completed activities and previous sessions to provide continuity, instead of starting from nothing each time.'),
        ('fa-compass', 'AI-Guided Exercises', 'Helps users understand and work through evidence-informed activities, with focused guidance rather than open-ended chat.'),
        ('fa-calendar-check', 'Weekly Check-Ins', 'Encourages reflection and continued engagement over time, the part most wellbeing tools lose people on.'),
        ('fa-language', 'Multilingual Experience', 'Designed to make support accessible across different languages and communities.'),
        ('fa-face-smile', 'Interactive AI Companion', 'A friendly visual companion, so the experience feels like something you return to rather than a form you fill in.'),
        ('fa-shield-heart', 'Safety-First Design', 'AI interactions are intentionally constrained and designed for wellbeing support, not diagnosis, and not clinical treatment.'),
    ]
    cap_html = '\n'.join(f"""        <div class="cap-card">
          <i class="fas {i}"></i>
          <h3>{t}</h3>
          <p>{b}</p>
        </div>""" for i, t, b in caps)

    return (
        head('COGITO AI | Private, On-Device AI for Mental Wellbeing | The Alpha Nova',
             'COGITO AI is a private, personalized AI companion for everyday mental wellbeing, developed with researchers at University Medical Center Hamburg-Eppendorf (UKE). Privacy-first and on-device.',
             'cogito-ai',
             faq_schema(COGITO_FAQS))
        + header('products')
        + f"""
  <section class="page-hero">
    <div class="container">
      <span class="section-label">Flagship Product</span>
      <h1>COGITO AI</h1>
      <p style="max-width:780px; margin:18px auto 0;"><strong>Private, personalized AI for everyday mental wellbeing.</strong></p>
      <p style="max-width:780px; margin:14px auto 0;">An intelligent mental wellbeing companion developed in collaboration with researchers at University Medical Center Hamburg-Eppendorf (UKE), Germany.</p>
      <div class="hero-buttons" style="justify-content:center; margin-top:32px;">
        <a href="/book" class="btn btn-primary" data-calendly>Talk to Us About COGITO AI <i class="fas fa-arrow-right"></i></a>
        <a href="/case-cogito" class="btn btn-secondary">Read the COGITO Case Study</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">The Idea</span>
        <h2>Personalization Without Surveillance</h2>
        <p>Building on the principles and research behind the COGITO self-help app, COGITO AI explores how artificial intelligence can make evidence-based mental health exercises more personalized, engaging and accessible.</p>
      </div>
      <div class="cap-grid cap-grid-2 scroll-reveal" style="max-width:900px;margin:0 auto;">
        <div class="cap-card">
          <i class="fas fa-cloud-arrow-up"></i>
          <h3>The usual trade-off</h3>
          <p>Cloud AI assistants personalize by sending your conversations to someone else&rsquo;s servers. For mental health, that is a steep price to pay for a recommendation.</p>
        </div>
        <div class="cap-card">
          <i class="fas fa-lock"></i>
          <h3>The approach here</h3>
          <p>A privacy-first, on-device design allows personalization without requiring users to send sensitive conversations or personal information to external AI servers.</p>
        </div>
      </div>
      <p style="max-width:760px;margin:34px auto 0;text-align:center;color:var(--secondary-text);line-height:1.8;">
        The companion remembers previous exercises and preferences, provides personalized recommendations, guides users through activities, summarizes progress and supports regular check-ins, built around focused guidance rather than unrestricted AI chat.
      </p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Capabilities</span>
        <h2>What COGITO AI Does</h2>
      </div>
      <div class="cap-grid scroll-reveal">
{cap_html}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-label">Our Role</span>
        <h2>What The Alpha Nova Does Here</h2>
        <p>We work with the COGITO research team on the technical development and AI architecture of COGITO AI, privacy-preserving AI, personalization, on-device intelligence, user experience, multilingual capabilities and scalable mobile technology.</p>
      </div>
      <p style="max-width:760px;margin:0 auto;text-align:center;color:var(--secondary-text);line-height:1.8;">
        The goal is to demonstrate how AI can enhance evidence-based digital mental health tools while keeping <strong>privacy, accessibility, safety and scientific validation</strong> at the centre of the experience.
      </p>
      <div class="hero-quote scroll-reveal" style="margin-top:46px;">
        <blockquote>&ldquo;{T_MORITZ['quote']}&rdquo;</blockquote>
        <div class="hero-quote-author">
          <img src="{T_MORITZ['img']}" alt="{T_MORITZ['name']}">
          <div>
            <h4>{T_MORITZ['name']}</h4>
            <p>University Medical Center Hamburg-Eppendorf (UKE)</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-label">FAQ</span>
        <h2>Frequently Asked Questions</h2>
      </div>
      <div class="faq-list">
{faq_html(COGITO_FAQS)}
      </div>
    </div>
  </section>
"""
        + BOOK_CTA + FOOTER)


if __name__ == '__main__':
    for name, fn in {'products.html': products_page, 'cogito-ai.html': cogito_ai_page}.items():
        path = os.path.join(ROOT, name)
        open(path, 'w').write(fn())
        print('wrote', path)
