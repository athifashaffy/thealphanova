**INTERNAL DRAFT. NOT FOR SUBMISSION. THE ALPHA NOVA.**

Do not email the buyer. Do not upload to abbotsford.bidsandtenders.ca. All buyer contact goes through the bidding system only. Fees are entered in the portal's fee fields, never in the technical sections below. Strip every block marked INTERNAL before any submission.

---

TAN · THE ALPHA NOVA INC.
AI. Software. IoT. One Technology Partner.

DRAFT DATE: 2026-09-04
STATUS: Internal draft, fit MAYBE, Addendum 1 reviewed, commercial decision pending (see INTERNAL Section 6)

**INTEGRATED MOBILE PLATFORM**
**A productized civic mobile layer, integrated with the City's SAP PM, CentralSquare Works and Esri estate**
**RFP 1220-2026-4120**

SUBMITTED TO:
City of Abbotsford
Procurement Services
Attention: Megan Clarke, Buyer II
Procurement via abbotsford.bidsandtenders.ca (all communication through the bidding system)
Closing: Monday 21 September 2026, 14:00 PDT
Questions deadline: Tuesday 8 September 2026, 14:00 PDT

SUBMITTED BY:
The Alpha Nova Inc.
1545 Maley Drive, Greater Sudbury ON P3A 4R7
info@thealphanova.com · +1 437 424 5384
Signing authority: Athif Shaffy, Founder & CEO

A resident-facing and staff-facing mobile platform the City configures rather than rebuilds, connected to SAP PM, CentralSquare Works and Esri through a maintained integration layer, delivered by a Canadian team.

www.thealphanova.com

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.

---

## Table of Contents

The RFP scores the technical submission against Appendix D, Sections S1 to S5, with fees captured separately in the portal. The five sections below are written to be pasted into S1 to S5 in order. `[ATHIF TO CONFIRM: exact S1 to S5 headings and any word or page limits from Appendix D]`

1. Understanding of the Project (S1)
2. Company Experience and References (S2)
3. Proposed Solution and Integration Approach (S3)
4. Implementation Work Plan, Support and Transition (S4)
5. Team (S5)
6. INTERNAL. Commercial position (Athif only, never in the technical file)
7. Compliance Matrix (internal working table)

Appendix A. Resumes
INTERNAL. Athif checklist (strip before bid)

Open questions for the City are kept in a separate file, `ABBOTSFORD-QUESTIONS-TO-SEND.md`, for Athif to post through the bidding system before Tue 8 Sep 2026 14:00 PDT.

---

## 1. Understanding of the Project (S1)

### 1.1 What the City is buying

The City of Abbotsford is buying an integrated mobile platform: a single mobile experience for residents and for City staff that sits in front of three systems the City already owns and will keep. Addendum 1 makes the landscape concrete. Work management runs in SAP Plant Maintenance, with notifications created and displayed through IW21 and IW26 and work orders created through IW31. Spatial data runs in Esri ArcGIS Enterprise 11.5 on-premises alongside ArcGIS Online. Service requests and related civic workflows run in CentralSquare Works, currently v25.3 and moving to the v26.1 cloud release. The platform must serve more than 10,000 public mobile users and more than 30 named staff users. `[ATHIF TO CONFIRM FROM OFFICIAL PDF AND ADDENDUM 1: functional scope list, e.g. service requests, notifications, maps, payments, permits, staff field intake]`

We read the requirement as a front door and a set of connectors, not as a replacement for any of these systems. Residents should be able to report, request, track and be notified from one app. Staff should be able to receive, triage and close work from a mobile device with the record of truth remaining in SAP PM, CentralSquare Works and Esri. The platform's job is to make those three systems feel like one to the person holding the phone.

### 1.2 What this engagement is not

It is not an ERP, work-management or GIS replacement. It is not a custom build from zero that the City then has to maintain. It is not a consumer app with a City logo and no back-office connection. Any proposal that treats the three integrations as afterthoughts is proposing a second silo.

### 1.3 Our honest position on the integrations

