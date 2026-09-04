> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

**INTERNAL DRAFT: NOT FOR SUBMISSION**

# Software Development and Innovation

# THE ALPHA NOVA INC.

## AI-Enabled Customer-Service Automation
## CRM + Website Chatbot
## + Telephone Callbot

A bundled, bilingual CRM, website chatbot, and telephone callbot that answer only from CICIC-approved content, cite their sources, and route uncertain or sensitive inquiries to staff.

**www.thealphanova.com**

### SUBMITTED TO

The Corporation of the Council of Ministers of Education, Canada (CCMEC)  
Owner: Canadian Information Centre for International Credentials (CICIC)  
Attention: Michael Ringuette, Coordinator, CICIC  
95 St. Clair Avenue West, Suite 1106  
Toronto ON M4V 1N6  
m.ringuette@cmec.ca | 416-962-9725 ext. 271

### SUBMITTED BY

The Alpha Nova Inc.  
1545 Maley Drive  
Greater Sudbury ON P3A 4R7  
info@thealphanova.com | +1 437 424 5384  
thealphanova.com | labs.thealphanova.com

### SUBMISSION DATE

4 September 2026, internal draft date only

**Solicitation:** 2026-CICIC-01  
**MERX:** 0000330086  
**Source ID:** PV.MN.ON.383381.C111700  
**Solicitation type:** RFQ Formal  
**Closing:** 18 September 2026, 4:00 p.m. EDT  
**Proposed initial term:** 1 April 2027, 9:00 a.m. EDT to 31 March 2028, 9:00 a.m. EDT  
**Components bid:** All three components as one bundled proposal

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

## Table of Contents

