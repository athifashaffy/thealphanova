**INTERNAL DRAFT. NOT FOR SUBMISSION. THE ALPHA NOVA.**

Do not email the buyer. Do not upload to lethbridge.bidsandtenders.ca. Official PDF still required; every `[ATHIF TO CONFIRM FROM OFFICIAL PDF]` must be resolved before the posture in Section 3 is chosen. Price appears only in Section 6 (rates only) and only where the RFP's price form puts it. Strip every block marked INTERNAL before any submission.

---

TAN · THE ALPHA NOVA INC.
AI. Software. IoT. One Technology Partner.

DRAFT DATE: 2026-09-04
STATUS: Internal draft, fit MAYBE, posture not yet chosen (Section 3), official PDF not yet reconciled

**CCTV SEWER AND STORM INSPECTION SOFTWARE**
**Inspection data, condition coding and asset intelligence for the City's wastewater and stormwater networks**
**RFP COL-25-173**

SUBMITTED TO:
City of Lethbridge
`[ATHIF TO CONFIRM FROM OFFICIAL PDF: department, named contact]`
Procurement via lethbridge.bidsandtenders.ca
Closing: Wednesday 23 September 2026, 14:00 MDT `[ATHIF TO CONFIRM FROM OFFICIAL PDF]`

SUBMITTED BY:
The Alpha Nova Inc.
1545 Maley Drive, Greater Sudbury ON P3A 4R7
info@thealphanova.com · +1 437 424 5384
Signing authority: Athif Shaffy, Founder & CEO

Software that turns the City's CCTV inspection footage and PACP-coded observations into a searchable, GIS-linked condition record the utility can plan and budget from, delivered as either a configured proven inspection platform or an integration and vision layer over the coding software the City chooses.

www.thealphanova.com

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.

---

## Table of Contents