The Alpha Nova has not implemented SAP PM, CentralSquare Works or Esri Enterprise for a British Columbia municipality. We state this in the technical submission because it is true and because the evaluators will check. Our integration approach (Section 3) is standards-based and sandbox-first precisely so that it does not depend on prior tribal knowledge of the City's specific configuration. Where the SAP landscape requires work inside SAP (RFC-enabled function modules, OData services on SAP Gateway, PI/PO or BTP integration flows), we assume that work is performed by the City's SAP team or SAP partner and we consume the resulting interface. Where the CentralSquare API surface or sandbox is not available to third parties, we need the City to broker access. Both points are raised as questions in the separate questions file.

### 1.4 What matters most in Abbotsford

- **Scale and reliability at the public edge.** More than 10,000 residents will use this on days when a storm, a water main break or a wildfire smoke event drives everybody to the same "report an issue" button at once. Queueing, back-pressure and graceful degradation are design requirements, not operational tuning later.
- **Staff mobility that respects the record of truth.** Thirty-plus staff need to work in the field with intermittent coverage and see their action land in SAP PM or CentralSquare Works, once, correctly, with a photo and a location that Esri recognises.
- **Privacy and Canadian residency.** Resident reports contain names, addresses, photos and sometimes complaints about neighbours. BC's FIPPA and the City's own policies govern where that personal information may be stored and processed. Our default is Canadian-region hosting with no personal information leaving Canada; we have asked the City to confirm its residency requirement.
- **A three-year total cost the City can live with.** Addendum 1 gives the City's total for the three-year term. We respect it by proposing a productized layer that the City configures rather than a bespoke build that has to be paid for line by line. Commercial detail is in the portal fee fields only.
- **Transition from the incumbent.** Whatever the City uses today holds resident accounts, open requests and history. A migration path and a clean export are part of the job.

---

## 2. Company Experience and References (S2)

### 2.1 About The Alpha Nova

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. We build intelligent software and industrial systems across four connected capabilities: AI and Intelligent Systems; Industrial IoT and Edge; Software Engineering; and Product Engineering. We have delivered cross-platform mobile products for a public post-secondary institution, a university hospital and small operators, and we build and own products of our own, which is where our productized civic layer comes from.

### 2.2 Why we are a strong fit, honestly

- **Mobile product delivery to completion.** The Cambrian College Alumni App is a cross-platform iOS and Android product for a public institution, delivered from concept to production with a client who will speak to that.
- **Sensitive data and offline behaviour.** COGITO, built with the University Medical Center Hamburg-Eppendorf, handles mental-health data under GDPR, works offline and syncs when it can. Those are the same constraints a field worker in a coverage gap imposes.
- **Integration and platform depth.** Our senior developer leads architecture across the team and has current Microsoft 365, SharePoint and Exchange integration experience; our developers work in telemetry and computer-vision pipelines, which is where photo intake, geotagging and automated triage of resident reports come from.
- **Accessibility.** Our UI consultant works to WCAG and AODA. A resident app for a city of Abbotsford's size will be used by people with low vision, motor impairments and older devices, and BC public bodies are increasingly held to WCAG 2.1 AA in practice.
- **A product mindset.** We do not want to bill the City for the same login screen every other municipality has already paid for. The civic layer is maintained as a product; the City pays for configuration, integration and support.

### 2.3 Where we are weaker

No SAP PM, CentralSquare Works or Esri Enterprise implementation for a BC municipality. No production Esri or SAP reference at all; we do not claim one. We mitigate with a standards-based integration architecture, a sandbox-first plan that proves each connector before build, explicit dependency on the City's SAP and CentralSquare partners for their side of each interface, and a demonstration the City can inspect.

### 2.4 Public work the City may examine

- **Cambrian College Alumni App.** Cross-platform mobile app: directory, events, career portal, push notifications, content feed. Public-sector client; delivered to completion.
- **COGITO (UKE Hamburg).** Mobile mental-health app; multi-language; offline; clinician dashboard; GDPR. Demonstrates privacy-sensitive mobile at scale.
- **Wheel It Transportation (Greater Sudbury).** Accessibility-focused transportation software for a small operator.
- **VanGuardian.** Our own AI product; shows we build and maintain products, not only projects.
- **Côté Gold Blast Captain AI Challenge.** First of 29 teams; computer-vision pipeline on drone video. Relevant to automated photo triage of resident reports.

