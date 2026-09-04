**INTERNAL DRAFT. NOT FOR SUBMISSION. THE ALPHA NOVA.**

This is a response to a Request for Information, not a bid. No price is offered anywhere in this document. Do not email the buyer. Do not upload to saskatoon.bidsandtenders.ca until Athif says yes. Strip every block marked INTERNAL before any submission.

---

TAN · THE ALPHA NOVA INC.
AI. Software. IoT. One Technology Partner.

DRAFT DATE: 2026-09-04
STATUS: Internal draft, RFI response, fit MAYBE, official RFI document not yet reconciled

**EMAIL TO SHAREPOINT CONNECTOR**
**Capturing Outlook email as records in SharePoint with metadata and retention**
**RFI 26-0470**

SUBMITTED TO:
City of Saskatoon
Attention: Jill Schneider `[ATHIF TO CONFIRM FROM OFFICIAL DOCUMENT: title and department]`
Via saskatoon.bidsandtenders.ca
Closing: Friday 18 September 2026, 14:00 CST (Saskatchewan does not observe daylight time)

SUBMITTED BY:
The Alpha Nova Inc.
1545 Maley Drive, Greater Sudbury ON P3A 4R7
info@thealphanova.com · +1 437 424 5384
Contact: Athif Shaffy, Founder & CEO

Information on how a Microsoft 365 organisation can move email from Outlook into SharePoint as governed records, with metadata and retention applied at the point of capture, using native capability first and a targeted add-in only where native falls short.

www.thealphanova.com

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.

---

## Table of Contents

Re-order to the RFI's numbered questions once the official document is read. `[ATHIF TO CONFIRM FROM OFFICIAL DOCUMENT: response format, question list, page limit]`

1. Understanding of the City's Need
2. About The Alpha Nova and Relevant Experience
3. Solution Approaches: Native-First, Then Add-In
4. Implementation, Governance and Risk Considerations
5. Commercial Models (placeholders only, no price)
6. Suggestions for a Future Solicitation
7. Team

Appendix A. Resumes
Appendix B. Response-to-RFI question map (internal working table)
INTERNAL. Athif checklist (strip before submission)

---

## 1. Understanding of the City's Need

The City of Saskatoon is asking the market how email that lives in Outlook mailboxes can be captured into SharePoint as records, with the right metadata applied and the right retention enforced, in a way staff will actually use. `[ATHIF TO CONFIRM FROM OFFICIAL DOCUMENT: the City's stated objectives, current environment, and the specific questions asked]`

We read the need as four linked problems, and we would answer each differently.

**Capture.** Staff must be able to file an email, with attachments, from Outlook into the correct SharePoint location in one or two actions. If it takes six, it does not happen and the record stays in a mailbox where it is outside the records programme.

**Metadata.** A filed email must carry the properties the records programme needs: sender, recipients, sent date, subject, the business classification, and often a file or case number. Some of these can be read from the message automatically. Some must be chosen by the person filing. The design question is how few choices a person must make and how many can be inferred or defaulted.

**Retention.** Once filed, the record must fall under the retention schedule the City has adopted, be protected from casual deletion, and be disposed of, or transferred, on time and with an audit trail. Saskatchewan's local authority access and privacy legislation and the City's own bylaws set the obligations; the technology must make compliance the default path.

**Adoption and governance.** The best connector fails if it is optional and slow. The City will want to know how other organisations drive adoption, how duplicates and mis-filings are handled, how the solution survives Microsoft's own feature changes, and what it costs to own.

Everything below is offered as information. Nothing in this response is a bid, an offer or a commitment to price.

---

## 2. About The Alpha Nova and Relevant Experience

### 2.1 Who we are

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive in Greater Sudbury, Ontario. We build intelligent software and industrial systems across four capabilities: AI and Intelligent Systems; Industrial IoT and Edge; Software Engineering; and Product Engineering. We are a small firm; the people named in Section 7 are the people who would do the work.

### 2.2 Relevance, stated plainly

Email-to-SharePoint records capture is adjacent to our Microsoft 365 work. It is not a named Alpha Nova product and we do not hold a packaged connector on a price list. What we bring is hands-on Microsoft 365, SharePoint and Exchange engineering through our senior developer, a software engineering practice used to building against Microsoft Graph and Office.js, a product discipline that measures adoption rather than feature count, and experience carrying sensitive personal data under strict privacy regimes through COGITO with the University Medical Center Hamburg-Eppendorf. We have no municipal records-management reference to cite and we do not invent one.