1. [Understanding of the Project](#1-understanding-of-the-project)  
   1.1 [CICIC's mandate defines the product boundary](#11-cicics-mandate-defines-the-product-boundary)  
   1.2 [The operational opportunity](#12-the-operational-opportunity)  
   1.3 [Three components, one controlled service chain](#13-three-components-one-controlled-service-chain)  
   1.4 [A governed knowledge base, not an open-ended AI assistant](#14-a-governed-knowledge-base-not-an-open-ended-ai-assistant)  
   1.5 [Non-negotiable operating rules](#15-non-negotiable-operating-rules)  
   1.6 [What success looks like](#16-what-success-looks-like)
2. [Relevant Experience & References](#2-relevant-experience--references)  
   2.1 [About The Alpha Nova](#21-about-the-alpha-nova)  
   2.2 [Why we are a strong fit](#22-why-we-are-a-strong-fit)  
   2.3 [Core Project Team](#23-core-project-team)  
   2.4 [Relevant public work](#24-relevant-public-work)  
   2.5 [References](#25-references)
3. [Technical Architecture & Scalability](#3-technical-architecture--scalability)  
   3.1 [Architecture principles](#31-architecture-principles)  
   3.2 [Logical architecture](#32-logical-architecture)  
   3.3 [Knowledge ingestion and governance](#33-knowledge-ingestion-and-governance)  
   3.4 [Grounded response pipeline](#34-grounded-response-pipeline)  
   3.5 [Channel design](#35-channel-design)  
   3.6 [Identity, authorization, and tier enforcement](#36-identity-authorization-and-tier-enforcement)  
   3.7 [Security, privacy, residency, and portability](#37-security-privacy-residency-and-portability)  
   3.8 [Accessibility and bilingual delivery](#38-accessibility-and-bilingual-delivery)  
   3.9 [Auditability, measurement, and service levels](#39-auditability-measurement-and-service-levels)  
   3.10 [Scalability and maintainability](#310-scalability-and-maintainability)
4. [Work Plan & Delivery Approach](#4-work-plan--delivery-approach)  
   4.1 [Delivery sequence](#41-delivery-sequence)  
   4.2 [Governance and working model](#42-governance-and-working-model)  
   4.3 [Quality assurance and acceptance](#43-quality-assurance-and-acceptance)  
   4.4 [Training, documentation, and support](#44-training-documentation-and-support)  
   4.5 [CICIC and CCMEC responsibilities](#45-cicic-and-ccmec-responsibilities)  
   4.6 [Risks and controls](#46-risks-and-controls)  
   4.7 [Transition and end-of-term portability](#47-transition-and-end-of-term-portability)
5. [Budget](#5-budget)
6. [Appendix A: Key Team Resumes](#appendix-a-key-team-resumes)
7. [Appendix B: R1-R22 Compliance Matrix](#appendix-b-r1-r22-compliance-matrix)
8. [INTERNAL Athif Checklist](#internal-athif-checklist-strip-before-bid)

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# 1. Understanding of the Project

## 1.1 CICIC's mandate defines the product boundary

CICIC provides information and referrals concerning the recognition of academic and occupational credentials. It does not assess or recognize credentials and it does not decide individual cases. That distinction is not background context to be placed in a disclaimer and forgotten. It is the central product rule.

The proposed system must help a person find the correct CICIC-approved information, understand the appropriate next step, and reach the proper authority. It must not replace the provincial or territorial authority responsible for education, the autonomy of a post-secondary institution, the jurisdiction of a professional regulator, or the role of an Alliance of Credential Evaluation Services of Canada member. When a request crosses from information into assessment, recognition, comparison, interpretation of an individual's documents, or a decision, the system must stop answering and refer or escalate.

We therefore propose a controlled service model in which CICIC remains the author, publisher, and authority. The technology retrieves approved material, assembles a cited response, applies CICIC's disposition and escalation rules, and records the interaction. Staff remain in control of content, exceptions, and any external communication that requires review. The system supports the mandate. It does not expand it.

## 1.2 The operational opportunity

CICIC has already moved a substantial share of service demand to self-service. The website receives approximately 770,000 sessions and 2.1 million page views each year. Connect.the.dots handles approximately 6,000 guided reports, while the automated telephone menu handles approximately 1,800 calls. Three staff members handle approximately 2,560 email and telephone inquiries a year, about four in five in writing and one in five by telephone, with one person acting as the primary point of contact.

The existing custom CRM dates from 2010, Connect.the.dots from 2015, and the VoIP menu from 2019. Together, these tools have helped reduce staff-assisted inquiries by approximately 63 percent over a decade. The remaining constraint is not a lack of content or willingness to self-serve. It is the limit of fixed navigation trees. A fixed tree can ask a person to choose a category. It cannot reliably interpret how that person describes their situation, find the relevant approved passage across a bilingual corpus, explain the referral path, cite the source, and recognize when not to answer.

The next gain should come from better interpretation and routing, not from removing human judgement. CICIC's staff should spend less time locating repeatable information and more time handling exceptions, maintaining content, reviewing sensitive drafts, and addressing inquiries that genuinely require their expertise.

The language profile also shapes the solution. Approximately 70 percent of demand is in English and 30 percent is in French. French is therefore a production language and an acceptance stream, not a translation task deferred until the end. Content, retrieval, prompts, interface behaviour, voice scripts, fallback behaviour, testing, and reporting must all work in both official languages.

## 1.3 Three components, one controlled service chain

The Alpha Nova is bidding the required three components together:

1. **CRM:** the operational spine for intake, case records, taxonomy, assignments, escalation, human review, audit history, and reporting.
2. **Website chatbot:** a public self-service surface for Tier 1 information, with AI disclosure, source citations, mandate disclaimers, confidence controls, and handover to the CRM.
3. **Telephone callbot:** a bilingual voice surface that identifies itself, uses controlled scripts for critical statements, retrieves approved information for eligible questions, and transfers or arranges follow-up when an answer is not appropriate.

These are not three unrelated tools. A website conversation and a telephone conversation must enter the same staff workflow when human help is required. The handover should carry the language, inquiry category, relevant taxonomy node, trigger or disposition, transcript, citations, and confidence outcome already collected. Staff should not force the person to begin again, and CICIC should not need to reconcile three incompatible records.

The sequence also matters. The CRM and escalation model must exist before a public AI channel can safely hand work to staff. The knowledge and policy service must be shared so that web and voice apply the same mandate boundary, tier rules, approved sources, and escalation logic. Each channel can present information differently, but it cannot operate from a separate interpretation of CICIC policy.

One delivery team gives CCMEC one accountable integration path. It also reduces the risk that a chatbot vendor, a telephony vendor, and a CRM vendor each consider the handover to be someone else's responsibility.

## 1.4 A governed knowledge base, not an open-ended AI assistant

CICIC already owns the knowledge base to be served: approximately 75 items represented by 147 English and French files, organized through a taxonomy and divided into three sensitivity tiers:

| Tier | Intended access | Proposed enforcement |
|---|---|---|
| Tier 1 | Public | Eligible for the unauthenticated website chatbot and for public voice responses |
| Tier 2 | Authenticated | Retrieved only after verified authentication and authorization |
| Tier 3 | Internal | Available only to authorized CICIC staff within the internal workflow |

Each knowledge item also carries a disposition of answer, refer, or escalate. The technology must respect that disposition before it generates prose. An item marked refer should produce a referral based on approved wording. An item marked escalate should create or enrich a CRM handover. An answer is permitted only when the retrieved material and policy rules support it.

The proposed approach is closed-domain retrieval-augmented generation. CICIC's approved corpus is the only answer source. The model may help select, organize, and express retrieved material, but it receives no permission to search the open web or rely on its general training as evidence. Every substantive text answer must carry a citation that a user or staff member can inspect. When the corpus does not support an answer, the correct result is an abstention and a route to the next appropriate step.

Knowledge-base maintenance must not require model retraining. CICIC should be able to correct wording, add an approved file, change a tier, revise a disposition, or retire an item through a governed publishing workflow. The retrieval index then updates while retaining version and audit information. CICIC supplies and approves the content. The Alpha Nova will implement the system that serves it; we will not write CICIC's credential-recognition content.

## 1.5 Non-negotiable operating rules

We understand that the solution must never:

- assess, recognize, compare, or decide an individual's credentials;
- answer from the open web or treat a general-purpose model as an authoritative source;
- serve Tier 2 or Tier 3 content through an unauthenticated public channel;
- send an unreviewed AI-drafted external communication;
- present provincial or territorial content that CICIC has not validated;
- use CCMEC data, CICIC content, or inquiry data to train foundation models;
- invent an answer when the knowledge base does not support one;
- hide that a user is interacting with AI;
- continue a clarification loop when confidence remains below the configured threshold; or
- make a person repeat information that can be transferred safely and appropriately during human handover.

These rules will be implemented in retrieval filters, authorization checks, response policies, interface copy, deterministic voice blocks, test cases, and launch gates. A policy that exists only in project documentation is not enough.

## 1.6 What success looks like

Success is not the largest possible percentage of inquiries answered by AI. It is the largest safe and useful share answered or routed correctly within CICIC's mandate.

For a member of the public, success means receiving a clear answer in English or French, knowing that it was generated with AI, seeing the CICIC source behind it, understanding that CICIC does not decide their case, and reaching a human or the correct outside authority when the system should not answer.

For CICIC staff, success means one queue, consistent taxonomy, complete handover context, editable knowledge without retraining, review before external send, searchable audit history, and reports that show what the channels are doing. A staff member remains able to correct a category, override a route, review a draft, and identify the content and rule version used.

For CCMEC, success means a portable and auditable service with enforceable access boundaries, evidence of bilingual and accessible operation, controlled data handling, and measurable service levels. The system should make performance visible without turning aspirational targets into unbounded warranties.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# 2. Relevant Experience & References

## 2.1 About The Alpha Nova

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. We build intelligent software and industrial systems across four capabilities:

1. AI & Intelligent Systems
2. Industrial IoT & Edge
3. Software Engineering
4. Product Engineering

Our brand line, **AI. Software. IoT. One Technology Partner.**, reflects an integrated product model. We are not a staffing agency and we do not divide accountability among unrelated vendors. The team that validates requirements also designs the workflow, builds the software, tests the controls, supports acceptance, and stays accountable for the operating result.

For CICIC, the relevant combination is intelligent retrieval, production software, bilingual interfaces, accessible service design, integration, and human-controlled operations. The engagement also requires restraint. The system must know when to answer, when to refer, and when to stop. That kind of boundary is designed into product behaviour and acceptance tests from the beginning.

## 2.2 Why we are a strong fit

**Closed-domain product discipline.** COGITO was developed with UKE Hamburg in a privacy-sensitive mental-health context under scientific guidance. The subject matter differs from credential information, but the operating discipline is relevant: software must stay within an approved informational boundary and cannot substitute for a qualified decision-maker.

**Bilingual and multilingual delivery.** Chamber Perks includes bilingual English and French dashboard and content features. COGITO has reached more than 240,000 downloads across 19 languages. This experience supports interface, content, and release practices that treat language variants as maintained product content rather than one-time copies.

**Accessible workflows.** Wheel It Transportation uses accessible booking and scheduling software for seniors and people with disabilities. That work is directly relevant to building understandable workflows, testing practical usability, and treating accessibility as a delivery requirement.

**Education-adjacent delivery.** The Cambrian Alumni App and Athif Shaffy's teaching in software engineering and IoT at Cambrian College give the team direct experience with Canadian post-secondary users and stakeholders.

**Applied AI and systems engineering.** The Alpha Nova's own VanGuardian product applies AI to wearable-free fall detection. The team also placed first among 29 teams in the Côté Gold AI Challenge involving IAMGOLD, Laurentian University, Cambrian College, and GDG Sudbury. These examples show the ability to move from an operational problem to a tested technical system.

**One accountable team across workflow and channels.** Athif Shaffy leads the engagement and technical direction. Ertugrul Sahin leads architecture and complex backend development. Laxman KC builds AI and software services with production testing. Deepshika Ghale advises on UI and UX. Shubham Dhamane coordinates requirements, taxonomy, and user acceptance. This structure places the core handover between CRM, chat, and voice within one delivery team.

**An honest experience boundary.** The Alpha Nova has not previously deployed a retrieval-augmented generation service for CICIC, CMEC, or the credential-recognition domain. We will not imply otherwise. Our case is based on relevant product disciplines: closed-domain behaviour, multilingual delivery, accessible software, privacy-sensitive systems, production engineering, and human-controlled workflows. CICIC's own approved knowledge and evaluation items should be the basis for proving domain performance.

## 2.3 Core Project Team

| Name | About page title or standing | Role on this project | Responsibility |
|---|---|---|---|
| Athif Shaffy | Founder & CEO | Project Lead & Technical Lead | Single accountable lead for strategy, client partnership, product direction, architecture decisions, and delivery governance |
| Ertugrul Sahin | Senior Software Developer | Senior Software Engineer / Architect | System architecture, complex feature delivery, scalable backends, integrations, and engineering quality |
| Laxman KC | Software Developer | Software Developer | AI and retrieval services, full-stack delivery, data services, automated testing, and production hardening |
| Deepshika Ghale | UI Consultant | UI/UX | User research support, interaction design, prototyping, and AODA and WCAG 2.1 AA design support |
| Shubham Dhamane | Business Analyst | Requirements, taxonomy, and UAT coordination | Requirements traceability, taxonomy workshops, acceptance coordination, and measurable business outcomes |

The project team can draw on the following advisors without representing them as day-to-day delivery staff:

| Name | Standing | Advisory contribution and disclosure |
|---|---|---|
| Cheick Ismael Maiga, P.Eng. | Technical Advisor | Advises across engineering projects and is not proposed for day-to-day CICIC delivery |
| Dr. Markus Lehmann | Strategic Advisor | Advises on technology strategy and enterprise architecture; his advisory relationship with The Alpha Nova is disclosed |
| Prof. Dr. Steffen Moritz | Lead Scientific Advisor | May advise on scientific and human-boundary considerations; he is also the named client reference for COGITO, and that dual relationship is disclosed |

Detailed resumes and disclosed profiles are provided in Appendix A.

## 2.4 Relevant public work

### COGITO, UKE Hamburg

The Alpha Nova developed COGITO with UKE Hamburg from January 2021 to March 2022 and has provided occasional support since. The application has more than 240,000 downloads and is available in 19 languages. Its relevance is not a claim that mental health and credential information are the same. It is evidence of multilingual product delivery in a privacy-sensitive setting where software must support, rather than replace, the role of qualified people and approved content.

### Chamber Perks, One Chamber System

Over approximately 18 months, The Alpha Nova delivered bilingual English and French features for Chamber Perks, including a dashboard, rewards, Shop Local, the Affinity Partner Portal, and Chamber Member Pro content blocks. This work is relevant to bilingual interface behaviour, governed content, non-technical administration, and production feature delivery.

### Wheel It Transportation

From August to November 2025, with ongoing support, The Alpha Nova delivered accessible booking and scheduling for Wheel It Transportation. The service supports seniors and people with disabilities, making practical accessibility and understandable task flows central to the work.

### Cambrian Alumni App

The Cambrian Alumni App is an education-adjacent product for a Canadian college community. It demonstrates delivery for users and stakeholders in a post-secondary context.

### VanGuardian

VanGuardian is The Alpha Nova's own product for wearable-free fall detection. It demonstrates applied AI product engineering and the integration of intelligent behaviour into a system intended to support real operational response.

### Côté Gold AI Challenge

The Alpha Nova placed first among 29 teams in the Côté Gold AI Challenge involving IAMGOLD, Laurentian University, Cambrian College, and GDG Sudbury. The result demonstrates applied problem-solving and delivery under formal evaluation.

## 2.5 References

### Reference 1: UKE Hamburg

**Contact:** Prof. Dr. Steffen Moritz  
**Title:** Head of Clinical Neuropsychology Working Group, Department of Psychiatry and Psychotherapy, UKE Hamburg; Professor of Clinical Psychology  
**Email:** moritz@uke.de  
**Telephone:** +49 40 7410 56565  
**Engagement:** COGITO, January 2021 to March 2022, with occasional support since  
**Relevant scope:** Privacy-sensitive multilingual application, more than 240,000 downloads, 19 languages

**Relationship disclosure:** Prof. Dr. Steffen Moritz is both the client reference for the COGITO engagement and listed as Lead Scientific Advisor to The Alpha Nova. CCMEC should evaluate the reference with that relationship clearly disclosed.

### Reference 2: One Chamber System / Chamber Perks

**Contact:** Karen Hastie, CEO and Founder  
**Email:** karen@onechambersystem.com  
**Telephone:** +1 705 669 7343  
**Engagement:** Approximately 18 months  
**Relevant scope:** Bilingual English and French dashboard, rewards, Shop Local, Affinity Partner Portal, and Chamber Member Pro content blocks

### Reference 3: Wheel It Transportation

**Contact:** Shaunna Babyak, Chief Operating Officer  
**Email:** info@wheelittransportation.com  
**Telephone:** +1 705 929 8006  
**Engagement:** August to November 2025, with ongoing support  
**Relevant scope:** Accessible booking and scheduling for seniors and people with disabilities

These are the three proposed client references. Dr. Markus Lehmann is not presented as an independent client reference because he is a Strategic Advisor to The Alpha Nova.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# 3. Technical Architecture & Scalability

## 3.1 Architecture principles

The architecture is designed around six principles.

**CICIC controls the truth.** Only current, approved CICIC knowledge is eligible for retrieval. The software does not become an independent source.

**Policy precedes generation.** Authentication, tier, disposition, mandate, and escalation rules are evaluated before a response is produced. A fluent answer cannot override a failed policy check.

**One knowledge and policy service supports every channel.** CRM, web, and voice use the same approved content versions and routing logic. Channel presentation differs, but the institutional answer does not drift.

**Humans control consequential communication.** Staff review any AI-drafted external message before it is sent. The system can summarize and prepare context, but cannot silently become a decision-maker or correspondent.

**Evidence travels with the answer.** Text answers include citations. Voice interactions retain the retrieved source references in the transcript and handover record even when a long URL is not spoken aloud.

**Components remain portable.** Content, taxonomy, configuration, transcripts, audit history, and operational records can be exported in documented formats. The one-year term must not become technical lock-in.

## 3.2 Logical architecture

The proposed solution has five connected layers.

### 1. Governed content layer

This layer stores or indexes CICIC's approximately 75 knowledge items and 147 bilingual files together with language, taxonomy, tier, disposition, escalation triggers, source identifier, effective date, status, and version. It is the only corpus that the response service may retrieve.

### 2. Retrieval and policy layer

This layer accepts a normalized inquiry and its context, including language, channel, authenticated role, and conversation state. It filters eligible content by tier and status, retrieves candidate passages, applies mandate and disposition rules, and calculates the configured response path: answer, clarify, refer, or escalate.

### 3. Response orchestration layer

This layer composes a channel-appropriate answer from supported passages, attaches citations, applies CICIC-approved disclosure and disclaimers, and validates the response before release. If validation fails, it abstains and prepares a structured handover rather than improvising.

### 4. Channel and case layer

The CRM manages staff-facing intake, records, assignments, status, review, and reporting. The website adapter presents public Tier 1 responses. The telephone adapter integrates with the agreed YoVu path and handles speech, deterministic scripts, transfer, and callback. All three use a common handover contract.

### 5. Audit and operations layer

This layer records authentication outcome, content versions, retrieved citations, policy result, confidence band, handover event, staff action, configuration change, and channel health. It provides authorized CSV and JSON export and the data needed for agreed performance indicators.

The CRM product choice, voice integration path, and hosting pattern will be selected against the RFQ, security evidence, integration access, residency requirement, and total cost. The architecture does not depend on an unconfirmed product name.

## 3.3 Knowledge ingestion and governance

Knowledge ingestion begins with an inventory, not with bulk uploading files into a model. The team will map each supplied item to its English and French variants, source identifier, taxonomy path, sensitivity tier, disposition, trigger rules, and publication state. Missing relationships or conflicting metadata are returned to CICIC for a content-owner decision.

Approved files are parsed into retrieval passages while preserving the link to the parent item and exact source location. Search indexes contain only authorized content. Tier metadata is applied at query time and tested independently from interface visibility. Hiding a Tier 3 menu item is not a security control if the underlying passage remains retrievable.

CICIC staff will have a governed edit and publishing workflow. Depending on the final platform pattern, an authorized editor can add, revise, retire, or reclassify knowledge without retraining a model. A change moves through draft and approved states, creates an audit entry, and updates the retrieval index after publication. Prior versions remain identifiable for audit purposes.

English and French counterparts are linked but independently versioned. This supports a case where CICIC approves one language update at a different time while making any resulting parity gap visible to staff. The system will not automatically invent a translation and publish it as approved CICIC content.

## 3.4 Grounded response pipeline

Each eligible inquiry follows a controlled sequence:

1. Detect or confirm English or French and retain the user's chosen language.
2. Apply channel, authentication, role, and tier constraints before retrieval.
3. Classify the inquiry against CICIC's taxonomy and mandate boundaries.
4. Retrieve candidate passages only from active, eligible CICIC content.
5. Apply the item's answer, refer, or escalate disposition and any trigger rules.
6. Generate a response only from the supported passages.
7. Validate that each substantive claim is supported and that required citations, disclosure, and disclaimer text are present.
8. Apply the configured confidence path: answer, ask one useful clarification, or escalate.
9. Record the transcript, tags, citations, policy outcome, and content versions.
10. Send a structured handover to the CRM whenever a staff response is required.

Confidence thresholds are configurable and will be tuned using CICIC-approved evaluation material and pilot evidence. Confidence is a routing signal, not proof that an answer is correct. A high score does not override a tier restriction, escalation trigger, unsupported claim, or mandate boundary.

The system will limit clarification loops. If one clarification cannot move the inquiry into a safe and supported path, the user receives an appropriate referral or human-handover option. This avoids trapping users in repeated questions and avoids creating a false impression that the system will eventually decide their case.

## 3.5 Channel design

### CRM

The CRM is the operational foundation. It will support inquiry intake, case ownership, status, taxonomy tags, channel and language, answer or referral disposition, trigger identifiers, transcripts, citations, staff notes, audit history, and performance reporting. Role-based interfaces will expose only the information and actions needed by each staff role.

For written communication, AI may summarize an inquiry or draft a response from eligible CICIC content, but a staff member must review and approve it before any external send. This proposal does not assume an autonomous mailbot.

### Website chatbot

The public widget will retrieve Tier 1 content only. It will identify itself as AI, use CICIC-approved mandate language, provide inspectable citations, and make the human-handover path available without requiring the user to understand internal taxonomy. It will not ask for credential documents or unnecessary personal information.

The widget will be designed to integrate into cicic.ca without treating the website's full annual traffic as simultaneous chatbot demand. Capacity and cost models will use observed adoption during launch and retain room for growth.

### Telephone callbot

The telephone channel will integrate through the agreed YoVu mechanism or an approved replacement path. Identification, AI disclosure, mandate disclaimer, transfer, callback, privacy notices, and failure messages will be deterministic blocks approved in both languages. Retrieval-based speech is permitted only for supported informational content.

The callbot will not read long URLs aloud. Source references will be retained in the transcript and handover record, while the voice response gives a usable source title or approved next step. The design will support relay or TTY use and a callback alternative so accessibility does not depend on waiting through a voice menu.

If speech recognition, retrieval, or the telephony connection cannot support a safe answer, the channel will offer transfer, callback, or another CICIC-approved route. It will not continue guessing.

### Shared handover contract

Every handover will use a common structure that can include:

- source channel and timestamp;
- English or French;
- inquiry category and taxonomy node;
- disposition and trigger identifier;
- transcript or concise interaction summary;
- citations and content versions;
- confidence path and reason for escalation;
- authentication state and authorized tier, without exposing credentials; and
- callback or reply information only when the person has chosen to provide it.

This shared contract is the point where the bundled approach produces the greatest operational value. Staff receive one queue and one traceable context regardless of channel.

## 3.6 Identity, authorization, and tier enforcement

Tier 1 content is public. Tier 2 requires authentication. Tier 3 is restricted to authorized CICIC staff. The existing identity provider and authentication method for Tier 2 are **[ATHIF TO CONFIRM]**.

The final integration will follow least privilege. The identity service establishes who the user is and the role or entitlement they hold. The retrieval service receives only the authorization context needed to filter content. It does not receive or store the user's password.

Authorization will be enforced at the retrieval and API layers, not only in the interface. Test accounts will verify that:

- unauthenticated users cannot retrieve Tier 2 or Tier 3 passages by direct prompts, altered requests, or conversational references;
- authenticated Tier 2 users cannot retrieve Tier 3 content;
- internal staff access reflects assigned roles;
- exports and audit views are restricted; and
- a role or session change takes effect without leaving stale access.

Failure of the R3/R4 boundary test is a hard launch blocker for public channels.

## 3.7 Security, privacy, residency, and portability

The solution will minimize personal information at collection. Public prompts and scripts will discourage users from entering credential documents or unnecessary personal details. Handover will collect reply or callback information only when needed and voluntarily supplied. Retention and deletion rules will be configurable to the approved CCMEC schedule.

Data will be encrypted in transit and at rest. Administrative access will use role-based controls, and consequential access or configuration changes will be logged. CCMEC data and CICIC content will not be used to train foundation models.

Canadian data residency is preferred. The final submission will identify the proposed application region, inference path, storage region, backup location, telephony media path, subprocessors, and any cross-border transfer. It will also state whether the proposed pattern is Canadian cloud hosting, a private deployment, or an on-premises option. The proposal will not imply residency merely because the primary database is in Canada while model inference, logs, backups, or voice media leave the country.

The final evidence package will include the proposed data processing agreement and subprocessor map. SOC 2 or ISO evidence for the proposed platform or proponent is **[ATHIF TO CONFIRM artefacts]**. The proposal will describe exactly whose assurance report or certification is supplied and what parts of the solution it covers.

Portability is designed into the service. CICIC will be able to export its knowledge items, taxonomy, tier and disposition metadata, system configuration, case records, tagged transcripts, citations, audit records, and reports in documented formats. Exit documentation will identify dependencies and the process for verified deletion after transfer.

## 3.8 Accessibility and bilingual delivery

The website and staff-facing surfaces will follow WCAG 2.1 Level AA with a documented path to WCAG 2.2 and a VPAT for the applicable surfaces. Accessibility work will include keyboard operation, focus order, labels and instructions, error identification, contrast, reflow, text scaling, screen-reader semantics, status announcements, and non-colour cues. Automated checks will support, not replace, manual keyboard and assistive-technology review.

The voice channel will support relay or TTY compatibility and a callback alternative. Deterministic scripts will be reviewed in English and French for understandable pacing and Canadian pronunciation. A voice channel is not considered accessible merely because it can speak.

English and French will share the same functional path, disposition rules, escalation options, citations, and audit data. The team will test each language independently and compare outcomes by inquiry type. Interface layouts will accommodate French text without truncation or reduced functionality. CICIC remains responsible for approving specialized terminology and public wording in each language.

## 3.9 Auditability, measurement, and service levels

Authorized staff will be able to trace a response to the content and controls that produced it. The audit record will include the channel, language, taxonomy, retrieved source identifiers, content versions, disposition, confidence path, escalation trigger, authentication tier, timestamps, and staff review or override. Exports will be available in CSV and JSON where appropriate.

The service will instrument agreed performance indicators from the first production day of each component. Measures can include inquiry volume by channel and language, answer, refer, and escalation outcomes, low-confidence rate, handover completion, common taxonomy paths, unresolved categories, staff review activity, response errors, accessibility defects, and channel availability. KPI definitions, denominators, exclusions, and ownership will be documented so reports remain interpretable.

Service levels will distinguish an engineering target from a contractual floor.

**Design target:** The team's internal operating objective. It supports capacity planning and proactive improvement but does not by itself create a credit or warranty.

**Contractual floor:** The minimum measured level agreed in the contract after applicable exclusions. Remedies apply only as the contract states.

Availability will be measured for the production components operated by The Alpha Nova over an agreed service window. The formula, monitoring source, incident severity definitions, notification clocks, maintenance notice, reporting period, and remedy will be explicit. Exclusions will identify dependencies outside The Alpha Nova's control, such as CCMEC networks, cicic.ca infrastructure not operated by the team, YoVu or another carrier, public telephone networks, internet or DNS services, buyer-caused configuration, and scheduled maintenance.

Conversational responsiveness will be treated the same way. Any contractual latency metric must identify the measurement point, percentile, observation window, and exclusions. We will not make an unbounded claim of 99 percent availability or a universal two-second response across browsers, model inference, telephony carriers, and public networks.

Incident and breach procedures will define severity, ownership, escalation, communication, containment, evidence preservation, and notification. The clock starts from the detection or notice event defined in the contract, not from an ambiguous retrospective point.

## 3.10 Scalability and maintainability

Current volume provides the sizing baseline: approximately 770,000 website sessions, 2.1 million page views, 6,000 Connect.the.dots reports, 1,800 automated-menu calls, and 2,560 staff-handled email and telephone inquiries each year. These figures do not imply that every website session will use the chatbot. Launch instrumentation will establish real adoption, peak concurrency, language distribution, handover volume, and voice duration.

Application, retrieval, and channel services will be separable so that load can scale where it occurs. Web demand can grow without duplicating the knowledge base. Voice capacity can expand without changing CRM taxonomy. Staff seats can change without rebuilding the public widget. The architecture will use bounded queues and controlled retries so a temporary channel interruption does not silently lose a handover or create duplicate cases.

Maintainability depends on configuration rather than model retraining. CICIC staff can update approved knowledge, dispositions, triggers, disclaimers, thresholds, and selected routing rules through controlled administration. Technical runbooks will cover content indexing, access review, failed handovers, channel health, export, restore, and incident response.

Future email automation can reuse the grounding and policy layer after its inbound and outbound scope is approved. It is not included as an autonomous fourth channel in this three-component proposal.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# 4. Work Plan & Delivery Approach

## 4.1 Delivery sequence

The work will be delivered within the proposed initial term from 1 April 2027 at 9:00 a.m. EDT to 31 March 2028 at 9:00 a.m. EDT. Detailed milestone dates will be baselined jointly at kickoff after the final platform, integration access, privacy review, and acceptance responsibilities are known. The sequence below protects the human-handover path before public automation is released.

| Phase | Focus and activities | Primary deliverables | Exit gate |
|---|---|---|---|
| 0. Mobilization and discovery | Confirm governance, users, current workflows, component boundaries, integration access, content ownership, privacy and security evidence, accessibility approach, and acceptance method | Approved delivery plan, requirements traceability, system context, data flows, risk register, subprocessor map, and acceptance plan | CICIC and The Alpha Nova approve the baseline and owners |
| 1. CRM and escalation foundation | Implement or configure inquiry intake, records, taxonomy, assignments, dispositions, handover payload, audit history, role controls, and reporting foundation | Acceptance-ready CRM component and shared channel contract | Staff workflow, audit, access, and handover tests pass |
| 2. Knowledge and policy service | Inventory the bilingual corpus, map tiers and dispositions, create governed indexing, implement closed-domain retrieval, citations, confidence paths, disclaimers, and escalation logic | Versioned bilingual retrieval corpus, policy service, administration workflow, and evaluation harness | Grounding, citation, mandate, and tier tests pass |
| 3. Website chatbot | Integrate the Tier 1 public widget, disclosure, citations, accessible interaction, human handover, analytics, and failure states | Acceptance-ready English and French chatbot on the approved cicic.ca environment | Bilingual, accessibility, security, and handover gates pass |
| 4. Telephone callbot | Integrate the agreed YoVu path, deterministic voice blocks, approved English and French voices, retrieval responses, transfer, callback, relay or TTY path, and transcripts | Acceptance-ready English and French telephone callbot | Voice determinism, accessibility, grounding, and transfer tests pass |
| 5. Controlled launch and stabilization | Release by approved channel, monitor outcomes, review escalations, tune thresholds, correct defects, train staff, and finalize operations | Production bundle, trained staff, evidence pack, runbooks, and KPI reporting | CICIC accepts production operation and residual risks |
| 6. Support and transition | Maintain the service, validate knowledge changes, report performance, support incidents, and prepare renewal or exit | Support records, regular KPI packs, updated documentation, and portable exports | End-of-term renewal or orderly transition decision |

CRM-first delivery does not mean that architecture and UX for later channels wait until the CRM is complete. Discovery and shared design run across the bundle. It means that no public channel launches before its escalation destination and staff operating process are ready.

## 4.2 Governance and working model

Athif Shaffy will act as Project Lead and Technical Lead and will be The Alpha Nova's accountable contact. CICIC has three staff members and one primary point of contact, so governance must respect a small operational team. The delivery model will concentrate decisions into prepared working sessions, concise written decision records, and demonstrations of working software.

The working rhythm will include:

- a regular project status meeting focused on decisions, risks, dependencies, and acceptance;
- focused workshops for taxonomy, dispositions, escalation triggers, language, security, privacy, and accessibility;
- demonstrations at the end of each acceptance-ready increment;
- a maintained requirements and compliance matrix;
- a decision log naming the owner, decision, date, and affected component;
- a risk and issue register with a clear next action; and
- written release notes and acceptance evidence for each production change.

Shubham Dhamane will coordinate requirements, taxonomy, and user acceptance so that technical implementation remains tied to CICIC's operating rules. Ertugrul Sahin will own architecture consistency and integration quality. Laxman KC will support implementation, automated checks, and production hardening. Deepshika Ghale will advise on staff and public UI and UX, including AODA and WCAG 2.1 AA considerations.

Advisors are available for defined reviews. Cheick Ismael Maiga, P.Eng., is not represented as day-to-day delivery capacity. Dr. Markus Lehmann's strategic advisory relationship and Prof. Dr. Steffen Moritz's dual advisor and client-reference relationship remain disclosed.

## 4.3 Quality assurance and acceptance

Quality assurance is continuous and risk-based. The team will test software behaviour, content grounding, authorization, bilingual parity, accessibility, integration, recovery, and operational reporting. Acceptance evidence will map each test to the applicable requirement and content or configuration version.

The evaluation set will be separated from development examples where CICIC requires an unbiased measure. CICIC-provided items will be used for formal domain evaluation. The Alpha Nova will not scrape the open web, invent credential-recognition answers, or treat public pages as a substitute for CICIC's approved EV-01 material.

Core acceptance streams include:

**Grounding and citations:** Every substantive claim in a sampled answer must be supported by an eligible CICIC passage, with the source retained in the audit record and shown on text surfaces.

**Mandate and disposition:** Assessment, recognition, decisional, unsupported, and out-of-mandate prompts must abstain, refer, or escalate according to the approved rule.

**Tier enforcement:** Direct prompts, indirect prompts, altered requests, and conversation-history attacks must not expose Tier 2 or Tier 3 content to an unauthorized user. This is a hard launch gate.

**Bilingual parity:** English and French test sets will compare grounding, citation, disposition, escalation, usability, and channel function. Passing in one language does not compensate for a failure in the other.

**Human review:** An AI-drafted external response must remain unsent until an authorized staff member reviews and approves it.

**Voice determinism:** Identification, disclosure, disclaimer, transfer, callback, and failure blocks must use approved deterministic wording. Transcripts must retain source and routing context without speaking long URLs.

**Accessibility:** Public and staff surfaces will be reviewed against WCAG 2.1 Level AA, the path to WCAG 2.2, the applicable VPAT, and practical keyboard and assistive-technology use. Voice acceptance includes relay or TTY and callback behaviour.

**Instrumentation:** Each channel must produce the tags, audit records, exports, and agreed KPI inputs from its first production release.

**Recovery and handover:** Interrupted channel calls, duplicate retries, failed CRM writes, and unavailable dependencies must have observable, recoverable outcomes. A user must not receive a false confirmation that a handover succeeded.

No production release proceeds with an unresolved defect that permits unauthorized retrieval, unsupported external answers, unreviewed external sends, or bypass of an escalation rule.

## 4.4 Training, documentation, and support

Training will be organized around staff tasks rather than product menus. CICIC staff will learn how to receive and assign a handover, review a draft, inspect citations, correct taxonomy, approve or retire knowledge, change an approved configuration, run an export, interpret KPI reports, and report an incident.

Documentation will include:

- administrator and staff user guides;
- knowledge ingestion, approval, versioning, and retirement procedures;
- taxonomy, tier, disposition, and trigger configuration guidance;
- CRM and channel handover runbooks;
- access review and account administration procedures;
- incident, failed-integration, restore, and escalation runbooks;
- data-flow and subprocessor documentation;
- audit and KPI definitions;
- accessibility and VPAT evidence for applicable surfaces;
- architecture and interface documentation; and
- export and end-of-term transition instructions.

Support during the initial term will cover defect triage, production monitoring for operated components, failed handovers, knowledge-index verification after approved changes, security and access incidents, and controlled configuration adjustments. Service response and resolution commitments will be tied to agreed severity definitions and service windows, not left as general assurances.

## 4.5 CICIC and CCMEC responsibilities

Delivery depends on CICIC and CCMEC retaining authority for institutional content and decisions. The buyer will need to provide:

- the approved English and French knowledge base, taxonomy, sensitivity tiers, dispositions, escalation triggers, and source identifiers;
- a primary product owner and available subject-matter reviewers;
- approval of mandate disclaimers, AI disclosure, voice scripts, referral wording, and specialized terminology;
- access to the existing CRM information needed for migration or transition;
- access to cicic.ca integration points and the relevant deployment process;
- access to the agreed YoVu SIP, API, IVR, or replacement integration path;
- the existing Tier 2 identity method and authorization rules;
- privacy, retention, deletion, incident, and records-management decisions;
- staff participation in workflow validation, training, and user acceptance;
- CICIC-owned EV-01 and related domain evaluation material; and
- timely decisions on content gaps, conflicting rules, and launch exceptions.

The Alpha Nova will make dependencies visible early and present decisions in a form the small CICIC team can resolve. We will not silently fill an institutional content gap with generated material.

## 4.6 Risks and controls

| Risk | Practical consequence | Control |
|---|---|---|
| CICIC content is incomplete, duplicated, or inconsistent across languages | Retrieval can be fluent but institutionally wrong | Inventory and metadata validation before indexing; route unresolved content decisions to CICIC |
| Tier metadata is enforced only in the interface | Sensitive material can be retrieved through a direct or manipulated request | Enforce authorization in retrieval and APIs; make the access-boundary test a hard launch gate |
| A model answers beyond CICIC's mandate | The service appears to assess credentials or decide a case | Pre-generation mandate and disposition rules, citation validation, abstention, and escalation tests |
| English quality exceeds French quality | A substantial share of users receives an inferior service | Independent bilingual tests, linked content versions, French UX review, and comparative KPI sampling |
| Public launch precedes staff workflow readiness | Escalations enter an unmanaged queue or users repeat their story | Deliver the CRM and common handover contract before public channel launch |
| Telephony integration details arrive late | Callbot delivery or call transfer is delayed | Confirm YoVu SIP, API, IVR, number, routing, and callback access during mobilization |
| Users provide unnecessary personal information | Privacy exposure increases without service value | Data-minimizing prompts, redaction or masking controls, restricted access, and retention rules |
| Automated metrics are misunderstood | A high containment rate is rewarded even when referrals are wrong | Define denominators and quality measures; report safe answer, referral, escalation, and error outcomes separately |
| A third-party platform changes availability or residency | Contractual commitments no longer match the operating chain | Document subprocessors, regions, dependencies, exit options, and service-level exclusions |
| The three-person CICIC team is overburdened by workshops | Decisions and content validation become delivery bottlenecks | Prepared decision packets, concentrated workshops, asynchronous review, and one maintained decision log |

## 4.7 Transition and end-of-term portability

The one-year initial term should produce an operable service, not a dependency that can be exited only through a new development project. Throughout delivery, configuration and interfaces will be documented, and exports will be tested before the end of the term.

At renewal or transition, CICIC will receive the agreed current exports of knowledge, metadata, taxonomy, cases, tagged transcripts, citations, audit records, configuration, and reports. The handover package will identify software dependencies, subprocessor relationships, outstanding incidents, known defects, operating procedures, and deletion obligations. The parties can then choose renewal, transition to another operator, or decommissioning with a verified data disposition.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# 5. Budget

All figures are in Canadian dollars and are subject to applicable HST. The rates below are the professional-service rates used in The Alpha Nova's prior MineOpportunity bid.

## 5.1 Professional-service rates

| Service category | Hourly rate | Daily rate |
|---|---:|---:|
| Software development | $80/hour | $640/day |
| Design, UI/UX | $75/hour | $600/day |
| Testing and QA | $50/hour | $400/day |

No other labour category or premium rate is introduced in this draft.

## 5.2 Pricing structure for the bundled submission

The final quote must distinguish implementation, recurring platform costs, usage, and support so CCMEC can see the complete first-year cost and the cost drivers for later operation. It must also show the three component prices while making clear that The Alpha Nova is bidding all three as one integrated bundle.

| Cost item | Basis | Amount, CDN before HST |
|---|---|---:|
| Mobilization, discovery, solution design, and privacy and security documentation | One-time | **[ATHIF TO CONFIRM]** |
| CRM implementation or configuration, intake, migration, taxonomy, workflow, audit, reporting, and training | One-time | **[ATHIF TO CONFIRM]** |
| Shared knowledge, retrieval, policy, citation, and evaluation service | One-time | **[ATHIF TO CONFIRM]** |
| Website chatbot integration, accessibility, bilingual acceptance, and launch | One-time | **[ATHIF TO CONFIRM]** |
| Telephone callbot integration, deterministic voice blocks, accessibility, bilingual acceptance, and launch | One-time | **[ATHIF TO CONFIRM]** |
| Cross-channel CRM handover and integration | One-time | **[ATHIF TO CONFIRM]** |
| Initial-term hosting, platform licences, storage, monitoring, and backups | Recurring for initial term | **[ATHIF TO CONFIRM]** |
| CRM agent and administrator seats | Recurring for initial term | **[ATHIF TO CONFIRM]** |
| AI inference usage for web and staff workflows | Usage-based or included allowance | **[ATHIF TO CONFIRM]** |
| Voice transcription, synthesis, telephony, and AI usage | Usage-based or included allowance | **[ATHIF TO CONFIRM]** |
| Initial-term support and service management | Recurring for initial term | **[ATHIF TO CONFIRM]** |
| Optional services outside the three-component scope | Separately authorized | **[ATHIF TO CONFIRM]** |

### Component and total summary

| Summary | Amount, CDN before HST |
|---|---:|
| CRM component total for the initial term | **[ATHIF TO CONFIRM]** |
| Website chatbot component total for the initial term | **[ATHIF TO CONFIRM]** |
| Telephone callbot component total for the initial term | **[ATHIF TO CONFIRM]** |
| Shared and cross-channel costs | **[ATHIF TO CONFIRM]** |
| Total one-time implementation | **[ATHIF TO CONFIRM]** |
| Total recurring and usage allowance for the initial term | **[ATHIF TO CONFIRM]** |
| **Total bundled quote for 1 April 2027 to 31 March 2028, before HST** | **[ATHIF TO CONFIRM]** |
| Applicable HST | **[ATHIF TO CONFIRM]** |
| **Total bundled quote including HST** | **[ATHIF TO CONFIRM]** |

## 5.3 Pricing assumptions to state in the final quote

The final pricing workbook or schedule should state rather than hide its operating assumptions:

- all three components are bid as one integrated bundle;
- CICIC has approximately three staff members, while final agent, administrator, and concurrent-seat quantities remain subject to the buyer's clarification;
- current annual volumes are approximately 770,000 website sessions, 2.1 million page views, 6,000 Connect.the.dots reports, 1,800 automated-menu calls, and 2,560 staff-assisted written and telephone inquiries;
- website traffic is a capacity indicator and is not treated as guaranteed chatbot usage;
- English and French are included production languages;
- CICIC provides and approves the knowledge-base content and terminology;
- Tier 2 identity integration depends on the existing identity method;
- telephony cost depends on the agreed YoVu SIP, API, IVR, or replacement path;
- hosting, inference, log, backup, and telephony residency will be stated explicitly;
- included usage, overage units, renewal basis, and any price adjustment will be stated explicitly; and
- work outside the approved scope will require written authorization before billing.

This internal draft intentionally contains no invented component amount, platform licence, usage fee, or total quote.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# Appendix A: Key Team Resumes

## Athif Shaffy

**Title:** Founder & CEO, The Alpha Nova Inc.  
**Location:** Greater Sudbury, Ontario  
**Proposed role:** Project Lead & Technical Lead  
**LinkedIn:** https://www.linkedin.com/in/athif-shaffy/

### Profile

Athif Shaffy leads company strategy, client partnerships, and product vision at The Alpha Nova. He has over seven years of experience shipping software across mining, healthcare, and education. For CICIC, he will be the accountable project and technical lead, own client governance and architecture decisions, and connect product requirements to delivery.

### Experience

**The Alpha Nova Inc., Founder & CEO | September 2020 to present**

- Leads strategy, client partnerships, and product vision.
- Directs intelligent-software and product-engineering engagements.
- Provides the single accountable leadership point for the proposed CICIC bundle.

**Maestro Digital Mine | November 2022 to February 2025**

- Worked on Duetto Analytics supporting more than 250 industrial devices.
- Brought mining and industrial-software experience to data-intensive production systems.

**Cambrian College, educator**

- Teaches software engineering and IoT.

### Education

- Diploma, Mobile Application Development, Cambrian College
- Bachelor of Science in Software Engineering, First Class Honours, Staffordshire University. **[ATHIF TO CONFIRM: programme name and year. Do not name Colombo, Passau, or a Sri Lanka office. Personal education pathway may be stated only if Athif wants it on this bid.]**

### Community leadership

- Lead Organizer, GDG Sudbury
- Cursor Ambassador, Sudbury

### Awards

- First place, Communications-Denied Autonomy Hackathon, York University, 2026
- First place, Côté Gold Blast Captain DevFest Challenge, GDG Sudbury
- Third place, Ottawa Defence Hackathon, Canadian Supply Chains track

### CICIC relevance

Athif combines delivery leadership, software architecture, AI product work, education experience, and industrial systems exposure. He will be responsible for keeping the system inside CICIC's informational and referential mandate and for ensuring that delivery decisions remain traceable to the RFQ.

## Ertugrul Sahin

**About page title:** Senior Software Developer  
**Proposed role:** Senior Software Engineer / Architect  
**LinkedIn:** https://www.linkedin.com/in/ertugrul-sahin-502911155/

### Profile

Ertugrul Sahin leads complex feature development and system architecture, with a focus on scalable backends and engineering quality. For CICIC, he will shape the shared architecture, CRM and channel integrations, access boundaries, deployment pattern, and engineering standards.

### Experience

**The Alpha Nova Inc. | March 2026 to present**

- Leads complex feature development and system architecture.
- Builds scalable backend services and guides engineering quality.

**Cambrian College Research and Development | March 2023 to March 2026**

- Contributed to applied research and development work over a three-year period.

### Education

- Diploma, Mobile Application Development, Cambrian College
- Bachelor's degree, Computer Engineering, Beykent University, Istanbul

### Technical skills

- Languages: Python, JavaScript, TypeScript, C#, PHP, Java, Dart, Kotlin, Swift
- Frameworks and platforms: Flutter, Angular, React, Node.js, Django, Laravel
- Interfaces: REST, WebSockets
- Data: MySQL, PostgreSQL, CouchDB, Firebase
- IoT and edge: MQTT, Raspberry Pi
- Delivery: Docker, Linux, CI/CD
- Enterprise systems: Exchange Online, Teams, SharePoint, access management

### Awards

- First place, Côté Gold Challenge, 2024

### CICIC relevance

Ertugrul's backend, real-time interface, database, delivery, and access-management experience maps to the CRM spine, shared retrieval service, telephony integration, role controls, auditability, and cross-channel handover.

## Laxman KC

**Title:** Software Developer  
**Proposed role:** Software Developer  
**LinkedIn:** https://www.linkedin.com/in/laxmankc/

### Profile

Laxman KC ships web and mobile features as well-tested production code. His work spans AI tools, APIs, data systems, telemetry, user interfaces, messaging, testing, and cloud services. For CICIC, he will support retrieval and policy services, full-stack implementation, automated acceptance checks, and production hardening.

### Experience

**Cambrian College Research and Development | December 2024 to present**

- Works on AI tools and mining-vehicle telemetry.
- Supports Rokion and Teleco telemetry processing at more than 90,000 records per day.

**The Alpha Nova Inc. | January 2024 to present**

- Delivers production web, mobile, AI, data, and API features.
- Builds and tests software intended for ongoing operational use.

### Education

- Diploma, Computer Programming and IoT, Cambrian College

### Technical skills

- Languages and scripting: Python, TypeScript, JavaScript, C, C++, Bash, SQL
- AI and computer vision: computer vision, YOLOE, CLIP
- APIs and services: FastAPI, Node.js, REST
- Data and messaging: PostgreSQL, MongoDB, Redis, Kafka
- Web: React, Next.js
- IoT: MQTT
- Quality and delivery: Pytest, Jest, Docker, GitLab CI
- Cloud: AWS, Azure

### Awards

- First place, Communications-Denied Autonomy Hackathon, York University, 2026
- Second place, Verified Canadian Supply Chains, Ottawa, 2026
- Third place and NVIDIA Brev.dev AI Control recognition, McGill, 2026
- Second place, AI Hackathon, Cambrian College, 2025
- First place, Côté Gold Challenge, 2024

### CICIC relevance

Laxman's experience with AI tooling, event-driven data, APIs, automated tests, and cloud platforms supports closed-domain retrieval, confidence and escalation logic, transcript tagging, exports, instrumentation, and repeatable bilingual acceptance tests.

## Deepshika Ghale

**About page title:** UI Consultant  
**Proposed role:** UI/UX  
**LinkedIn:** https://www.linkedin.com/in/deepshika-ghale/

### Profile

Deepshika Ghale is a UI Consultant who advises The Alpha Nova on UI and UX. She works with Figma, prototyping, and AODA and WCAG 2.1 Level AA considerations. For CICIC, she will advise on staff workflows, public chat interaction, bilingual layouts, accessibility, and user-acceptance preparation.

### Experience

**The Alpha Nova Inc., UI Consultant | March 2025 to present**

- Advises on UI and UX for digital products.
- Supports interface design and prototyping.

**Cambrian College Research and Development, UI/UX | April 2024 to April 2025**

- Contributed UI and UX work in an applied research and development setting.

**Additional website work**

- The Social Soulpreneur
- RufDiamond

### Education

- Business Analytics, Cambrian College
- Mobile Application Development, Cambrian College
- Bachelor of Science with Honours in Computer Science, Herald College Kathmandu

### Design skills

- Figma
- Prototyping
- Product design and UX strategy
- AODA and WCAG 2.1 Level AA design considerations

### Awards

- First place, Cursor Sudbury Hackathon, 2026
- First place, Côté Gold Challenge, 2024

### CICIC relevance

Deepshika's role supports practical accessibility, readable disclosures and citations, low-friction human handover, staff review workflows, and equivalent English and French interface behaviour. Her title remains UI Consultant; this proposal does not represent her as a full-time Product Designer.

## Shubham Dhamane

**Title:** Business Analyst  
**Location:** Greater Sudbury, Ontario  
**Proposed role:** Requirements, taxonomy, and UAT coordination  
**LinkedIn:** https://www.linkedin.com/in/dhamanes7/

### Profile

Shubham Dhamane bridges business and engineering by translating requirements into delivery work tied to measurable value. For CICIC, he will coordinate requirement validation, taxonomy and disposition workshops, traceability, user-acceptance planning, issue capture, and acceptance evidence.

### CICIC responsibilities

- Maintain traceability from RFQ requirements to design, implementation, and evidence.
- Coordinate review of taxonomy, tiers, dispositions, and escalation triggers.
- Prepare focused decisions for CICIC's primary point of contact.
- Coordinate English and French user-acceptance activities with the delivery team.
- Track acceptance findings through resolution and sign-off.

No additional employment dates, education, certifications, or awards are claimed in this proposal.

## Cheick Ismael Maiga, P.Eng.

**Standing:** Technical Advisor  
**Proposed role:** Advisory review, not day-to-day delivery  
**LinkedIn:** https://www.linkedin.com/in/cheickismaelmaiga/

### Profile

Cheick Ismael Maiga is a Professional Engineer who advises across The Alpha Nova's engineering projects. If requested for CICIC, his contribution will be limited to defined technical-advisory reviews. He is not represented as day-to-day delivery capacity.

No engineering discipline, employment history, education, certification beyond P.Eng., project allocation, or additional credential is claimed in this proposal.

## Dr. Markus Lehmann

**Standing:** Strategic Advisor  
**Proposed role:** Strategic advisory input, not day-to-day delivery

### Profile

Dr. Markus Lehmann advises The Alpha Nova on technology strategy and enterprise architecture. His relationship with The Alpha Nova is disclosed wherever his name appears. He is not presented as an independent client testimonial and is not one of the three proposed client references.

No day-to-day CICIC allocation, employment history, education, or additional credential is claimed in this proposal.

## Prof. Dr. Steffen Moritz

**Standing:** Lead Scientific Advisor to The Alpha Nova and client reference for COGITO  
**Institutional role:** Head of Clinical Neuropsychology Working Group, Department of Psychiatry and Psychotherapy, UKE Hamburg; Professor of Clinical Psychology  
**Proposed role:** Scientific advisory input if requested, not day-to-day delivery  
**Reference contact:** moritz@uke.de | +49 40 7410 56565

### Profile

Prof. Dr. Steffen Moritz provided scientific leadership in connection with COGITO, developed with UKE Hamburg from January 2021 to March 2022, with occasional support since. COGITO has more than 240,000 downloads and is available in 19 languages.

### Relationship disclosure

Prof. Dr. Steffen Moritz is both the proposed UKE Hamburg client reference for COGITO and listed as Lead Scientific Advisor to The Alpha Nova. This dual relationship is disclosed so CCMEC can assess the reference with full context. He is not represented as independent of The Alpha Nova's advisory network and is not proposed for day-to-day CICIC delivery.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# Appendix B: R1-R22 Compliance Matrix

**Legend:** M = Must. S = Should. "Will comply" states the proposed bundled solution's intended contractual posture. Assurance evidence that has not been confirmed is identified rather than invented.

| ID | Priority | Requirement | Proposed compliance response | Proposal section and acceptance evidence |
|---|:---:|---|---|---|
| R1 | M | Closed-domain retrieval-augmented generation with no open-web or open-domain answer generation | **Will comply.** CICIC's active, approved corpus is the only retrieval source. Unsupported questions abstain, refer, or escalate. | Sections 1.4, 1.5, 3.3, 3.4; grounded-answer and unsupported-prompt tests |
| R2 | M | Citations for substantive answers | **Will comply.** Text channels show inspectable citations. Voice retains source references in transcripts and handovers without reading long URLs aloud. | Sections 3.4, 3.5, 3.9; citation coverage and source-version checks |
| R3 | M | AI disclosure and confidence fallback | **Will comply.** Each public channel identifies AI use and follows configured answer, clarify, refer, or escalate paths. | Sections 1.5, 3.4, 3.5; disclosure and low-confidence routing tests |
| R4 | M | Role-based access across Tiers 1, 2, and 3 | **Will comply.** Authorization is enforced in retrieval and APIs. Tier-boundary failure blocks public launch. | Sections 1.4, 3.6, 4.3; direct, indirect, and altered-request access tests |
| R5 | M | Escalation hooks and structured human handover | **Will comply.** Web and voice use one CRM handover contract containing channel, language, tags, transcript, citations, confidence path, and trigger context. | Sections 1.3, 3.5, 4.1; end-to-end handover and failure-recovery tests |
| R6 | M | Equivalent English and French operation, including Canadian voice register | **Will comply.** Content, retrieval, interface, voice, fallback, audit, and acceptance are tested independently in both languages. | Sections 1.2, 3.8, 4.3; CICIC-owned bilingual evaluation and voice review |
| R7 | S | Canadian data residency or private deployment preferred | **Preferred and supported as an evaluated design choice.** The final bid will name application, inference, storage, logs, backups, and telephony media locations. | Section 3.7; architecture and subprocessor evidence |
| R8 | M | WCAG 2.1 Level AA, path to WCAG 2.2, and VPAT | **Will comply.** Accessibility is a launch stream for applicable public and staff surfaces. | Sections 3.8, 4.3, 4.4; manual and automated evidence plus VPAT |
| R9 | M | Audit logs and CSV or JSON export | **Will comply.** The system retains content versions, policy outcomes, access context, handovers, and staff actions with authorized export. | Sections 3.2, 3.9, 4.7; audit trace and export tests |
| R10 | M | Privacy controls, DPA, subprocessors, and SOC 2 or ISO 27001 evidence | **Will comply with the control and disclosure requirement.** DPA and subprocessor mapping are included. SOC 2 or ISO evidence is **[ATHIF TO CONFIRM artefacts]** and will state whose controls it covers. | Section 3.7; executed DPA, subprocessor map, and confirmed assurance material |
| R11 | M | Data portability for a one-year term | **Will comply.** Knowledge, metadata, configuration, cases, transcripts, citations, audit records, and reports are exportable in documented formats. | Sections 3.7, 4.7; trial export and transition runbook |
| R12 | M | Knowledge-base edits without model retraining | **Will comply.** Authorized publishing updates the retrieval index while retaining version and audit information. | Sections 1.4, 3.3, 3.10; add, revise, retire, re-tier, and rollback tests |
| R13 | M | Human-in-the-loop approval before external send | **Will comply.** AI may prepare an internal draft, but an authorized staff member must review it before release. | Sections 1.5, 3.1, 3.5, 4.3; send-control and permission tests |
| R14 | S | Tunable confidence and related routing thresholds | **Will comply.** Thresholds and loop limits are configurable and tuned using CICIC-approved evidence. Confidence never overrides mandate or authorization. | Sections 3.4, 3.9; threshold, clarification, and fallback tests |
| R15 | M | Tagged transcripts delivered to the CRM | **Will comply.** Handover includes language, inquiry category, taxonomy, trigger, transcript, citations, confidence path, and channel. | Sections 3.5, 3.9; end-to-end transcript and tag verification |
| R16 | M | Personal-information minimization, retention and deletion, and no CCMEC data used for model training | **Will comply.** Collection is minimized, access is controlled, retention is configurable, deletion is verifiable, and model training on CCMEC data is prohibited. | Sections 1.5, 3.7; prompt, retention, deletion, and vendor-configuration evidence |
| R17 | M | Deterministic voice blocks and YoVu or SIP integration | **Will comply.** Identification, disclosure, disclaimer, transfer, callback, privacy, and failure wording are approved deterministic blocks. Long URLs are not read aloud. | Sections 3.5, 4.1, 4.3; script-match, transcript, routing, and integration tests |
| R18 | M | Performance indicators from the first production day | **Will comply.** Agreed tags and KPI events are part of each channel's production release. | Sections 3.9, 4.3; instrumentation and report reconciliation tests |
| R19 | S | Service-level agreement for availability, incident response, and breach notification | **Will comply on measured terms.** The SLA will distinguish target from contractual floor and define formula, window, exclusions, severity, clocks, and remedies. | Sections 3.9, 4.4; monitoring report and incident exercise |
| R20 | S | Accessible voice through relay or TTY and callback | **Will comply.** Voice acceptance includes relay or TTY compatibility and a callback alternative. | Sections 3.5, 3.8, 4.3; accessible-channel test evidence |
| R21 | M | Configurable CICIC disclaimers and branding | **Will comply.** Authorized staff can maintain approved wording and presentation through controlled configuration and audit. | Sections 1.5, 3.3, 3.5, 3.10; configuration, approval, and channel-rendering tests |
| R22 | M | Encryption, access control, and Tier 2 authentication | **Will comply.** Data is encrypted in transit and at rest, access is role-based, and Tier 2 integrates with CICIC's existing identity method, **[ATHIF TO CONFIRM]**. | Sections 3.6, 3.7; encryption configuration, access review, and authentication tests |

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION

---

> The Alpha Nova | CICIC Customer-Service Automation | RFP No. 2026-CICIC-01

# INTERNAL Athif Checklist: Strip Before Bid

## Official package and submission

- [ ] Download and read the current official MERX RFQ package, all appendices, and every addendum.
- [ ] Confirm that Solicitation 2026-CICIC-01, MERX 0000330086, Source ID PV.MN.ON.383381.C111700, buyer name, contact, address, closing time, and initial term match the latest official documents.
- [ ] Confirm the required channel for questions before 4 September 2026 at 9:00 a.m. EDT. Athif sends them. Nothing is submitted by this draft.
- [ ] Record and incorporate every official answer issued to proponents.
- [ ] Confirm the bid submission channel, file naming, file types, signatures, declarations, and whether pricing is separate from the technical response.
- [ ] Confirm page and format limits: **[ATHIF TO CONFIRM]**.
- [ ] Confirm whether resumes and the compliance matrix are outside any page limit.
- [ ] Acknowledge every addendum in the required place.
- [ ] Plan submission before close day.

## Solution and compliance

- [ ] Bid CRM, website chatbot, and telephone callbot together as required.
- [ ] Resolve whether the CRM may be configured COTS, must be custom-built, or may use either approach.
- [ ] Identify the Tier 2 identity provider and authentication method: **[ATHIF TO CONFIRM]**.
- [ ] Confirm YoVu access and whether integration is through SIP, API, the existing IVR, number routing, or replacement.
- [ ] Confirm whether mailbot scope includes inbound triage, outbound drafting, outbound sending, or future work only.
- [ ] Identify the proposed Canadian hosting, inference, logs, backups, and telephony media locations.
- [ ] Name every subprocessor and confirm data-retention and model-training settings.
- [ ] Assemble the DPA and subprocessor map.
- [ ] Attach and describe SOC 2 or ISO evidence: **[ATHIF TO CONFIRM artefacts]**.
- [ ] Confirm the required VPAT format and attach evidence for each applicable surface.
- [ ] Verify that the technical response never claims credential assessment, recognition, comparison, or decision-making.
- [ ] Verify that no Tier 2 or Tier 3 content is proposed for an unauthenticated channel.
- [ ] Verify that external AI-drafted communication always requires staff review.
- [ ] Verify that no CCMEC data is used to train models.
- [ ] Confirm that EV-01 and other domain evaluation items come from CICIC and are not created by The Alpha Nova.
- [ ] Replace architecture choices described as proposals with the final named products, regions, and evidence.

## Team and references

- [ ] Confirm each delivery team member's availability for the initial term.
- [ ] Keep Deepshika Ghale's About page title as UI Consultant.
- [ ] Keep Cheick Ismael Maiga, P.Eng., as an advisor and not day-to-day delivery staff.
- [ ] Disclose Dr. Markus Lehmann's Strategic Advisor relationship wherever relevant.
- [ ] Disclose Prof. Dr. Steffen Moritz's dual role as COGITO client reference and Lead Scientific Advisor.
- [ ] Do not use Dr. Markus Lehmann as an independent testimonial or client reference.
- [ ] Obtain permission from UKE Hamburg, One Chamber System, and Wheel It Transportation to use the named contacts.
- [ ] Recheck all names, titles, email addresses, telephone numbers, engagement dates, download counts, language counts, and award descriptions.
- [ ] Keep the honest gap that The Alpha Nova has no prior CICIC, CMEC, or credential-recognition RAG deployment.
- [ ] Do not add unconfirmed years, certifications, education, projects, or allocations.

## Commercial

- [ ] Build effort and vendor costs from the final architecture and integration answers.
- [ ] Confirm component prices, shared costs, first-year recurring costs, usage allowance, overage units, support, and renewal basis.
- [ ] Confirm all budget totals marked **[ATHIF TO CONFIRM]**.
- [ ] Confirm HST treatment and total.
- [ ] Do not add an after-hours rate, discount, validity period, credit, or warranty unless approved and required.
- [ ] Ensure the SLA distinguishes design target from contractual floor and contains defined measurement, exclusions, severity, clocks, and remedies.
- [ ] Remove any unbounded 99 percent availability or universal two-second response language.

## Final editorial and packaging

- [ ] Use Canadian English throughout.
- [ ] Search the final response, forms, metadata, and exported PDF for em dashes.
- [ ] Check that the cover has the correct short title, value proposition, buyer, bidder, draft date, running header, and footer.
- [ ] Check every Table of Contents link and heading after conversion.
- [ ] Check tables, URLs, page breaks, headers, footers, accessibility tags, and selectable text in the exported PDF.
- [ ] Remove this checklist.
- [ ] Remove every "INTERNAL DRAFT: NOT FOR SUBMISSION" marker only after Athif approves the submission version.
- [ ] Remove all unresolved placeholders or make an explicit, accurate disclosure in the final bid.
- [ ] Athif gives final approval and personally submits through the official channel.

The Alpha Nova | Confidential | INTERNAL DRAFT: NOT FOR SUBMISSION