The earlier compliance pass noted this RFP scores Experience, Software, Demonstration and Price. Sections 2 to 4 are written to those headings; Section 1 gives the evaluators our reading of the need and Section 5 the team. Re-order once the official PDF confirms the rated criteria. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: criteria, weights, page limit, demonstration format and date]`

1. Understanding of the Requirement
2. Experience
3. Software: two postures
4. Demonstration and Implementation Plan
5. Team
6. Price posture (INTERNAL, rates only)
7. Compliance Matrix (internal working table)

Appendix A. Resumes
INTERNAL. Athif checklist (strip before bid)

---

## 1. Understanding of the Requirement

### 1.1 What the City is buying

The City of Lethbridge is buying software for closed-circuit television inspection of its sanitary sewer and storm drainage networks: the software that inspection crews and engineers use to record what a crawler camera sees, code defects and features to a recognised standard, store the video and the observations against the right pipe segment and manhole, and turn thousands of individual inspections into a condition picture the utility can prioritise, budget and report from. `[ATHIF TO CONFIRM FROM OFFICIAL PDF: whether the City inspects with its own crews, contractors or both; whether field capture software is in scope or only office and analytics; asset and inspection volumes; existing GIS and work management systems]`

We read the requirement in three layers: field capture (in the truck, on the camera controller's laptop, coding as the crawler moves); office management (import, QA, storage, search, reporting, exchange with contractors); and asset intelligence (condition scoring, deterioration trends, risk-based renewal planning, links to GIS and to work orders). Different vendors are strong in different layers. The City should know which layers this proposal addresses under each posture, and Section 3 says so.

### 1.2 What The Alpha Nova is and is not

We are a Canadian software company. We are not a camera, crawler or inspection-truck manufacturer and we do not supply hardware. We are not a PACP-certified coding house. We are not proposing to replace the City's inspection crews or contractors. What we bring is software engineering, computer vision and telemetry experience, and integration discipline with GIS and enterprise systems. Section 2 states our relevant work and our gaps in the same paragraph so the evaluators do not have to hunt for them.

### 1.3 What matters most

**The standard.** NASSCO's PACP, MACP and LACP are the coding languages of North American sewer inspection, and the PACP exchange database is how inspections move between contractors, software and owners. Whatever the City buys must read and write PACP-conformant data or the City is locked in on day one.

**The asset link.** An inspection that cannot be tied to the correct pipe segment, manhole and lateral in the City's GIS is a video file, not an asset record. Bidirectional linkage to the City's GIS and, ideally, to its work management system, is where the value lives.

**Storage and retrieval.** Inspection video is large and lives for decades. Where it is stored, at what cost, how quickly an engineer can jump from a defect code to the exact frame, and how the City exits the platform later are commercial and technical questions with long tails.

**Contractor exchange.** If the City uses inspection contractors, their deliverables must import cleanly with QA checks, and the City's requirements to them must be enforceable in software.

**Making sense of it all.** Condition grades, risk scoring, deterioration modelling and renewal prioritisation are where inspection budgets pay back. This is also where computer vision now adds real value: pre-screening footage for likely defects so a certified operator reviews frames rather than hours.

---

## 2. Experience

### 2.1 About The Alpha Nova

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. We build intelligent software and industrial systems across four capabilities: AI and Intelligent Systems; Industrial IoT and Edge; Software Engineering; and Product Engineering. Sudbury is a mining and underground-infrastructure city; our engineering culture comes from environments where cameras, sensors and telemetry have to work in the dark, in the wet and without a reliable link.

### 2.2 Relevant experience, stated with its limits

- **Computer vision on industrial video.** Our team won first place of 29 teams in the Côté Gold Blast Captain AI Challenge (IAMGOLD, Laurentian University, Cambrian College, GDG Sudbury), building a computer-vision pipeline that analysed drone footage of open-pit blasts and extracted fragmentation metrics. That is the same class of problem as pre-screening sewer footage for defects: noisy video, domain-specific features, expert validation of model output. It is not sewer footage and we do not claim it is.
- **Telemetry and edge.** Our Industrial IoT and Edge practice, and our developer Laxman KC's computer-vision and telemetry work, cover store-and-forward capture from field devices with intermittent connectivity, which is the inspection truck's situation.
- **Sensitive data and offline operation.** COGITO (UKE Hamburg) runs offline, syncs when it can, and operates under strict privacy controls. Inspection data is less sensitive but the offline-first and audit disciplines are the same.
- **Integration engineering.** Our senior developer leads architecture and has hands-on enterprise integration experience (Microsoft 365, SharePoint, Exchange). GIS and work-management integration for this RFP would be new specific systems for us and we say so.
- **Our own products.** VanGuardian, an AI fall-detection product without wearables, shows that we build, own and maintain software over time rather than only deliver projects.

### 2.3 The gaps, in the buyer-facing text

We have no municipal sewer or storm CCTV software reference. We have not deployed inspection software for a Canadian utility. No member of the team holds NASSCO PACP, MACP or LACP certification; Laxman KC's computer-vision and telemetry experience is adjacent, not certified. We have not previously integrated with Esri-based municipal GIS or a municipal work-management system in production. Under Posture A (Section 3) these gaps are covered by the ISV's product maturity and our role is configuration and integration; under Posture B they are covered by leaving the coding to the City's certified operators and contractors, and building the layer that consumes their output.

### 2.4 Public work the City may examine

Côté Gold Blast Captain AI Challenge; COGITO (UKE Hamburg); VanGuardian; Cambrian College Alumni App; Wheel It Transportation. None is a municipal utility reference.

### 2.5 References

| Reference | Organisation | Contact | Relationship |
| --- | --- | --- | --- |
| Prof. Dr. Steffen Moritz | University Medical Center Hamburg-Eppendorf (UKE) | moritz@uke.de · +49 40 7410 56565 | COGITO client; also Lead Scientific Advisor to The Alpha Nova (dual role disclosed) |
| Karen Hastie | One Chamber System | karen@onechambersystem.com · +1 705 669 7343 | Client, Chamber Perks |
| Shaunna Babyak | Wheel It Transportation | info@wheelittransportation.com · +1 705 929 8006 | Client |

Disclosure: Dr. Markus Lehmann is a Strategic Advisor to The Alpha Nova. He is not offered as a client reference.

---

## 3. Software: two postures

INTERNAL: one posture must be chosen before submission. Do not submit both. The choice depends on the official PDF (is the City buying a coding platform, an analytics layer, or both), on whether an ISV partnership can be confirmed in time, and on the demonstration format. No ISV is named as committed anywhere in this draft.

### Posture A. Configure and integrate a proven inspection ISV platform

**What the City gets.** A mature, commercially supported CCTV inspection platform from an established independent software vendor that already provides PACP, MACP and LACP coding, field capture on the camera controller, office import and QA, video storage and contractor exchange. The Alpha Nova acts as the Canadian implementation and integration partner: requirements confirmation, configuration to the City's asset hierarchy and coding rules, GIS linkage, work-management linkage, data migration from the current system, training and first-line support, with the ISV providing the product, its updates and second-line support.

**Why this posture.** It gives the City product maturity in the coding and field layers where we have no track record, and puts our effort where it adds value: integration, migration and adoption.

**Conditions.** A signed partner or reseller arrangement with a suitable ISV before submission `[ATHIF TO CONFIRM: which ISVs will partner with a new Canadian integrator, on what terms, in what timeframe]`; ISV licence pricing obtained in writing; the ISV's Canadian hosting or on-premises options confirmed against the City's data requirements. If no arrangement can be confirmed before the closing date, Posture A is not available and Posture B or a no-bid follows.

**Scope under Posture A.** Field capture, office management and base analytics from the ISV; The Alpha Nova delivers GIS and work-management integration, migration, training, first-line support and, optionally, the vision pre-screening module described in Posture B as an add-on.

### Posture B. Integration and vision layer over the City's chosen coding software

**What the City gets.** The City keeps or separately procures PACP-conformant coding software for its crews and contractors. The Alpha Nova delivers the layer above it: a central inspection data hub that imports PACP exchange databases and video from any conformant source, validates them against the City's QA rules, links every inspection to the correct GIS asset, stores video in City-controlled Canadian cloud or on-premises storage with frame-level indexing, exposes search and reporting across the whole history, computes condition and risk scores on the City's methodology, integrates with the work-management system to raise follow-up work, and applies computer-vision pre-screening that flags likely defects for a certified operator's review. The layer is vendor-neutral by design: it consumes the standard, not any one product's database.

**Why this posture.** It matches what we are actually good at, avoids any claim to be a coding house, and protects the City from lock-in because its data lives in the PACP standard and in its own GIS.

**Scope under Posture B.** Hub, GIS integration, work-management integration, storage, search, reporting, scoring, vision pre-screening, contractor QA portal. Explicitly out of scope: field capture software, camera and crawler hardware, coding certification, and the coding itself.

**Honesty clause.** The vision pre-screening module is an assistive tool. Model output is never a coded observation; a certified operator confirms or rejects every flag, and the system records both so the City can measure the model's usefulness on its own footage over time.

### 3.1 Requirements addressed under either posture

`[ATHIF TO CONFIRM FROM OFFICIAL PDF: requirement list; map each into this table]`

| Requirement area | Posture A | Posture B |
| --- | --- | --- |
| PACP / MACP / LACP coding | ISV product | City's chosen coding software; hub validates and imports |
| Field capture | ISV product | Out of scope |
| PACP exchange import and export | ISV product | Hub, any conformant source |
| Video storage and frame-level retrieval | ISV product; Canadian hosting to confirm | Hub, City-controlled Canadian storage |
| GIS linkage | Alpha Nova integration | Hub integration |
| Work-management linkage | Alpha Nova integration | Hub integration |
| Contractor deliverable QA | ISV plus Alpha Nova rules | Hub QA portal |
| Condition and risk scoring | ISV plus configuration | Hub, City methodology |
| Vision pre-screening | Optional add-on | Included |
| Reporting and dashboards | ISV plus Alpha Nova | Hub |
| Data ownership and exit | Per ISV terms, to confirm | City owns everything; standard formats |

### 3.2 Non-functional commitments

Canadian data residency for inspection data and video `[ATHIF TO CONFIRM: provider and region]`; role-based access with City identity provider; audit trail on every import, edit and score change; offline-tolerant imports; documented APIs; WCAG 2.1 AA for the web interface; documented exit including bulk export in PACP and open formats.

---

## 4. Demonstration and Implementation Plan

### 4.1 Demonstration

`[ATHIF TO CONFIRM FROM OFFICIAL PDF: whether a demonstration is scored, its format, duration and date]`

Under Posture A the ISV demonstrates its product with The Alpha Nova presenting the integration and adoption plan. Under Posture B we demonstrate the hub using a sample PACP exchange database and sample inspection video `[ATHIF TO CONFIRM: source of a licensable sample data set; if none is available, synthetic data is used and labelled as such]`, showing import and QA, GIS linkage on a demonstration map, frame-level retrieval from a defect code, scoring, a work-order hand-off to a demonstration endpoint, and the vision pre-screening flagging frames for operator review. Everything shown will be what exists at demonstration time; we will not show mock-ups as working software.

### 4.2 Implementation phases

| Phase | Weeks | Posture A | Posture B |
| --- | --- | --- | --- |
| 0 Mobilise | 1 to 2 | Requirements confirmation; ISV environment; GIS and work-management access | Requirements confirmation; storage and GIS access; sample data from the City |
| 1 Configure / build core | 3 to 10 | Configure ISV to City asset hierarchy and coding rules; migration mapping | Hub import, QA, storage, GIS linkage |
| 2 Integrate | 8 to 14 | GIS and work-management connectors | Work-management connector; scoring; reporting |
| 3 Migrate and pilot | 12 to 18 | Historic inspection migration; pilot with one crew or contractor | Historic import; pilot; vision pre-screening calibrated on City footage |
| 4 Train and go live | 18 to 20 | Crew, office and engineering training; go-live | Office and engineering training; go-live |
| 5 Support | Term | First-line by Alpha Nova, second-line by ISV | Alpha Nova |

`[ATHIF TO CONFIRM FROM OFFICIAL PDF: required go-live, contract term, support expectations]`

### 4.3 City responsibilities

Project lead; GIS administrator access and asset data; work-management system access; historic inspection data and video; coding rules and QA thresholds; certified operators for validation; identity provider configuration.

### 4.4 Risks

| Risk | Handling |
| --- | --- |
| No ISV partnership confirmed in time | Posture B or no-bid; decided before submission |
| Asset IDs in historic inspections do not match GIS | Migration mapping phase with exception queue for engineering decision |
| Video volumes exceed storage assumptions | Storage sized from City's actual volumes in Phase 0; tiered storage |
| Vision model under-performs on City footage | Positioned as assistive only; usefulness measured; never a coded observation |
| Integration to systems we have not used before | Sandbox-first, City administrators engaged from Phase 0, P.Eng. review at gates |

---

## 5. Team

| Name | Role on this engagement | Title at The Alpha Nova | Commitment |
| --- | --- | --- | --- |
| Athif Shaffy | Engagement lead; ISV relationship under Posture A; commercial and escalation contact | Founder & CEO | Throughout |
| Ertugrul Sahin | Solution architect; hub design; GIS and work-management integration | Senior Software Developer | Phases 0 to 4 |
| Laxman KC | Computer-vision and telemetry developer; video pipeline; pre-screening model; import tooling | Software Developer | Phases 1 to 4 |
| Shubham Dhamane | Business analyst; requirements traceability; coding rules and QA thresholds; migration mapping | Business Analyst | Phases 0 to 3 |
| Deepshika Ghale | UX of the engineering and contractor interfaces; WCAG 2.1 AA | UI Consultant | Phases 1 to 3 |
| Cheick Ismael Maiga, P.Eng. | Technical advisor; engineering review of scoring methodology and integration design | Technical Advisor | Gate reviews |

Advisors disclosed and not assigned: Dr. Markus Lehmann (Strategic Advisor; not a client reference) and Prof. Dr. Steffen Moritz (Lead Scientific Advisor; also COGITO client and listed reference).

---

## 6. Price posture (INTERNAL, rates only)

Never place this in the technical sections. Price goes only on the RFP's price form once the posture is chosen and the ISV licence, if any, is known in writing.

Published rates, the only figures permitted in this draft:

| Role | Hourly | Daily |
| --- | --- | --- |
| Software engineering (architecture, development, integration) | $80 | $640 |
| Design (UX, accessibility) | $75 | $600 |
| Quality assurance | $50 | $400 |

Posture A price = ISV licence and hosting pass-through `[ATHIF TO CONFIRM: written ISV quote]` plus Alpha Nova services at the rates above for the effort in Section 4.2 plus support at an annual figure derived from the rates `[Athif to build]`.

Posture B price = Alpha Nova services at the rates above for the effort in Section 4.2, plus City-controlled storage at cost, plus annual support derived from the rates `[Athif to build]`.

Do not enter a total in this file. Build the total in the pricing spreadsheet on the PC once the official price form is known, and check whether the City wants a fixed price, a rate card, licence and support split, or all three.

---

## 7. Compliance Matrix (internal working table)

| RFP requirement (from official PDF) | Draft section | Status / gap |
| --- | --- | --- |
| Experience | 2 | Honest gaps stated: no municipal sewer-CCTV reference; no PACP certification |
| Software | 3 | Posture to be chosen; requirement list to be mapped in 3.1 |
| Demonstration | 4.1 | Format and sample data to confirm |
| Price | 6, price form only | Rates only until posture and ISV quote known |
| Mandatory forms, insurance, WCB Alberta | INTERNAL checklist | Do not invent |
| Addenda acknowledgement | Portal | Check |
| Page limit | Unknown | `[ATHIF TO CONFIRM]` |

---

## Appendix A. Resumes

### Athif Shaffy, Founder & CEO (Greater Sudbury, Ontario)

Engagement lead. Seven-plus years in software and technology delivery. Founded The Alpha Nova in September 2020 and leads strategy, client partnerships and product vision. Maestro Digital Mine, November 2022 to February 2025 `[ATHIF TO CONFIRM: role title]`, in a mining technology environment of underground sensors, telemetry and intermittent connectivity. Instructor, Cambrian College `[ATHIF TO CONFIRM: programme and dates]`. BSc, First Class Honours, Staffordshire University `[ATHIF TO CONFIRM: programme]`. Google Developer Group Sudbury `[ATHIF TO CONFIRM: role]`. First place, Côté Gold Blast Captain AI Challenge (29 teams, computer vision on industrial drone footage); first place, Comms-Denied Autonomy challenge, York, 2026.

### Ertugrul Sahin, Senior Software Developer

Solution architect. Leads complex feature development and system architecture at The Alpha Nova (March 2026 to present). Research and Development, Cambrian College, March 2023 to March 2026. Computer Engineering, Beykent University. Enterprise integration experience in Microsoft 365, SharePoint and Exchange; designs the hub, its APIs and its GIS and work-management connectors. First place, Côté Gold Blast Captain AI Challenge.

### Laxman KC, Software Developer

Computer-vision and telemetry developer. Software Developer at The Alpha Nova since January 2024; Research and Development at Cambrian College since December 2024. Works in computer vision and telemetry pipelines, which is adjacent to sewer inspection video analysis; not NASSCO PACP certified. Builds the video pipeline, import tooling and pre-screening model. Multiple hackathon awards in 2026.

### Shubham Dhamane, Business Analyst (Greater Sudbury, Ontario)

Business analyst. Translates client goals into requirements and measurable value at The Alpha Nova. Owns requirements traceability, coding-rule and QA-threshold capture, and migration mapping. `[ATHIF TO CONFIRM: start date and prior experience]`

### Deepshika Ghale, UI Consultant (Greater Sudbury, Ontario)

UX and accessibility. UI Consultant advising The Alpha Nova since March 2025 on interface and user experience; Figma and prototyping; AODA and WCAG practice. First place, Cursor hackathon, Sudbury, 2026. Designs the engineering, contractor and review interfaces to WCAG 2.1 AA.

### Cheick Ismael Maiga, P.Eng., Technical Advisor

Professional Engineer advising across The Alpha Nova's engineering projects; reviews the scoring methodology and integration design at gates. `[ATHIF TO CONFIRM: jurisdiction and discipline]`

### Advisors (disclosed, not assigned)

Dr. Markus Lehmann, Strategic Advisor; not presented as a client reference. Prof. Dr. Steffen Moritz, Lead Scientific Advisor; also COGITO client and listed reference.

---

## INTERNAL. Athif checklist (strip before bid)

- [ ] Official PDF downloaded from lethbridge.bidsandtenders.ca; scope layers (field, office, analytics), criteria, demonstration format, page limit and price form confirmed
- [ ] Posture chosen: A only if an ISV partnership and written licence quote exist before submission; otherwise B or no-bid
- [ ] The unchosen posture and every "two postures" reference removed from the submission copy
- [ ] No ISV named as committed unless a signed arrangement exists
- [ ] Requirement list from the PDF mapped into Section 3.1
- [ ] Sample PACP data and video for the demonstration sourced or synthetic data prepared and labelled
- [ ] Canadian storage provider and region named in 3.2
- [ ] Insurance, WCB Alberta, business licence: only stated if required and held
- [ ] Price built on the PC from published rates; entered only on the price form; technical file searched for "$"
- [ ] Addenda acknowledged in the portal
- [ ] Reference contacts warned
- [ ] Every INTERNAL block and `[ATHIF TO CONFIRM]` removed from the submission copy
- [ ] No em dashes; run a search
- [ ] Athif said yes
- [ ] Submit day is not close day (target Mon 21 or Tue 22 Sep 2026; close is Wed 23 Sep 14:00 MDT)

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.