### 2.3 Public work the City may examine

- **COGITO (UKE Hamburg).** Privacy-sensitive health application; encryption, audit and data-minimisation discipline that transfers directly to records handling.
- **Cambrian College Alumni App.** Public-sector client, delivered to completion, with a client willing to speak to how we work.
- **Wheel It Transportation.** Small-operator software with accessibility as a requirement.

### 2.4 References

| Reference | Organisation | Contact | Relationship |
| --- | --- | --- | --- |
| Prof. Dr. Steffen Moritz | University Medical Center Hamburg-Eppendorf (UKE) | moritz@uke.de · +49 40 7410 56565 | COGITO client; also Lead Scientific Advisor to The Alpha Nova (dual role disclosed) |
| Karen Hastie | One Chamber System | karen@onechambersystem.com · +1 705 669 7343 | Client, Chamber Perks |
| Shaunna Babyak | Wheel It Transportation | info@wheelittransportation.com · +1 705 929 8006 | Client |

Disclosure: Dr. Markus Lehmann is a Strategic Advisor to The Alpha Nova. He is not offered as a client reference.

---

## 3. Solution Approaches: Native-First, Then Add-In

Our position is that the City should exhaust what its existing Microsoft 365 licensing already provides before paying anyone to build or license a connector, and should add custom capability only at the specific points where native behaviour falls short of the records programme. The order below reflects that.

### 3.1 Tier 1. Native Microsoft 365 capability

**Filing.** Outlook (new Outlook and Outlook on the web, and classic Outlook with the SharePoint site synced through OneDrive) allows a message to be dragged or saved to a SharePoint document library, which stores it as an .msg or .eml with attachments embedded. Microsoft 365 groups and Teams-connected sites give each team a library that Outlook can reach.

**Metadata.** SharePoint content types and library columns hold classification, file number and business metadata. Column defaults per folder, and required columns, reduce the choices a person must make. Email properties (from, to, sent date, subject) are promoted automatically by SharePoint for .msg files into the standard email columns when the library uses the email content type.

**Retention.** Microsoft Purview retention labels and label policies apply retention and disposition to items in SharePoint. Labels can be auto-applied by location, by content type, by sensitive information type, or by trainable classifier, and can be set as default per library or folder. Record and regulatory-record labels lock content and drive a disposition review with an audit trail. Retention can also be applied to the mailbox itself, so mail that is never filed still falls under a schedule.

**Where Tier 1 falls short.** Filing is multi-step and inconsistent across Outlook clients. Users choose the destination every time. Classification depends on where the item lands rather than on a deliberate choice. Duplicates are common when several recipients file the same thread. Case or file numbers cannot be validated against a source of truth at filing time. Reporting on what was filed by whom is possible but not friendly. For many organisations these gaps are acceptable with training and governance; for a records programme with legal exposure they usually are not.

### 3.2 Tier 2. Low-code automation on the native platform

Power Automate flows triggered from Outlook (a button in the message, a flagged category, or a shared mailbox rule) can save the message and attachments to a chosen library, set metadata from message properties and a short adaptive card the user completes, and let Purview labels do the rest. Shared mailboxes for intake functions (permits, complaints, procurement) can be filed automatically with no user action at all. This tier closes the "too many steps" gap for common cases at licensing cost the City likely already carries, and it is where we would start any pilot. Limits: per-user flow licensing and throughput, weaker validation, and flows that break silently when a library or column changes unless monitored.

### 3.3 Tier 3. A targeted Outlook add-in and Graph service

Where the City needs deliberate classification, validated file numbers, duplicate suppression and consistent behaviour across every Outlook client, an Outlook add-in built on Office.js, backed by a small service using Microsoft Graph, is the appropriate step. The add-in adds a "File to records" action in the message surface on desktop, web and mobile. It reads the message, proposes a destination and classification from rules and from the user's recent filings, validates any case or file number against the City's source of truth, checks for a duplicate already filed from the same conversation, writes the message and attachments to SharePoint through Graph with the metadata set in a single call, and applies or confirms the Purview label. Every filing is logged for records staff. Optional: a machine-learning suggestion model trained on the City's own past filings that proposes the classification, always with the person confirming.

