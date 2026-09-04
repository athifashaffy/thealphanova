**INTERNAL DRAFT. NOT FOR SUBMISSION. THE ALPHA NOVA.**

Do not email the buyer. Do not upload to yellowknife.bidsandtenders.ca. Every field marked `[ATHIF TO CONFIRM FROM OFFICIAL PDF]` must be replaced from the official RFP document before this leaves the company. Strip every block marked INTERNAL before any submission.

---

TAN · THE ALPHA NOVA INC.
AI. Software. IoT. One Technology Partner.

DRAFT DATE: 2026-09-04
STATUS: Internal draft, fit MAYBE, official PDF not yet reconciled

**PROTECTIVE SERVICES SOFTWARE PORTFOLIO ASSESSMENT**
**Vendor-neutral current-state review, gap analysis and roadmap**
**RFP 26-073**

SUBMITTED TO:
City of Yellowknife
Protective Services / Procurement `[ATHIF TO CONFIRM FROM OFFICIAL PDF: department and named contact]`
Procurement via yellowknife.bidsandtenders.ca
Closing: Friday 11 September 2026, 15:00 MDT `[ATHIF TO CONFIRM FROM OFFICIAL PDF]`

SUBMITTED BY:
The Alpha Nova Inc.
1545 Maley Drive, Greater Sudbury ON P3A 4R7
info@thealphanova.com · +1 437 424 5384
Signing authority: Athif Shaffy, Founder & CEO

An independent, vendor-neutral assessment of the software the City's Protective Services division relies on today, with a costed, sequenced roadmap the City can take to Council and to market on its own terms.

www.thealphanova.com

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.

---

## Table of Contents

The headings below follow the default MineOpportunity structure. Re-order them to the RFP's rated headings once the official PDF is read. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: evaluation criteria, weights, page limit, required forms]`

1. Understanding of the Project
2. Relevant Experience and References
3. Approach and Methodology
4. Work Plan, Deliverables and Assumptions
5. Team
6. Fees (proposed, not submitted)
7. Compliance Matrix (internal working table)

Appendix A. Resumes
Appendix B. Questions we would have asked (NOT SENT)
INTERNAL. Athif checklist (strip before bid)

---

## 1. Understanding of the Project

### 1.1 What the City is buying

The City of Yellowknife is buying an assessment, not a system. RFP 26-073 asks a consultant to look across the software portfolio that Protective Services depends on, describe honestly how well it serves the division today, and hand the City a defensible picture of what should change, in what order, and at what rough cost. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: exact scope statement, list of in-scope applications, and whether CAD is in scope or is provided through a territorial or regional dispatch arrangement]`

We read "portfolio" broadly and will confirm the boundary with the City in week one. In a division of this shape the portfolio typically includes some or all of the following: computer-aided dispatch and call handling; fire and emergency records management; incident and patient care reporting; pre-incident planning and inspections; hydrant, apparatus and equipment records; staff scheduling, certification and training records; municipal enforcement ticketing and case files; emergency management and public alerting; and the reporting layer that feeds Council, the GNWT and national statistical returns. Several of these are usually delivered by different vendors, several are usually spreadsheets, and the seams between them are usually where the division loses time.

### 1.2 What this engagement is not

This is not a software build. We will not write code for Protective Services under this contract. It is not a product sale. The Alpha Nova does not resell, refer or take commission from any CAD, RMS, fire-service or enforcement software vendor, and we will state that in writing to the City at kick-off. `[ATHIF TO CONFIRM: no reseller, referral or commission agreement with any vendor in this space]` It is not an implementation plan for a product the City has already chosen; if the City has a preferred direction, we will test it rather than rubber-stamp it.

If the City wishes to exclude the assessment consultant from any subsequent implementation procurement that flows from this work, we accept that condition. We would rather the City receive advice it can trust than position ourselves for the next contract.

### 1.3 The go / no-go we will not paper over

The Alpha Nova has not previously delivered a CAD or RMS portfolio assessment for a Canadian municipality. We say that here, in the buyer-facing text, because an evaluator will find it in our references anyway and because the method we propose does not depend on having done one before. It depends on structured discovery, on knowing how operational software behaves in remote and connectivity-constrained environments, and on being independent of every vendor whose product we will be assessing. Our relevant background is in industrial operations technology, health-sector software carrying sensitive personal data, and public-sector-adjacent product work in Northern Ontario. Section 2 sets that out without inflation.

### 1.4 What matters most in Yellowknife

Three things shape this assessment and we want the City to see that we understand them.

**Northern and offline reality.** Yellowknife's connectivity depends on a small number of long-haul links. Fibre cuts, satellite fallback and weather-related outages are operational facts, not edge cases. Any recommendation that assumes an always-on cloud console in a fire hall, an ambulance or a bylaw vehicle is not a recommendation for Yellowknife. Every option we assess will be scored explicitly for degraded-connectivity behaviour: what still works, what queues, what is lost, and how the division recovers.

**Small teams carrying large mandates.** Protective Services staff are operators first. Software that adds administrative load, duplicates data entry or requires a specialist administrator the City does not have will fail regardless of feature count. Our interviews are built around the shift, the call and the report, not around vendor feature lists.

**Territorial privacy and records obligations.** Information about incidents, patients and enforcement subjects is sensitive personal information under NWT access and privacy legislation. Data residency, retention, audit trails and disclosure workflows will be assessed as first-order requirements, not as a compliance footnote. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: whether the RFP names specific legislation or records-retention schedules]`