None of the above is a municipal reference and none involves SAP PM, CentralSquare or Esri in production. We present them for what they are.

### 2.5 References

| Reference | Organisation | Contact | Relationship |
| --- | --- | --- | --- |
| Prof. Dr. Steffen Moritz | University Medical Center Hamburg-Eppendorf (UKE) | moritz@uke.de · +49 40 7410 56565 | Client for COGITO. Also Lead Scientific Advisor to The Alpha Nova; dual role disclosed. |
| Karen Hastie | One Chamber System | karen@onechambersystem.com · +1 705 669 7343 | Client `[ATHIF TO CONFIRM: project to cite]` |
| Shaunna Babyak | Wheel It Transportation | info@wheelittransportation.com · +1 705 929 8006 | Client |

Disclosure: Dr. Markus Lehmann is a Strategic Advisor to The Alpha Nova and also appears as a client testimonial on our website. He is not offered as an independent reference.

---

## 3. Proposed Solution and Integration Approach (S3)

### 3.1 Architecture in one paragraph

A configurable civic mobile application (iOS and Android from one codebase, plus a responsive web fallback) for residents and a role-gated staff mode for the 30-plus staff users, both talking to a Canadian-hosted integration layer we call the civic hub. The hub owns identity federation, request routing, media handling, notification fan-out, offline queueing and an audit log. Three connectors hang off the hub: one for CentralSquare Works (service requests and their status lifecycle), one for SAP PM (notifications via the IW21/IW26 pattern and work orders via the IW31 pattern, consumed through the interface the City's SAP team exposes), and one for Esri (address and asset lookup, geofencing, map layers from ArcGIS Enterprise 11.5 and ArcGIS Online, and feature writes where the City permits). The record of truth never lives in the hub; the hub holds routing state, a cache for resilience and the audit trail.

### 3.2 The productized civic layer

The resident app, the staff mode and the hub are maintained by The Alpha Nova as a product. Per-client work is configuration: branding, service catalogue, form fields, routing rules, notification templates, map layers and role definitions. Product improvements ship to every client; City-specific configuration stays the City's. We say plainly that this layer has not yet been deployed for a BC municipality; the City would be an early adopter, and Section 4 reflects that with a longer pilot and a heavier acceptance stage than a mature product would need. `[ATHIF TO CONFIRM: what of the civic layer exists today versus what is planned, so the wording is exactly true]`

### 3.3 Integration approach by system

**CentralSquare Works (v25.3 to 26.1 cloud).** Service request create, update, attach media, status read and closure through the CentralSquare Works API. Status changes flow back to the resident as notifications. We need confirmation of API availability to third parties, a sandbox tenant, and the 26.1 cut-over date so the connector is built once against the target release. Until confirmed, we treat this as the highest integration risk.

**SAP Plant Maintenance (IW21 / IW26 / IW31).** Staff field intake and qualifying resident reports create PM notifications (IW21 semantics), read notification status (IW26 semantics) and, where the City's business rules allow, create work orders (IW31 semantics). We consume an interface the City's SAP landscape exposes: OData on SAP Gateway, RFC-enabled BAPIs through a middleware, or integration flows on SAP BTP or PI/PO. Building or exposing that interface inside SAP is assumed to be the City's or its SAP partner's responsibility; we specify it, test against it and handle idempotency, retries and reconciliation on our side. This assumption is stated in the questions file.

**Esri (ArcGIS Enterprise 11.5 on-premises and ArcGIS Online).** Address geocoding and asset lookup through ArcGIS REST services; map layers rendered in-app through the ArcGIS Maps SDK; geofencing to route a report to the right service area; optional feature-service writes for staff field observations. We need the service URLs, the authentication model (ArcGIS Enterprise portal, OAuth, or a proxy) and any network path from a cloud hub to an on-premises Enterprise instance, which usually means a reverse proxy or a City-hosted relay.

### 3.4 Non-functional commitments

- **Hosting and residency.** Canadian-region cloud hosting; no resident personal information stored or processed outside Canada. `[ATHIF TO CONFIRM: named provider and region we will actually use]`
- **Scale.** Designed for more than 10,000 public users with burst handling by queueing at the hub; connectors drain at the rate each back-end tolerates so a surge never takes down SAP or CentralSquare.
- **Offline.** Staff mode captures work, photos and location offline and syncs with conflict detection when coverage returns.
- **Security.** Staff single sign-on through the City's identity provider (Entra ID or as confirmed); resident accounts with social or email login and no password reuse against City systems; encrypted in transit and at rest; full audit log of every write to a back-end.
- **Accessibility.** WCAG 2.1 AA target for the resident app and web fallback, tested with screen readers on both platforms.
- **App store ownership.** Apps published under the City's Apple and Google developer accounts so the City owns its listing, ratings and history; confirmed as a question.
- **Observability.** Connector health, queue depth and error budgets visible to City IT.

### 3.5 Migration from the incumbent

Export of resident accounts, open requests and history from the current platform; transformation to the hub model; load into CentralSquare Works where the City wants history to live; resident re-consent where required. Dependency: an export from the incumbent, which we have asked the City to confirm it can obtain.

---

## 4. Implementation Work Plan, Support and Transition (S4)

### 4.1 Phases

| Phase | Weeks | What happens | Exit criterion |
| --- | --- | --- | --- |
| 0 Mobilise and access | 1 to 2 | Kick-off, RACI, sandbox and credential requests to SAP, CentralSquare and Esri owners, residency and IdP confirmation | All three sandboxes reachable or a dated plan for each |
| 1 Configure and prove | 3 to 8 | Civic layer configured to the City's service catalogue; each connector proven in sandbox with a traceable round trip | Three connector proofs signed off |
| 2 Pilot | 9 to 14 | Staff pilot with a subset of the 30-plus users; resident soft launch to a limited area or service | Pilot exit report; defect burn-down to agreed level |
| 3 Migration and launch | 15 to 18 | Incumbent export and load; app store release under City accounts; communications support | Go-live |
| 4 Hypercare | 19 to 22 | Daily stand-ups with City IT; connector tuning under real load | Transition to support |
| 5 Support | Remainder of the 3-year term | Product updates, connector maintenance including the CentralSquare 26.1 transition, security patches, response and resolution targets | Term end or renewal |

Timing note: the RFP indicates contract execution on or about 30 October 2026. We have asked whether the City has a target go-live date, because eighteen weeks from execution lands in early March 2027 before any holiday slippage. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: execution and go-live dates]`

### 4.2 City responsibilities

- Product owner with authority over the service catalogue and routing rules
- SAP team or partner to expose and support the SAP interface
- CentralSquare account owner to broker API and sandbox access
- Esri administrator for service URLs, authentication and network path
- Apple and Google developer accounts in the City's name
- Identity provider configuration for staff SSO
- Export from the incumbent platform

### 4.3 Support model over the term

Named support contact, business-hours response in Pacific time, a severity matrix agreed at contract, product updates at least quarterly, connector regression testing before any back-end upgrade the City schedules, and an annual review. `[ATHIF TO CONFIRM: exact response and resolution targets we can commit to at the fee level in the portal]`

### 4.4 Risks and how we handle them

| Risk | Handling |
| --- | --- |
| CentralSquare API not available to third parties, or 26.1 changes the surface | Confirm before award through the question process; build against 26.1 sandbox only; escalation path through the City's account |
| SAP interface not exposed on time | Phase 0 exit criterion forces a dated plan; staff mode can operate against CentralSquare only until SAP is ready |
| On-premises Esri unreachable from cloud hub | City-hosted relay or reverse proxy specified in Phase 0 |
| Public surge on an emergency day | Hub queueing and rate-limited connectors; static status page fallback |
| Early-adopter product | Longer pilot, heavier acceptance, and source escrow or equivalent continuity assurance `[ATHIF TO CONFIRM]` |

---

## 5. Team (S5)

| Name | Role on this engagement | Title at The Alpha Nova | Commitment |
| --- | --- | --- | --- |
| Athif Shaffy | Engagement lead; product owner counterpart; commercial and escalation contact | Founder & CEO | Throughout |
| Ertugrul Sahin | Solution architect; hub and connector design; SAP and Esri interface specification | Senior Software Developer | Phases 0 to 4, then support escalation |
| Laxman KC | Mobile and connector developer; media pipeline; offline sync; automated photo triage | Software Developer | Phases 1 to 4, then support |
| Deepshika Ghale | UX and accessibility; resident and staff flows; WCAG 2.1 AA testing | UI Consultant | Phases 1 to 3 |
| Shubham Dhamane | Business analyst; service catalogue, routing rules, acceptance criteria, migration mapping | Business Analyst | Phases 0 to 3 |
| Cheick Ismael Maiga, P.Eng. | Technical advisor; architecture review at Phase 1 and Phase 3 gates | Technical Advisor | Review points |

Advisors disclosed and not assigned: Dr. Markus Lehmann (Strategic Advisor; also a website testimonial) and Prof. Dr. Steffen Moritz (Lead Scientific Advisor; also COGITO client and reference).

---

## 6. INTERNAL. Commercial position and the $33,000 question (Athif only)

Never paste any of this into S1 to S5. Fees go only into the portal fee fields.

**The trap.** Addendum 1 states $33,000 TOTAL for the three-year term, and that total includes implementation, configuration, integration and support. At our software rate of $640 per day that is roughly 51.5 person-days across three years for three enterprise integrations, a public app for more than 10,000 users, a staff app for more than 30 users, migration, app store publishing and 30-plus months of support. Blended with design at $600 per day and QA at $400 per day the day count rises slightly but the picture does not change. The Phase 0 to 4 plan in Section 4 alone is about 22 weeks of calendar time; even at one person half-time it exceeds the envelope before support begins.

**Three ways to read it.**
1. It is an estimate the City wrote before it understood the integration cost, and it will move once vendors respond. Evidence for: the figure appeared in an addendum answer, not in the base RFP. Evidence against: the addendum says it is the total.
2. It is a hard ceiling and the City expects a SaaS-style product where implementation is mostly configuration and the vendor recovers cost across many clients. That is the only reading under which the productized civic layer makes any sense at this number, and only if the City's SAP and CentralSquare partners do their sides at their own cost.
3. It is a hard ceiling and the City will get either a thin product with no real SAP or CentralSquare integration, or a vendor who will change-order the rest.

**Options.**
- **No-bid**, with a polite note through the bidding system that the integration scope and the three-year total are not reconcilable at a sustainable rate. Costs nothing, protects reputation.
- **Bid on the productized reading**, pricing a subscription that fits the envelope, with the technical file scoped so that SAP and CentralSquare interfaces are consumed, not built, and the City's partners carry their sides. Every assumption must be written in S3 and S4 so a change order is never a surprise. This still leaves us subsidising early-adopter risk.
- **Ask first.** Post the budget question through the bidding system before Tue 8 Sep 14:00 PDT (it is in the questions file). Decide after the answer.

**Recommendation:** ask first. If the answer confirms a hard $33,000 ceiling inclusive of support, no-bid unless the civic layer exists today to a degree that makes configuration genuinely cheap. Do not bid a build at this number.

Illustrative build-up, for internal reasoning only, at published rates:

| Item | Rate | Days | Amount |
| --- | --- | --- | --- |
| Architecture and connectors (software) | $640 | `[Athif]` | |
| Mobile development (software) | $640 | `[Athif]` | |
| UX and accessibility (design) | $600 | `[Athif]` | |
| QA and pilot support (QA) | $400 | `[Athif]` | |
| Support, 30 months | | | |
| **Total** | | | compare with $33,000 |

---

## 7. Compliance Matrix (internal working table)

| RFP requirement | Draft section | Status / gap |
| --- | --- | --- |
| Appendix D S1 | 1 | Complete; confirm heading text |
| Appendix D S2 | 2 | Honest gap stated: no SAP PM, CentralSquare or Esri implementation for a BC municipality |
| Appendix D S3 | 3 | Complete; confirm what of the civic layer exists today |
| Appendix D S4 | 4 | Confirm execution and go-live dates |
| Appendix D S5 | 5, Appendix A | Complete |
| Fees | Portal fee fields only | Commercial decision pending, see Section 6 |
| Addendum 1 acknowledgement | Portal | Check |
| WorkSafeBC, business licence, insurance | Not stated in draft | Asked in questions file; do not invent |
| Word or page limits | Unknown | `[ATHIF TO CONFIRM]` |

---

## Appendix A. Resumes

### Athif Shaffy, Founder & CEO (Greater Sudbury, Ontario)

Engagement lead. Seven-plus years in software and technology delivery. Founded The Alpha Nova in September 2020 and leads company strategy, client partnerships and product vision. Maestro Digital Mine, November 2022 to February 2025 `[ATHIF TO CONFIRM: role title]`, in a mining technology environment where field devices, telemetry and intermittent connectivity are daily realities. Instructor, Cambrian College `[ATHIF TO CONFIRM: programme and dates]`. BSc, First Class Honours, Staffordshire University `[ATHIF TO CONFIRM: programme]`. Google Developer Group Sudbury `[ATHIF TO CONFIRM: role]`. First place, Côté Gold Blast Captain AI Challenge (29 teams); first place, Comms-Denied Autonomy challenge, York, 2026.

### Ertugrul Sahin, Senior Software Developer

Solution architect. Leads complex feature development and system architecture at The Alpha Nova (March 2026 to present). Research and Development, Cambrian College, March 2023 to March 2026. Computer Engineering, Beykent University. Hands-on Microsoft 365, SharePoint and Exchange integration, which informs the identity federation and enterprise connector design. First place, Côté Gold Blast Captain AI Challenge.

### Laxman KC, Software Developer

Mobile and connector developer. Software Developer at The Alpha Nova since January 2024; Research and Development at Cambrian College since December 2024. Computer vision and telemetry pipelines, applied here to photo intake, geotagging and automated triage of resident reports, and to offline sync of field data. Multiple hackathon awards in 2026.

### Deepshika Ghale, UI Consultant (Greater Sudbury, Ontario)

UX and accessibility lead. Product designer and UX strategist advising The Alpha Nova since March 2025; Figma and prototyping; AODA and WCAG practice. First place, Cursor hackathon, Sudbury, 2026. Owns resident and staff flows and WCAG 2.1 AA testing.

### Shubham Dhamane, Business Analyst (Greater Sudbury, Ontario)

Business analyst. Translates client goals into requirements and measurable value at The Alpha Nova. Owns the service catalogue, routing rules, acceptance criteria and migration mapping. `[ATHIF TO CONFIRM: start date and prior experience]`

### Cheick Ismael Maiga, P.Eng., Technical Advisor

Professional Engineer advising across The Alpha Nova's engineering projects. Reviews architecture at the Phase 1 and Phase 3 gates. `[ATHIF TO CONFIRM: jurisdiction and discipline]`

### Advisors (disclosed, not assigned)

Dr. Markus Lehmann, Strategic Advisor; also a website testimonial for comAlpine Information System GmbH. Prof. Dr. Steffen Moritz, Lead Scientific Advisor; also COGITO client and listed reference.

---

## INTERNAL. Athif checklist (strip before bid)

- [ ] Questions posted through abbotsford.bidsandtenders.ca before Tue 8 Sep 2026 14:00 PDT (see `ABBOTSFORD-QUESTIONS-TO-SEND.md`); no email to Megan Clarke
- [ ] Budget answer received and the Section 6 decision made: bid on productized reading, or no-bid
- [ ] Appendix D S1 to S5 headings and limits confirmed; sections trimmed to fit
- [ ] Addendum 1 and any later addenda acknowledged in the portal
- [ ] "What exists today" in the civic layer confirmed so Section 3.2 is exactly true
- [ ] Canadian hosting provider and region named in 3.4
- [ ] Support targets in 4.3 set to what the fee actually funds
- [ ] Fees entered only in portal fee fields; technical file searched for "$"
- [ ] WorkSafeBC, business licence, insurance: only stated if required and held; otherwise per the City's answer
- [ ] Reference contacts warned
- [ ] Section 6, Section 7, this checklist and every `[ATHIF TO CONFIRM]` removed from the submission copy
- [ ] No em dashes; run a search
- [ ] Athif said yes
- [ ] Submit day is not close day (target Fri 18 Sep 2026)

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.