Hosting for the service would be in a Canadian Azure region within the City's own tenant or subscription so that no email content or personal information leaves the City's control. The add-in is centrally deployed through the Microsoft 365 admin centre, so nothing is installed on devices.

**Where Tier 3 falls short.** It is custom software the City must own or contract to maintain, Microsoft changes the Outlook add-in surface periodically, and it is only as good as the classification rules and the retention schedule behind it.

### 3.4 Tier 4. Commercial connectors

Several vendors sell packaged Outlook-to-SharePoint or Outlook-to-records connectors. We do not resell any of them and name none here. The City should include them in a future solicitation and compare them on the same criteria as Tiers 2 and 3: filing effort, metadata quality, retention integration, Canadian data handling, total cost over five years, and exit.

### 3.5 Recommended sequence

Configure Tier 1 properly and measure; automate the high-volume intake paths in Tier 2; build Tier 3 only for the classification and validation gaps that measurement proves; benchmark Tier 4 before committing to Tier 3.

---

## 4. Implementation, Governance and Risk Considerations

- **Retention schedule first.** No connector can apply a schedule that does not exist in Purview. The records programme's schedule must be modelled as labels and policies before any filing tool is rolled out.
- **Information architecture.** Site and library structure, content types and columns must be designed for filing, not only for browsing. Too many destinations is the most common reason filing stops.
- **Privacy.** Email contains personal information about residents and staff. Saskatchewan's local authority access and privacy obligations, the City's policies, and Canadian data residency should be confirmed as requirements; Microsoft 365 Canada data-centre regions and a City-controlled Azure subscription for any custom service keep content in Canada.
- **Adoption.** Measure filing volume per department monthly; publish it; pair the tool with a short, mandatory records orientation. Design for the person who files fifty emails a day, not the one who files one.
- **Duplicates and mis-filing.** Conversation-ID based duplicate detection and a records-staff review queue for corrections.
- **Change resilience.** Pin to supported Graph and Office.js versions; monitor Microsoft 365 roadmap changes; automated regression tests against a test tenant.
- **Exit.** Everything filed is ordinary SharePoint content with ordinary metadata and labels. If the City removes the add-in, the records remain intact.

---

## 5. Commercial Models (placeholders only, no price)

The City asked for information, so this section describes how such work is typically structured. No figures are offered and none should be inferred. Indicative rates can be provided in a subsequent RFP if the City asks for them.

| Model | Shape | When it fits |
| --- | --- | --- |
| Configuration and enablement engagement | Fixed-scope, fixed-fee assessment, Purview and SharePoint configuration, pilot with two or three departments, adoption measurement | Tiers 1 and 2; fastest time to value |
| Custom add-in build | Fixed-fee design and build against an agreed specification, with acceptance testing in the City's tenant | Tier 3 after measurement proves the gap |
| Support and evolution | Annual support arrangement covering Microsoft platform changes, rule updates, minor enhancements | After any Tier 3 deployment |
| Time and materials at published rates | Hourly or daily rates by role, for discovery or for work the City prefers to direct itself | Early discovery, or when scope is genuinely open |

`[PLACEHOLDER: no dollar values in an RFI response. Do not add rates here unless the official document explicitly requests indicative pricing.]`

---

## 6. Suggestions for a Future Solicitation

Offered to help the City write an RFP that gets comparable answers.

1. Publish the current Microsoft 365 licensing level (E3, E5, add-ons) so proponents can tell the City what is already paid for.
2. State the retention schedule's maturity: adopted and modelled in Purview, adopted on paper, or in development.
3. Describe the Outlook client mix (classic desktop, new Outlook, web, mobile) and the share of staff on each.
4. Give email volumes and the number of departments, sites and shared mailboxes in scope.
5. Ask every proponent to demonstrate filing a message from each Outlook client in the City's test tenant, and score effort in clicks and seconds.
6. Score Canadian data residency, exit, and five-year total cost of ownership alongside features.
7. Separate the price envelope from the technical response.
8. Allow a paid pilot with two departments before a full commitment.

---

## 7. Team

Roles are those held at The Alpha Nova, as shown on our public About page.