### 1.5 Outcomes the City should expect

At the end of the engagement the City will hold an application inventory it did not have before, a requirements baseline written in the City's own language, an options analysis that compares "keep", "consolidate", "integrate" and "replace" paths on the same criteria, and a roadmap that a Director can defend to Council and a procurement officer can turn into a future RFP without hiring us again.

---

## 2. Relevant Experience and References

### 2.1 About The Alpha Nova

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. We build intelligent software and industrial systems across four connected capabilities: AI and Intelligent Systems; Industrial IoT and Edge; Software Engineering; and Product Engineering. We are a small firm and we staff engagements with the people named in this proposal, not with a bench we describe and then substitute.

Our founder has spent the last several years in and around mining technology in Northern Ontario, an environment that shares Yellowknife's core operational constraints: remote sites, intermittent connectivity, safety-critical workflows, and staff who need software to work the first time underground or at minus forty. That is the lens we bring to Protective Services.

### 2.2 Why we are a strong fit, honestly

- **Vendor independence.** We do not sell or implement any of the products likely to be in the City's portfolio. Our only commercial interest is in the assessment being useful.
- **Operational technology in hard environments.** Through the founder's tenure at Maestro Digital Mine (November 2022 to February 2025) and the company's Industrial IoT and Edge practice, we understand offline-first design, store-and-forward telemetry and edge devices that must keep working when the link drops.
- **Sensitive personal data.** COGITO, built with the University Medical Center Hamburg-Eppendorf (UKE), carries mental-health data under GDPR, with offline capability and end-to-end encryption. The privacy and audit discipline transfers directly to incident, patient and enforcement records.
- **Frontline UX and accessibility.** Our UI consultant works to AODA and WCAG standards and has run discovery with non-technical users; that is exactly the skill an assessment interview with a firefighter or bylaw officer needs.
- **Enterprise platform depth.** Our senior developer has current, hands-on Microsoft 365, SharePoint and Exchange experience, which matters because a large share of any municipal "shadow portfolio" lives in Excel, Outlook and shared drives and has to be assessed as seriously as the licensed systems.

### 2.3 Where we are weaker, and what we do about it

We have no completed municipal CAD/RMS assessment to point to, and we have no NASSCO, NFPA or NENA credential holders on staff. `[ATHIF TO CONFIRM: any relevant certifications]` We mitigate this with a written, repeatable method (Section 3), by grounding the requirements baseline in the City's own operators rather than in our prior assumptions, and by offering the City direct access to our reference clients so evaluators can test how we behave when we are learning a domain.

### 2.4 Public work the City may examine

Cited only where relevant to this engagement. None of these is a municipal reference and we do not present them as one.

- **COGITO (UKE Hamburg).** Gamified mental-health app; multi-language; clinician dashboard; offline operation; GDPR controls. Relevance: sensitive personal data, offline-first, clinical stakeholders with no time for bad software.
- **Côté Gold Blast Captain AI Challenge (IAMGOLD, Laurentian, Cambrian, GDG Sudbury).** First place of 29 teams. Relevance: rapid discovery and delivery in a real industrial operating context.
- **Cambrian College Alumni App.** Cross-platform product for a public post-secondary institution. Relevance: public-sector-adjacent stakeholder management and delivery to completion.
- **Wheel It Transportation (Greater Sudbury).** Accessibility-focused transportation software. Relevance: small operator, real-world constraints, accessibility as a requirement rather than a feature.
- **VanGuardian.** Our own AI fall-detection product without wearables; privacy-first sensor design. Relevance: safety-critical alerting under strict privacy constraints.

### 2.5 References

Only confirmed, live contacts are listed. The City may contact each directly.

| Reference | Organisation | Contact | Relationship |
| --- | --- | --- | --- |
| Prof. Dr. Steffen Moritz | University Medical Center Hamburg-Eppendorf (UKE) | moritz@uke.de · +49 40 7410 56565 | Client for COGITO. Also serves as Lead Scientific Advisor to The Alpha Nova; this dual role is disclosed so the City can weigh the reference accordingly. |
| Karen Hastie | One Chamber System | karen@onechambersystem.com · +1 705 669 7343 | Client, Chamber Perks `[ATHIF TO CONFIRM: dates to cite]` |
| Shaunna Babyak | Wheel It Transportation | info@wheelittransportation.com · +1 705 929 8006 | Client, accessibility-focused transportation software |

Disclosure: Dr. Markus Lehmann is a Strategic Advisor to The Alpha Nova. He is not offered as a client reference.

---

## 3. Approach and Methodology

### 3.1 Principles

1. **Vendor-neutral by construction.** Options are compared at the category level on criteria the City agrees in advance. Named products appear only in a market scan appendix, never as a recommendation the City did not ask for.
2. **Operators before architecture.** We interview shift crews, dispatchers and enforcement officers before we open a single vendor contract.
3. **Degraded mode is a scored criterion.** Every current-state finding and every option is rated for behaviour on a satellite backhaul, on a dead link, and on recovery.
4. **The City owns the artefacts.** Inventory, interview notes, requirements and scoring workbooks are delivered in editable formats the City can reuse in a future procurement without us.
5. **Remote-first, on-site by choice.** The base engagement is delivered remotely across MDT working hours. An optional on-site week is available (Section 4.5) but the method does not depend on it.

### 3.2 Method

**Phase 0. Mobilise (week 1).** Kick-off with the City project lead. Confirm the in-scope application list, stakeholder roster, document access and communication cadence. Issue the data request (contracts, licence counts, support tickets, network topology summary, incident volumes, existing policies). Agree the evaluation criteria and weights that will be used in Phase 3 so the City, not the consultant, defines "good".

**Phase 1. Inventory and discovery (weeks 2 to 4).** Build the application inventory register: every licensed system, every spreadsheet and Access database doing system-like work, every integration and every manual hand-off. Capture owner, users, licence, cost, hosting, data sensitivity, connectivity dependence, support status and end-of-life exposure. Run structured interviews (45 to 60 minutes) with a cross-section of Protective Services roles and with IT, Finance and the Clerk's or records function. Observe at least two shifts remotely via screen-share where practical. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: expected stakeholder count]`

**Phase 2. Current-state and gap analysis (weeks 4 to 6).** Map the incident lifecycle and the enforcement case lifecycle end to end across systems. Identify duplicate entry, data loss points, reporting gaps, single points of failure and offline failure modes. Assess privacy, retention and audit posture against the City's obligations. Produce a heat map of pain against cost and against risk.

**Phase 3. Requirements baseline and options analysis (weeks 6 to 9).** Write functional and non-functional requirements in the City's language, tagged Must / Should / Could, including explicit offline, data-residency, accessibility and reporting requirements. Define options at category level (retain and remediate; consolidate onto an existing platform; integrate around existing systems; replace one or more systems) and score them on the agreed criteria. Include a market scan of product categories and representative vendors for the City's information, kept separate from the recommendation and clearly labelled as not evaluated in depth.

**Phase 4. Roadmap and business case inputs (weeks 9 to 11).** Sequence the recommended path into phases with dependencies, indicative effort bands, rough-order-of-magnitude cost ranges (labelled as such, with the basis stated), staffing implications and risks. Draft the procurement-ready requirements section the City can lift into a future RFP.