| Name | Role if engaged | Title at The Alpha Nova |
| --- | --- | --- |
| Athif Shaffy | Engagement lead | Founder & CEO |
| Ertugrul Sahin | Solution architect; Microsoft 365, SharePoint, Exchange, Graph and Office.js design | Senior Software Developer |
| Shubham Dhamane | Business analyst; retention schedule modelling, information architecture, adoption measurement | Business Analyst |
| Deepshika Ghale | UX of the filing action; accessibility of the add-in | UI Consultant |
| Laxman KC | Developer; classification suggestion model if pursued | Software Developer |
| Cheick Ismael Maiga, P.Eng. | Technical advisor and advisory review | Technical Advisor |

Advisors disclosed and not assigned: Dr. Markus Lehmann (Strategic Advisor; not a client reference) and Prof. Dr. Steffen Moritz (Lead Scientific Advisor; also COGITO client and listed reference).

---

## Appendix A. Resumes

### Athif Shaffy, Founder & CEO (Greater Sudbury, Ontario)

Seven-plus years in software and technology delivery. Founded The Alpha Nova in September 2020 and leads strategy, client partnerships and product vision. Maestro Digital Mine, November 2022 to February 2025 `[ATHIF TO CONFIRM: role title]`. Instructor, Cambrian College `[ATHIF TO CONFIRM: programme and dates]`. BSc, First Class Honours, Staffordshire University `[ATHIF TO CONFIRM: programme]`. Google Developer Group Sudbury `[ATHIF TO CONFIRM: role]`. First place, Côté Gold Blast Captain AI Challenge (29 teams); first place, Comms-Denied Autonomy challenge, York, 2026.

### Ertugrul Sahin, Senior Software Developer

Leads complex feature development and system architecture at The Alpha Nova (March 2026 to present). Research and Development, Cambrian College, March 2023 to March 2026. Computer Engineering, Beykent University. Hands-on Microsoft 365, SharePoint and Exchange engineering; the lead for any Graph, Purview or Office.js work described in Section 3. First place, Côté Gold Blast Captain AI Challenge.

### Shubham Dhamane, Business Analyst (Greater Sudbury, Ontario)

Translates business goals into requirements and measurable value at The Alpha Nova. Would own retention-schedule modelling, information architecture and adoption metrics. `[ATHIF TO CONFIRM: start date and prior experience]`

### Deepshika Ghale, UI Consultant (Greater Sudbury, Ontario)

UI Consultant advising The Alpha Nova since March 2025 on interface and user experience; Figma and prototyping; AODA and WCAG practice. First place, Cursor hackathon, Sudbury, 2026. Would design the filing action so it takes as few decisions as possible and remains accessible.

### Laxman KC, Software Developer

Software Developer at The Alpha Nova since January 2024; Research and Development at Cambrian College since December 2024. Computer vision and telemetry; would build the optional classification suggestion model. Multiple hackathon awards in 2026.

### Cheick Ismael Maiga, P.Eng., Technical Advisor

Professional Engineer advising across The Alpha Nova's engineering projects; advisory review. He is The Alpha Nova's Technical Advisor, not an independent third-party reviewer. `[ATHIF TO CONFIRM: jurisdiction and discipline]`

### Advisors (disclosed, not assigned)

Dr. Markus Lehmann, Strategic Advisor; not presented as a client reference. Prof. Dr. Steffen Moritz, Lead Scientific Advisor; also COGITO client and listed reference.

---

## Appendix B. Response-to-RFI question map (internal working table)

Populate once the official RFI document is read. Map each numbered City question to the section that answers it and trim anything the City did not ask for.

| RFI question (official) | Section | Gap |
| --- | --- | --- |
| `[ATHIF TO CONFIRM]` | | |

---

## INTERNAL. Athif checklist (strip before submission)

- [ ] Official RFI document downloaded from saskatoon.bidsandtenders.ca; Jill Schneider's title and the response format confirmed
- [ ] Sections re-ordered to the City's numbered questions; Appendix B filled
- [ ] Confirmed there is no price, rate or dollar figure anywhere in the document
- [ ] Confirmed wording says "adjacent" and never implies a packaged Alpha Nova connector product
- [ ] Reference contacts warned
- [ ] Every INTERNAL block, `[ATHIF TO CONFIRM]` and `[PLACEHOLDER]` removed from the submission copy
- [ ] No em dashes; run a search
- [ ] Athif said yes
- [ ] Submit day is not close day (target Thu 17 Sep 2026; close is Fri 18 Sep 14:00 CST)

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.