**Phase 5. Final report and briefing (week 12).** Executive summary, full report, all working artefacts, and a briefing for the Director and, if the City wishes, for Council or a committee. One round of consolidated City comments is included before final issue.

### 3.3 Quality and independence controls

- Every finding traceable to an interview, a document or an observation, referenced in the report.
- Requirements reviewed by a second Alpha Nova team member who did not conduct the interview.
- Options scoring workbook delivered with formulas visible so the City can change a weight and see the result move.
- Written independence statement signed by the Founder & CEO at kick-off.

---

## 4. Work Plan, Deliverables and Assumptions

### 4.1 Schedule

Twelve weeks from kick-off, remote delivery. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: required completion date or contract term]`

| Week | Phase | Milestone |
| --- | --- | --- |
| 1 | 0 Mobilise | Scope confirmed, criteria agreed, data request issued |
| 2 to 4 | 1 Inventory and discovery | Inventory register v1; interview programme complete |
| 4 to 6 | 2 Current-state and gap analysis | Current-state report; lifecycle maps; heat map |
| 6 to 9 | 3 Requirements and options | Requirements baseline; options analysis; market scan |
| 9 to 11 | 4 Roadmap | Roadmap; ROM cost ranges; procurement-ready requirements |
| 12 | 5 Final report and briefing | Final report; briefing delivered; artefacts handed over |

### 4.2 Deliverables

1. Application inventory register (spreadsheet, City-editable)
2. Stakeholder interview programme summary (anonymised where requested)
3. Current-state assessment with incident and enforcement lifecycle maps
4. Requirements baseline, functional and non-functional, Must / Should / Could
5. Options analysis and scoring workbook, formulas visible
6. Category-level market scan (informational, not a recommendation)
7. Roadmap with phases, dependencies, ROM cost ranges and risks
8. Procurement-ready requirements text for any future RFP
9. Executive summary and final report
10. Director and Council-level briefing deck and delivery of one briefing session

### 4.3 City responsibilities

- A single project lead with authority to schedule interviews and release documents
- Access to contracts, licence records, support history and a network summary
- Stakeholder availability for interviews within the Phase 1 window
- One consolidated round of comments on the draft report within ten working days

### 4.4 Assumptions

- Interviews and workshops are conducted remotely in MDT working hours; the City provides Microsoft Teams or equivalent
- Up to twenty stakeholder interviews are included; more are available at the rates in Section 6
- No software is procured, installed or configured under this engagement
- The City owns all deliverables on final payment

### 4.5 Optional on-site week (not in base)

Five working days in Yellowknife, typically during Phase 1, for in-person ride-alongs, station visits and a records-room review. Labour is priced at the standard software rate in Section 6. Travel, accommodation and per diems are additional at cost with no mark-up. `[ATHIF TO CONFIRM: travel estimate before offering a number]` The base method does not depend on this option.

---

## 5. Team

Roles below are the roles these individuals hold at The Alpha Nova and are drawn from our public About page. Detailed resumes are in Appendix A.

| Name | Role on this engagement | Title at The Alpha Nova | Commitment |
| --- | --- | --- | --- |
| Athif Shaffy | Engagement lead; lead assessor; author of options and roadmap | Founder & CEO | Lead throughout; primary City contact |
| Ertugrul Sahin | Technical assessor: architecture, integration, hosting, M365 shadow portfolio | Senior Software Developer | Phases 1 to 4 |
| Deepshika Ghale | Frontline UX and accessibility assessor; interview design | UI Consultant | Phases 1 to 3 |
| Shubham Dhamane | Business analyst: inventory register, requirements baseline, lifecycle maps | Business Analyst | Phases 1 to 4 |
| Laxman KC | QA and test-scenario author for requirements validation | Software Developer | Phase 3 |
| Cheick Ismael Maiga, P.Eng. | Technical advisor; advisory review of findings | Technical Advisor | Review points end of Phases 2 and 4 |

Advisors disclosed: Dr. Markus Lehmann (Strategic Advisor; not a client reference) and Prof. Dr. Steffen Moritz (Lead Scientific Advisor and COGITO client) advise the company and are not assigned to this engagement.

---

## 6. Fees (proposed, not submitted)

INTERNAL NOTE: this build-up was drafted before the official PDF was read. It is a proposed figure. Confirm the RFP's pricing form, tax treatment and whether fees belong in a separate envelope before any of this is placed in the submission. `[ATHIF TO CONFIRM FROM OFFICIAL PDF]`

Base fee, fixed price, remote delivery: **CAD $24,520 excluding applicable taxes.**

Tax note: the earlier draft said "excl. HST". Yellowknife is in the Northwest Territories, where GST at 5% applies and there is no HST. State "excluding GST" on the pricing form unless the RFP prescribes otherwise.

| Role | Rate | Effort | Amount |
| --- | --- | --- | --- |
| Lead assessor / technical assessor (software rate) | $640 per day ($80 per hour) | 28 days | $17,920 |
| UX and accessibility assessor (design rate) | $600 per day ($75 per hour) | 7 days | $4,200 |
| QA and requirements validation (QA rate) | $400 per day ($50 per hour) | 6 days | $2,400 |
| **Base total** | | **41 days** | **$24,520** |

Business analyst and P.Eng. advisory review time is absorbed within the lead assessor allocation and is not billed separately.

Payment milestones (proposed): 30% on acceptance of the inventory register; 40% on acceptance of the options analysis; 30% on delivery of the final report and briefing.

Optional items, priced at the rates above:
- On-site week in Yellowknife: 5 days at $640 = $3,200 labour, plus travel at cost `[ATHIF TO CONFIRM travel estimate]`
- Additional stakeholder interviews beyond twenty: $80 per hour, including write-up
- Second Council or committee briefing: $640

---

## 7. Compliance Matrix (internal working table)

Populate from the official PDF. Each RFP requirement maps to a section of this draft and records any gap.

| RFP requirement (from official PDF) | Draft section | Status / gap |
| --- | --- | --- |
| Mandatory forms and signatures | INTERNAL checklist | `[ATHIF TO CONFIRM FROM OFFICIAL PDF]` |
| Company profile | 2.1 | Complete |
| Relevant experience | 2.2 to 2.5 | Honest gap stated: no prior municipal CAD/RMS assessment |
| Methodology | 3 | Complete; re-order to RFP headings |
| Work plan and schedule | 4 | Confirm required completion date |
| Team and resumes | 5, Appendix A | Complete |
| Fees | 6 | Proposed only; confirm pricing form and tax wording |
| Insurance / WCB (NWT WSCC) | INTERNAL checklist | Not stated in draft; do not invent |
| Addenda acknowledgement | INTERNAL checklist | Check portal |

---

## Appendix A. Resumes

Facts below are limited to what The Alpha Nova has confirmed. Items marked `[ATHIF TO CONFIRM]` are to be completed or removed before submission.

### Athif Shaffy, Founder & CEO (Greater Sudbury, Ontario)

Engagement lead and lead assessor. Seven-plus years in software and technology delivery. Founded The Alpha Nova in September 2020 and has led it since, setting company strategy, client partnerships and product direction. From November 2022 to February 2025 he worked at Maestro Digital Mine, a Sudbury-based mining technology company, gaining direct exposure to operational technology in remote, connectivity-constrained industrial environments `[ATHIF TO CONFIRM: role title]`. Instructor at Cambrian College `[ATHIF TO CONFIRM: programme and dates]`. BSc, First Class Honours, Staffordshire University `[ATHIF TO CONFIRM: programme title]`. Active in Google Developer Group Sudbury `[ATHIF TO CONFIRM: role]`. Awards: first place, Côté Gold Blast Captain AI Challenge (IAMGOLD, 29 teams); first place, Comms-Denied Autonomy challenge, York, 2026. Relevance to this engagement: leads discovery and options work, owns the roadmap, and brings hands-on understanding of software that must operate when the link is down.

### Ertugrul Sahin, Senior Software Developer

Technical assessor. Leads complex feature development and system architecture at The Alpha Nova (March 2026 to present), guiding engineering quality across the team. Previously Research and Development at Cambrian College, March 2023 to March 2026. Computer Engineering, Beykent University. Working depth in Microsoft 365, SharePoint and Exchange, which covers the shadow portfolio of spreadsheets, mailboxes and shared drives that every municipal assessment must account for. First place, Côté Gold Blast Captain AI Challenge. Relevance: architecture, integration and hosting assessment; degraded-connectivity analysis.

### Deepshika Ghale, UI Consultant (Greater Sudbury, Ontario)

Frontline UX and accessibility assessor. UI Consultant advising The Alpha Nova since March 2025 on interface and user experience, working in Figma and prototyping tools. Applies AODA and WCAG accessibility standards. First place, Cursor hackathon, Sudbury, 2026. Relevance: designs and runs stakeholder interviews with operators, evaluates usability and accessibility of current systems, and turns findings into requirements.

### Shubham Dhamane, Business Analyst (Greater Sudbury, Ontario)

Business analyst. Bridges business and engineering at The Alpha Nova, translating client goals into clear requirements and measurable value. Relevance: owns the inventory register, lifecycle maps and the Must / Should / Could requirements baseline. `[ATHIF TO CONFIRM: start date and prior experience to cite]`

### Laxman KC, Software Developer

QA and requirements-validation author. Software Developer at The Alpha Nova since January 2024, shipping features across web and mobile products. Research and Development at Cambrian College since December 2024. Works in computer vision and telemetry. Multiple hackathon awards in 2026. Relevance: writes test scenarios against the requirements baseline so the City can validate future vendor claims.

### Cheick Ismael Maiga, P.Eng., Technical Advisor

Professional Engineer advising across The Alpha Nova's engineering projects. Provides advisory review of findings and the options analysis at two checkpoints. He is The Alpha Nova's Technical Advisor, not an independent third-party reviewer. `[ATHIF TO CONFIRM: licensing jurisdiction and discipline to cite]`

### Advisors (disclosed, not assigned)

Dr. Markus Lehmann, Strategic Advisor, advises on technology strategy and enterprise architecture. Not presented as a client reference. Prof. Dr. Steffen Moritz, Lead Scientific Advisor, University Medical Center Hamburg-Eppendorf; also the client for COGITO and listed as a reference with that dual role disclosed.

---

## Appendix B. Questions we would have asked (NOT SENT)

INTERNAL. These were not submitted through the portal. Check the question deadline in the official PDF; if it has not passed, decide which of these are worth asking. If it has passed, use them as assumptions in Section 4.4. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: question deadline]`

1. Which applications does the City consider in scope? In particular, is computer-aided dispatch provided by the City or through a territorial or third-party arrangement, and is it to be assessed?
2. Approximately how many staff across Protective Services, IT, Finance and records should the consultant expect to interview?
3. Does the City expect a shortlist of named products, or a category-level options analysis with a market scan?
4. Is on-site presence in Yellowknife required or preferred, or is remote delivery acceptable?
5. Is there a budget range or a not-to-exceed figure for this assessment?
6. Is there a required completion date tied to a budget cycle or Council calendar?
7. Will the consultant be excluded from any subsequent implementation procurement?
8. Is there a page limit or a prescribed format for the technical submission?
9. Are insurance, WSCC (NWT) or business licence requirements applicable to a remote Ontario consultant, and if so at what thresholds?
10. Are there existing IT strategy, records-retention schedule or network documentation the consultant should assume access to?

---

## INTERNAL. Athif checklist (strip before bid)

- [ ] Official PDF downloaded from yellowknife.bidsandtenders.ca and every `[ATHIF TO CONFIRM FROM OFFICIAL PDF]` replaced or removed
- [ ] Section headings re-ordered to the RFP's rated criteria; TOC updated
- [ ] Named contact, closing date and time verified against the PDF (draft says Fri 11 Sep 2026 15:00 MDT)
- [ ] Addenda downloaded and acknowledged in the portal
- [ ] Mandatory forms filled and signed
- [ ] Insurance, NWT WSCC clearance, business licence: only stated if the PDF requires it and only if we actually hold it; otherwise ask or note as "to be provided on award"
- [ ] Vendor-independence statement confirmed true (no reseller or referral agreements)
- [ ] Fee build-up ($24,520) confirmed as our number; tax wording changed from HST to GST for NWT; placed only where the pricing form puts it
- [ ] Optional on-site travel estimate obtained before quoting
- [ ] Reference contacts warned they may be called
- [ ] Every INTERNAL block, Appendix B and this checklist deleted from the submission copy
- [ ] No em dashes; run a search
- [ ] Athif said yes
- [ ] Submit day is not close day (target Thu 10 Sep 2026)

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.
