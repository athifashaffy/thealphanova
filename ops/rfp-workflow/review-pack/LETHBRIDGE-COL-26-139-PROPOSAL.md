**INTERNAL DRAFT. NOT FOR SUBMISSION. THE ALPHA NOVA.**

Do not email the buyer. Do not upload to lethbridge.bidsandtenders.ca. Nothing in this file has been cleared by Athif. Strip the internal pages before any real submission.

---

TAN · THE ALPHA NOVA INC.
Software Development and Innovation

DRAFT DATE: 2026-09-04

**ECONOMIC AND INVESTMENT
DATA PORTAL
RFQ COL-26-139**

SUBMITTED TO:
City of Lethbridge
Economic Development, City of Lethbridge
Procurement via https://lethbridge.bidsandtenders.ca
Named contact: Nicki Van Eck, nicki.vaneck@lethbridge.ca
All communication through the bidsandtenders portal only

Closing: Thursday 10 September 2026, 14:00 MDT
Addenda: Addendum 1 received and acknowledged
Questions period: closed 31 August 2026, no questions submitted

SUBMITTED BY:
The Alpha Nova Inc.
1545 Maley Drive, Greater Sudbury ON P3A 4R7
info@thealphanova.com · +1 437 424 5384

A configurable, public facing economic and investment data portal that publishes the City's indicators to anyone, 24 hours a day, with no login, and that City staff refresh, publish and retire themselves without a change request to us.

www.thealphanova.com

The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.

---

## Table of Contents

Ordered to the RFQ's rated criteria, with the unrated but mandatory material behind it.

1. Understanding of the Requirement
2. Experience and Qualifications (rated, 10 points)
3. The Software (rated, 50 points)
   - 3.1 What we are proposing, and what it is not
   - 3.2 Public portal, no login, 24/7
   - 3.3 Data ingest, refresh and provenance
   - 3.4 Staff administration and role based access control
   - 3.5 Visualization: charts, tables, maps, filters
   - 3.6 Export, reuse and embedding
   - 3.7 Branding and City visual identity
   - 3.8 Hosting, data residency and supplier origin
   - 3.9 Security and privacy
   - 3.10 Accessibility
   - 3.11 Performance, availability and monitoring
   - 3.12 Configuration versus custom development
4. Implementation Plan to 30 November 2026
5. Demonstration (rated, 10 points)
6. Support, Maintenance and Term
7. Price (rated, 30 points)
8. Project Team
9. References
10. Assumptions, Dependencies and Risks
11. Compliance Matrix
12. Appendix A: Resumes of Proposed Personnel

INTERNAL: Athif only. Strip before submission.

---

## 1. Understanding of the Requirement

The City of Lethbridge is buying a data publishing platform, not an analytics project and not a consulting study. The deliverable is a working public portal that presents the City's economic and investment indicators to residents, site selectors, realtors, developers, researchers, students and prospective employers, and that continues to be correct on a Tuesday morning eighteen months after we have gone quiet. Everything else in this response is subordinate to that.

Read plainly, the requirement has five parts.

First, the portal is public. It is available 24 hours a day, seven days a week, with no account, no login, no paywall and no registration gate in front of any published indicator. That single decision shapes the architecture: the public surface should be a cached, read only presentation layer with no user data in it, which is both faster and materially safer than a portal that has to authenticate the general public.

Second, the data arrives from more than one source and has to refresh on its own. A portal that depends on a staff member re-keying numbers from a spreadsheet every quarter will drift out of date, and the reputational cost of a stale investment figure quoted by a site selector is higher than the cost of the portal itself. The City needs scheduled, automated ingest from the sources it already relies on, with visible "as of" dates and an alert when a source stops answering.

Third, City staff own the content. Publishing an indicator, revising it, correcting it and retiring it are all normal staff actions performed in a browser through role based access control, with an audit trail. They are not tickets raised with the vendor. This is the difference between a portal the City operates and a portal the City rents access to.

Fourth, the presentation is not a single dashboard. The RFQ contemplates charts, tables, maps and filters, and export of what is on screen. Different audiences want different things from the same indicator. A site selector wants to compare Lethbridge against a peer community and take the number away in a spreadsheet. A councillor wants a five year trend line. A resident wants a map. The portal has to serve all of them from one governed dataset rather than from three separately maintained copies.

Fifth, the City wants a configurable product, not a bespoke build. Indicators change. Sources change. Definitions change. If each of those changes is a code deployment, the City has bought a maintenance liability. The correct answer is a platform where indicators, sources, refresh schedules, chart types, filters, map layers and page layouts are configuration held in data, editable by an administrator, and where our involvement after go-live is support and platform upgrades rather than content work.

### 1.1 The dates that govern everything

The RFQ closes Thursday 10 September 2026 at 14:00 MDT. Demonstrations, for the top three ranked proponents, are held 28 and 29 September 2026. Go-live is required no later than 30 November 2026. The initial term is four years, with two additional four year options at the City's discretion, so the City is choosing a platform it may live with for twelve years.

That combination is the central planning fact. There is a narrow window between demonstration and go-live, and the honest engineering conclusion is that the only way to hit 30 November 2026 is to configure a platform that already exists rather than to start building one in October. Section 4 sets out our plan against that window, including what we do if award slips.

### 1.2 What this engagement is not

We want to be direct about scope, because vague scope is how fixed date projects fail.

This is not a generative artificial intelligence proposal. We are not offering a chatbot on top of the City's indicators, we are not proposing to generate narrative commentary about economic performance, and we are not proposing machine learning forecasts of Lethbridge's economy. The City asked for a clean, trustworthy data portal. Adding a language model to a page whose entire value is that the number is correct would add risk, add cost, add a privacy review and add nothing the RFQ asked for. If the City later wants an interpretive layer, it should be a separate, separately evaluated decision.

This is not an enterprise data warehouse or business intelligence licensing programme. We are not proposing to become the City's analytics platform, to replace existing reporting tools, or to ingest operational systems beyond the sources needed to publish the indicator set.

This is not an economic development strategy engagement. We do not select the indicators. Economic Development does. Our job is to make the indicators the City chooses publishable, current, legible and exportable.

### 1.3 The gap we are not going to paper over

We have not shipped a municipal economic and investment open data portal for another Canadian city. If the City's evaluation requires a live reference portal of exactly this kind at another Alberta or Canadian municipality, we do not have one, and no amount of adjacent experience changes that. We would rather lose points at Section 2 than have the City discover it at reference check.

What we do have is the constituent parts, delivered for real clients and in production: multi audience data dashboards, scheduled ingest from external sources, published analytics that clinicians and administrators depend on, multi language and accessibility sensitive interfaces, and public facing platforms in Greater Sudbury and abroad. Section 2 describes those honestly, with named contacts who will answer the phone. Section 3 describes the software, and Section 5 offers the City a live demonstration, which is the fastest way for an evaluator to test whether our claim survives contact with reality.

### 1.4 Attachments 1 to 3

The RFQ refers to Attachments 1, 2 and 3, which we understand contain the City's indicator wishlist and related detail. As of this draft we have not been able to retrieve those attachments from lethbridge.bidsandtenders.ca. **[ATHIF TO CONFIRM: download Attachments 1 to 3 from the portal and reconcile Sections 3.3, 3.5 and 11 against the actual indicator list before submission.]**

We have deliberately not guessed at the indicator list. Nothing in this response invents an indicator, a source, a definition or a refresh frequency that the City has not published. Our commitment is stated at the level of capability: the platform ingests, governs and publishes the indicator set specified in Attachments 1 to 3, at the frequencies the City specifies, and any indicator the City adds later is a configuration change performed by City staff or by us under support, not a new project.

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 1

---

## 2. Experience and Qualifications

Rated criterion, 10 points.

### 2.1 About The Alpha Nova

The Alpha Nova Inc. is a Canadian technology company headquartered at 1545 Maley Drive, Greater Sudbury, Ontario P3A 4R7. We build intelligent software and industrial systems across four capabilities: artificial intelligence and intelligent systems, industrial Internet of Things and edge, software engineering, and product engineering. We are a technology company rather than a staffing agency: the people named in Section 8 are the people who do the work.

Everything we deliver for the City would be delivered from Canada by Canadian based personnel. We hold no offices outside Canada and make no claim to international delivery centres.

Registration, insurance, WSIB or WCB coverage and any bonding requirement in the RFQ are handled in the City's own forms. **[ATHIF TO CONFIRM: certificate of insurance limits, WCB Alberta clearance requirement for an Ontario based supplier performing remote software work, and extra provincial registration in Alberta if the City requires it.]** We have not asserted any of those in this technical response, and we will not.

### 2.2 Why we are a credible supplier for this portal, stated conservatively

Four things in our record map directly onto what COL-26-139 asks for.

**Published data that other people depend on being right.** COGITO, built with the University Medical Center Hamburg-Eppendorf, puts progress data in front of both patients and clinicians. The clinician view is a live analytics surface: aggregate progress across a caseload, per participant trends, and the ability to act on what is shown. **[ATHIF TO CONFIRM before submission: "deployed across multiple healthcare institutions" and "validated in peer reviewed publications". Do not leave either claim in the submitted file unless Athif can point to the institutions and the publications.]** The relevance here is not healthcare. It is that we have built a reporting surface in a domain where a wrong number is a serious problem, under European privacy rules, with data minimization designed in from the start.

**Multi language and accessibility sensitive interfaces.** COGITO is multilingual with full localization, including offline operation. **[ATHIF TO CONFIRM: use the same language count as CICIC (19) or keep a conservative wording. Do not mix "five or more" and "19" across bids.]** The Wheel It platform, built with Wheel It Transportation in Greater Sudbury, is accessibility oriented by its nature: the users are people whose mobility needs the service exists to meet. Both projects made us build interfaces where the layout, contrast, labelling and keyboard path are requirements rather than polish. That is the same discipline WCAG 2.1 AA compliance demands, and Section 3.10 states what we will and will not warrant.

**Public facing platforms with staff managed content.** The Cambrian College Alumni platform is a public facing product with institutional content behind it: a searchable directory with filters on industry, graduation year and location, an event lifecycle managed by staff, a career and resource area, and a content hub. Cambrian's alumni relations team manages that content. **[ATHIF TO CONFIRM: "Engagement tripled within six months of launch" and "became the primary channel for alumni relations". Remove both sentences if they cannot be evidenced.]** The transferable part is the pattern: a governed content and data model, filtered public discovery, and a staff workflow that does not route through the vendor.

**Ingest, aggregation and telemetry at frequency.** Chamber Perks, built with One Chamber System, is a member benefits platform where offers, merchants and redemptions are managed by chamber staff and surfaced to members, which is a publish, revise and retire lifecycle in commercial clothing. On the industrial side our team runs production telemetry pipelines ingesting more than ninety thousand messages per day, with scheduled collection, validation, failure handling and dashboards built on top. Economic indicator ingest is a lower volume, lower frequency version of the same engineering problem, and the parts that matter, scheduling, retry, validation, provenance and alerting on a silent source, are the parts we have already built.

For context on our analytical depth rather than as a claim of municipal experience: our team placed first out of twenty nine teams in the Côté Gold Blast Captain DevFest Challenge, an artificial intelligence competition run by IAMGOLD's Côté Gold Mine with Laurentian University, Cambrian College and Google Developer Group Sudbury. We cite it because it demonstrates that this team can take unfamiliar real world data and produce a defensible result under a hard deadline, which is the skill the window to 30 November 2026 will demand. We do not cite it as portal experience.

### 2.3 The honest comparison

| What COL-26-139 needs | What we have actually done | Where the gap is |
| --- | --- | --- |
| Public 24/7 data portal for a Canadian municipality | Public platforms for a Canadian college, a Canadian transportation operator, a chamber network and a German university hospital | We have not delivered this for a municipal economic development office. First municipal portal of this type. |
| Automated multi source ingest with refresh | Production telemetry ingest above ninety thousand messages per day, scheduled external data collection, validation and alerting | Our ingest experience is industrial and product telemetry rather than Statistics Canada and open data feeds. The engineering transfers. The specific connectors are new work in configuration. |
| Staff publish, revise and retire with roles | Staff managed content and lifecycle workflows in Cambrian Alumni and Chamber Perks | Comparable, delivered. |
| Charts, tables, maps, filters, export | Charts, tables and filtered discovery delivered. We have not delivered a municipal economic data portal or a production Esri implementation for a Canadian city. | Map layers would be configured from City supplied feature services in week one, not from an invented municipal GIS reference. **[ATHIF TO CONFIRM: map layer sources the City will provide.]** |
| WCAG 2.1 AA | Accessibility sensitive design in Wheel It and localization in COGITO | We have not been formally audited to WCAG 2.1 AA by a third party on those products. Section 3.10 states what we commit to. |
| Canadian hosting, no United States suppliers | All personnel and operations Canadian | Section 3.8 raises a real question about what "no United States suppliers" means for cloud infrastructure. We would rather ask than assume. |

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 2

---

## 3. The Software

Rated criterion, 50 points. This is the heaviest weighted section and it is written to be checked against Attachments 1 to 3 line by line.

### 3.1 What we are proposing, and what it is not

We propose a configurable data publishing platform assembled from components we already run in production, configured for the City's indicator set, branded to the City's visual identity, hosted in Canada, and handed to City staff to operate.

The distinction we want to be precise about, because evaluators are right to press on it, is this. We are not offering a shrink wrapped commercial off the shelf product with a published price list and a customer list of other municipalities. We do not have that, and a supplier who claims one should be asked for the customer list. What we are offering is a platform where the things that change are configuration rather than code:

- an indicator is a record, with a name, definition, unit, source, refresh schedule, geography, publication state and owner
- a source is a record, with a connector type, credentials, schedule, transformation and validation rules
- a page is a layout of components bound to indicators, arranged by an administrator
- a chart, table, map or filter is a component type with settings, not a bespoke build
- branding is theme configuration, not a template rewrite

The practical test the City should apply is this: after go-live, can City staff add an indicator, change its refresh frequency, correct a published value, retire an indicator and reorder a page without contacting the vendor. Under this proposal the answer is yes to all five, and we will demonstrate each of them live on 28 or 29 September rather than assert them here.

Where the City's requirements in Attachments 1 to 3 exceed what configuration covers, we will say so at the requirements validation stage in week one rather than discover it in November. Any such item becomes an explicit, scoped change with the City's agreement.

### 3.2 Public portal, no login, 24/7

The public portal is anonymous by design. No indicator page requires an account, an email address or a cookie consent gate to read a number.

The public surface is served as pre-rendered, cached content from a content delivery network with Canadian points of presence, refreshed when the underlying data changes rather than on every visitor request. Three consequences matter to the City:

1. Performance is predictable. A page that is already rendered does not slow down because forty people opened it during a council meeting or because a source system is busy.
2. Availability is decoupled from ingest. If a source feed fails at 03:00, the portal still serves the last published values, correctly labelled with their "as of" date, rather than showing an error or a blank chart.
3. The public attack surface is small. There is no public login, no public form posting into the data layer, and no personal information collected from public visitors, so the class of risk that dominates municipal web incidents is largely absent. Section 3.9 covers the staff side, which is where authentication actually lives.

Public analytics are limited to privacy respecting aggregate usage measurement so Economic Development can see which indicators are actually being used. **[ATHIF TO CONFIRM: whether the City wants a self hosted analytics option rather than a third party analytics service, given the supplier origin requirement in Section 3.8.]**

### 3.3 Data ingest, refresh and provenance

Ingest is the part of this portal that determines whether it is trusted in year three, so we treat it as the core of the build rather than as plumbing.

**Connector types.** The platform ingests from the source patterns a municipal indicator set typically depends on: REST and JSON web services, including statistical agency web data services; open data portal endpoints in the common CKAN and Socrata shapes; comma separated and Excel files delivered to a watched folder or secure file transfer location; spreadsheets maintained by a City business area; geospatial feature services; and, where a source genuinely offers no machine interface, an authenticated manual upload with the same validation and provenance rules as any automated feed. These are connector classes, not a claim about which sources the City's indicator set uses. That mapping comes from Attachments 1 to 3 and is confirmed in week one.

**Scheduling and refresh.** Each source carries its own schedule, because a building activity figure and a census derived population figure do not refresh at the same cadence. Schedules are configuration, expressed per source, and changeable by an administrator without a deployment. Every run is recorded.

**Validation before publication.** A refresh does not overwrite a published indicator simply because it returned data. Each incoming value passes configured checks: expected type and unit, expected range, expected row count, expected geography, and variance against the previous period beyond a configured threshold. A value that fails is quarantined rather than published, and the indicator continues to show its last good value with its "as of" date. The City's staff see the exception in the administration area, with the incoming value, the rule it broke and a one click accept or reject.

**Provenance on the public page.** Every published indicator displays its source, its "as of" date, its unit and its definition. Where a value has been revised, the revision is visible rather than silent. This is the single feature that most protects the City's credibility, because it means a site selector quoting a Lethbridge figure can see exactly what they are quoting.

**Staleness and failure alerting.** Each source has an expected refresh interval. When a source has not refreshed within its window, the administration area flags it and the platform emails the configured City owners and our support address. A silent failure is the failure mode that destroys trust in a data portal, so we make silence itself an alertable event.

**Data dictionary.** The portal publishes a data dictionary generated from the indicator records themselves, so definitions cannot drift away from what is displayed. This is a small feature that answers a large share of the questions Economic Development would otherwise field by email.

### 3.4 Staff administration and role based access control

City staff administer the portal through an authenticated area, separate from the public site.

**Roles.** Four roles, extendable in configuration:

- **Viewer, internal.** Sees drafts and unpublished indicators, cannot change them. Useful for a director who wants to review before publication.
- **Author.** Creates and edits indicators, pages and content, submits for publication. Cannot publish.
- **Publisher.** Everything an Author can do, plus publish, revise, retire and restore, plus resolve ingest exceptions.
- **Administrator.** Everything, plus sources, schedules, validation rules, roles, users, branding and site structure.

Permissions can be scoped so that, for example, a business area can maintain its own indicators without touching another area's. **[ATHIF TO CONFIRM: whether the City requires area scoped permissions at go-live or only the four global roles.]**

**Publication lifecycle.** Draft, in review, published, retired. Each transition is recorded with the user, timestamp and an optional note. Publication can be scheduled for a future date and time, which matters when a figure is embargoed until a release date. Retiring an indicator does not break the internet: the URL continues to resolve and explains that the indicator has been retired, with a date and, where the City wishes, a pointer to a replacement. Broken links from a municipal economic development site are cited by the people the City is trying to attract, so we handle retirement explicitly rather than by deletion.

**Versioning and audit.** Every published version of an indicator is retained and restorable. The audit log covers content changes, publication transitions, ingest runs, exception resolutions, role changes and sign ins, and is exportable for the City's records retention purposes. **[ATHIF TO CONFIRM: City records retention period applicable to portal audit logs.]**

**No vendor in the loop.** Nothing in the normal content lifecycle requires The Alpha Nova. This is a deliberate design position and it is the point of Section 3.1.

### 3.5 Visualization: charts, tables, maps and filters

One governed dataset, several presentations, no duplicated numbers.

**Charts.** Line and area for time series, column and bar for comparison, stacked variants for composition, scatter where a relationship is the point, and single value cards with trend indicators for headline figures. Charts are components bound to an indicator, with configured axis labels, units, number formats, colours from the City theme, annotations and source captions. Each chart offers a data table equivalent for users who prefer or require the numbers, which is both an accessibility requirement and a practical one.

**Tables.** Sortable, paginated, with configured column formatting, unit display and totals. A table is a first class presentation, not a fallback. Some of the portal's most valuable audiences want a table, not a picture.

**Maps.** Interactive maps configured from City supplied geospatial layers, rendered from Esri feature services, GeoJSON or shapefile inputs. Indicator values can be joined to geographies for choropleth display, with a legend, a defensible class break method, a hover and click detail panel, and a table alternative. We will confirm the layers, boundaries and coordinate reference systems with the City's GIS group in week one. **[ATHIF TO CONFIRM: City GIS contact, available feature services, and whether basemap tiles must also come from a non United States supplier, which materially narrows the basemap options.]**

**Filters.** Filters are declared per page and applied across the components on it, so a user who selects a geography or a time range sees every chart, table and map on the page move together. Filter state is reflected in the URL, which means a City staff member can send a colleague or a prospective investor a link to exactly the view they are describing. That single behaviour generates more real use of a portal than any other feature we could add.

**Search and discovery.** Indicator search across name, definition, source and tags, plus browse by theme. Every indicator has a permanent, human readable URL.

The specific charts, tables, maps and filters delivered at go-live are configured to the indicator set in Attachments 1 to 3. We have not invented a page inventory here, and we will not.

### 3.6 Export, reuse and embedding

Export is treated as a first class requirement rather than a button in a corner, because reuse is how the City's data does its job.

- Any table or chart exports to comma separated values and Excel, reflecting the filters applied at the moment of export rather than the unfiltered dataset.
- Charts export to portable image formats for use in reports and presentations, and pages print and export to PDF with the City's branding, source lines and "as of" dates intact.
- Every published indicator is available through a stable, read only, unauthenticated data endpoint returning JSON, so the City's own web team, a post secondary researcher or a partner agency can consume the number rather than transcribe it.
- Charts and tables can be embedded in another City page or a partner site through an embed code, with the source attribution and "as of" date carried into the embed so an out of date embed cannot masquerade as current.

**[ATHIF TO CONFIRM against Attachment 2: whether the City requires bulk download of the full indicator set as a single archive, and whether an open data licence statement must appear on export.]**

### 3.7 Branding and City visual identity

The portal is configured to the City of Lethbridge visual identity: logo assets, colour palette, typography, heading treatments, button styles, iconography, favicon and social sharing images, plus the City's required footer, privacy and terms links. Branding is theme configuration, so a future refresh of the City's identity is a configuration change, not a rebuild.

Typography and colour choices are validated against contrast requirements before go-live, because brand palettes and WCAG contrast ratios sometimes disagree and the City should know where, and decide, rather than inherit a quiet failure. Where the City has a web style guide, our design lead works from it directly. **[ATHIF TO CONFIRM: City of Lethbridge brand standards document and web style guide, and whether the portal sits on a City subdomain or a standalone domain.]**

### 3.8 Hosting, data residency and supplier origin

The City has expressed a preference for Canadian hosting and a requirement to avoid United States suppliers. We are treating both seriously and we are going to be straight with the City about a real tension between them.

All application data, backups, logs and content delivery caching are located in Canada under this proposal. No production data leaves Canada.

The complication is corporate control rather than geography. The large cloud platforms that operate Canadian regions are United States controlled corporations, and their Canadian regions are subject to that control regardless of where the disks sit. If the City's intent is data residency, a Canadian region of a major cloud platform satisfies it. If the City's intent is that no United States controlled supplier participates in the delivery chain, then those regions do not satisfy it, and neither do several common ancillary services: content delivery, email delivery, error monitoring, analytics and managed search are all dominated by United States suppliers.

We therefore propose two deployment options and ask the City to select one, and we would rather raise this in the proposal than discover it during contract negotiation:

**Option A. Canadian region of a major cloud platform.** Data resident in Canada, mature managed services, well understood operational tooling. Does not satisfy a strict no United States supplier test at the corporate control level.

**Option B. Canadian owned and Canadian operated infrastructure.** Satisfies both residency and supplier origin. Requires us to self manage several services that Option A provides as managed offerings, which we are prepared to do.

Both options are within reach for a portal of this size and shape. Our recommendation, if the City's no United States supplier requirement is to be read strictly, is Option B, with every ancillary service selected on the same test. Cost implications, if any, appear only in Schedule 1 and never in this document. **[ATHIF TO CONFIRM: which option the City requires, and provider selection under Option B. Do not name a hosting provider in the submitted document until this is settled.]**

### 3.9 Security and privacy

The public portal collects no personal information from public visitors, which removes most of the privacy surface before we start. What remains is staff access and the administrative plane.

- Staff authentication through the City's identity provider using SAML or OpenID Connect single sign on, with multi factor authentication enforced by the City's own policy, so account lifecycle stays in the City's hands and a departing employee loses portal access when they lose their City account. A local account fallback with multi factor authentication is available if the City prefers not to federate. **[ATHIF TO CONFIRM: City identity provider.]**
- Transport encryption throughout, encryption at rest for data and backups, and secrets held in a managed secret store rather than in configuration files.
- Least privilege on every service account, including the ingest credentials for each source.
- Administrative area not exposed to the public internet where the City's network arrangements allow restriction, otherwise protected by federated authentication, multi factor authentication and rate limiting.
- Web application firewall and rate limiting in front of both public and administrative surfaces.
- Backups on a defined schedule with tested restores, and stated recovery point and recovery time objectives in the support schedule.
- Dependency and vulnerability scanning in our build pipeline, with a defined patch cadence for the platform and its dependencies through the support term.
- Privacy review support for the City's obligations under Alberta's Freedom of Information and Protection of Privacy legislation. We are not offering a legal opinion. We are offering the technical documentation the City's privacy advisor will ask for. **[ATHIF TO CONFIRM: whether the City requires a completed privacy impact assessment as a deliverable, and whether a third party penetration test before go-live is required and by whom it is paid.]**

### 3.10 Accessibility

We commit to WCAG 2.1 Level AA as the design and testing standard for the portal, and to a specific, checkable set of behaviours rather than a slogan.

- Semantic structure and heading order that reflects the page, so screen reader users can navigate by heading and landmark.
- Full keyboard operability, including charts, filters, tables and maps, with a visible focus indicator and a skip link.
- Text alternatives for every non text element, and a table alternative for every chart and map, so the information in a visualization is never available only visually.
- Colour contrast validated against the City's palette, with variance raised to the City rather than absorbed silently, and no encoding of meaning by colour alone.
- Responsive layouts that reflow to small screens and to 400 percent zoom without loss of content or function.
- Testing with automated tooling in the build pipeline plus manual keyboard and screen reader passes on each template before go-live.

Alberta has no provincial equivalent of Ontario's accessibility statute, so WCAG 2.1 AA and the City's own web standards govern. **[ATHIF TO CONFIRM: City of Lethbridge accessibility standard and whether a third party accessibility audit is required as an acceptance condition. We have not been independently audited to WCAG 2.1 AA on a prior product and we will not imply otherwise.]**

### 3.11 Performance, availability and monitoring

The pre-rendered public surface described in Section 3.2 is what makes the performance commitments below realistic rather than aspirational.

- Target first contentful paint under two seconds on a standard connection for public indicator pages, and interactive charts responding to a filter change without a full page reload.
- Uptime monitoring at short intervals from outside our own infrastructure, alerting on state change rather than on every failed check, so a genuine outage produces a small number of actionable alerts instead of hundreds. We run this pattern on our own properties today.
- Ingest run monitoring, staleness alerting and error reporting as described in Section 3.3.
- A monthly service report to Economic Development covering availability, ingest success rates by source, exceptions raised and resolved, portal usage by indicator, and any incidents.
- Availability target and support response commitments are stated in the support schedule, with any associated cost in Schedule 1 only. **[ATHIF TO CONFIRM: whether the RFQ or the City's standard agreement specifies a service level the City will not negotiate.]**

### 3.12 Configuration versus custom development

To make the configurable claim testable, this is the boundary as we understand it today, subject to reconciliation against Attachments 1 to 3.

| Change | Who does it | How |
| --- | --- | --- |
| Add, edit or retire an indicator | City staff | Administration area, no deployment |
| Change a refresh schedule | City administrator | Configuration |
| Add a source in an existing connector class | City administrator, or us under support | Configuration, credentials supplied by the City |
| Add a new connector class for an unusual source | The Alpha Nova | Platform work, scoped and agreed |
| Add or reorder a page, change chart type, add a filter | City staff | Page composition, no deployment |
| Change branding, colours, logo, typography | City administrator | Theme configuration |
| Add a new component type not in the library | The Alpha Nova | Platform work, scoped and agreed |
| Add a user or change a role | City administrator | Administration area |
| Platform, dependency and security updates | The Alpha Nova | Support term |

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 3

---

## 4. Implementation Plan to 30 November 2026

### 4.1 The constraint, stated plainly

Demonstrations are 28 and 29 September 2026. Go-live is required by 30 November 2026. Award timing is the City's to determine and is not published in the RFQ. Working from an assumed award in the first half of October, the delivery window is approximately seven to eight weeks including a Canadian statutory holiday and the City's own review time.

That window is achievable for a configured platform. It is not achievable for a bespoke build, which is the practical reason Section 3.1 is framed the way it is. It also means the City's own responsiveness is on the critical path, and Section 4.3 says exactly where.

### 4.2 Phases

**Phase 0. Mobilization. Week 1.**
Kick off with Economic Development and the City's information technology and GIS contacts. Confirm the indicator set from Attachments 1 to 3, source by source, including owner, access method, credentials, refresh frequency, definition and geography. Confirm hosting option under Section 3.8. Confirm identity provider, brand assets, domain and accessibility standard. Deliverable: a signed off requirements and source register, which becomes the acceptance baseline. This is the single most important week in the project and it happens first for that reason.

**Phase 1. Environment, ingest and data model. Weeks 1 to 3.**
Stand up development, staging and production environments in the selected Canadian hosting arrangement. Configure the indicator and source records. Build and test each connector against the real source, not a sample file. Configure validation rules and thresholds per indicator with the City's data owners. Deliverable: every source ingesting on schedule into staging, with provenance and exception handling working, evidenced by run logs the City can inspect.

**Phase 2. Presentation, branding and content. Weeks 2 to 5.**
Configure pages, charts, tables, maps and filters for the confirmed indicator set. Apply City branding and validate contrast. Configure the data dictionary, retirement pages, search and export. Two structured review sessions with Economic Development on staging, at the end of week 3 and the end of week 5, so feedback arrives while it is still cheap. Deliverable: complete portal on staging with real data.

**Phase 3. Accessibility, security, performance and user acceptance. Weeks 4 to 6.**
Automated and manual accessibility passes on every template. Security review and hardening. Performance testing and cache tuning. Role based access control walkthrough with the actual City staff who will hold each role, using a script we provide. Staff training, two sessions, recorded, plus written administrator and author guides. Deliverable: accessibility test record, security review record, signed user acceptance testing results, training complete.

**Phase 4. Go-live. Week 7, no later than 30 November 2026.**
Production cut over, domain and certificate configuration, search engine indexing and sitemap, redirects from any existing City page the portal replaces, monitoring and alerting confirmed live, first production ingest cycle verified against source. Deliverable: portal live and accepted.

**Phase 5. Hypercare. 30 days after go-live.**
Elevated response, daily ingest verification for the first two weeks, weekly check in with Economic Development, and a post implementation review that closes out any deferred item in writing. Transition to standard support at day 31.

### 4.3 City responsibilities

Stated as commitments rather than assumptions, because the schedule depends on them.

1. A single City project contact empowered to make decisions, plus named data owners for each source.
2. Source access, credentials and any required firewall or allow list changes within five business days of request.
3. Brand assets and web style guide at kick off.
4. Identity provider configuration support in Phase 1.
5. GIS layers and a GIS contact in Phase 1.
6. Written feedback from each staging review within five business days.
7. City staff available for role based access control walkthrough, user acceptance testing and training in Phase 3.
8. Domain, certificate and any DNS changes coordinated before Phase 4.

### 4.4 If award slips

If award occurs late enough that the full scope cannot be delivered to the standard above by 30 November 2026, we will say so at kick off rather than in November. The contingency, subject to the City's agreement, is a staged go-live: the confirmed core indicator set live and correct by 30 November 2026, with the remaining indicators configured and published on an agreed schedule in December. We prefer that to a full portal that is live on time and wrong, and we would rather have the conversation in writing in week one.

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 4

---

## 5. Demonstration

Rated criterion, 10 points. Held 28 and 29 September 2026 for the top three ranked proponents. We will attend on either date, in person or virtually, at the City's preference. **[ATHIF TO CONFIRM: format, duration and whether the City sets the agenda or the proponent does.]**

We would use the time to let the evaluation committee test the claims in Section 3 rather than to present slides. Our proposed structure, adaptable to whatever the City prescribes:

1. **Two minutes of framing, not a company pitch.** Who is in the room and what we will prove.
2. **The public experience.** A live portal configured with publicly available Lethbridge area data, so evaluators see the real thing rather than a mock. We will use only public sources for this, and we will label it as a demonstration configuration rather than imply it is the City's portal.
3. **Charts, tables, maps and filters on one page.** Move a filter, watch every component follow, copy the URL, open it fresh, land on the same view.
4. **Export, live.** Filter a table, export it, open the file in front of the committee.
5. **The staff workflow, performed not described.** Sign in as an Author, create an indicator, submit it. Sign in as a Publisher, publish it, see it appear on the public site, revise it, then retire it and show the retirement page. This is the demonstration that separates a configurable platform from a bespoke site.
6. **Ingest and provenance.** Show a source register, a run history, a deliberately failed validation sitting in quarantine, and the alert it generated.
7. **Accessibility, live.** Keyboard only navigation through a chart, and the table alternative.
8. **Administration.** Change a brand colour, add a user, change a role, all without a deployment.
9. **Questions, with the engineer who built it in the room.** Ertugrul Sahin attends and answers architecture questions directly. Athif Shaffy leads. Deepshika Ghale answers design and accessibility questions. Shubham Dhamane answers requirements and workflow questions.

We will not use the demonstration to introduce scope the City did not ask for, and we will not show generative artificial intelligence features. If a competitor does, the City should ask them who reviews the generated text before a resident reads it.

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 5

---

## 6. Support, Maintenance and Term

The initial term is four years, with two City held options of four years each. A portal that has to survive up to twelve years should be bought on its operating characteristics, not its launch.

**Support scope.** Incident response and correction, ingest failure diagnosis and repair, platform and dependency updates including security patches, accessibility regression checks after significant updates, backup verification and restore testing, monitoring and alerting operation, monthly service reporting, and reasonable configuration assistance for City staff.

**Response commitments.** Severity based, with a critical severity covering the public portal being unavailable or publishing a materially incorrect value, and lower severities for degraded function, single source ingest failures and requests for assistance. Specific target times, hours of coverage and any after hours arrangement are stated in the support schedule with costs in Schedule 1 only. **[ATHIF TO CONFIRM: response and resolution targets Athif is willing to be held to for four to twelve years, including whether coverage is business hours Mountain Time or extended.]**

**Continuity and exit.** The City's data is the City's. The portal's content, indicator definitions, historical values and configuration are exportable in open formats at any time on request and at the end of any term, without an exit fee. We will document the deployment such that another supplier could take it over. A supplier who makes exit expensive has told the City something about the next twelve years.

**Roadmap.** Platform improvements delivered to all clients of the platform during the support term arrive at no additional licence cost. City specific enhancements beyond configuration are quoted separately at the rates in Schedule 1.

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 6

---

## 7. Price

Rated criterion, 30 points.

Pricing is submitted **only** in Schedule 1, Revision 1, using **either** Model 1 **or** Model 2, not both. No dollar amount, rate, licence fee, hourly rate or cost estimate appears anywhere in this technical proposal, and any reader who finds one in this document should treat it as an error to be removed before submission.

Our commitments on price behaviour, which cost nothing to state here and matter over a twelve year horizon:

- The pricing submitted covers the scope described in Sections 3 and 4 as reconciled against Attachments 1 to 3. Where our understanding of an attachment is incomplete, we identify it in Section 11 rather than pricing an assumption in silence.
- Indicator additions and content changes performed by City staff carry no charge from us, because they do not involve us.
- Support pricing is stated for the full initial term so the City is not exposed to an unpredictable escalation in year three.
- Any pricing dependency created by the hosting decision in Section 3.8 is identified in Schedule 1 rather than resolved by assumption.

**[ATHIF TO CONFIRM before submission: (1) Model 1 or Model 2, selected deliberately, one only, submitting both risks non compliance; (2) that Schedule 1 Revision 1 is the current revision issued under Addendum 1; (3) that no figure has leaked into the technical file.]**

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 7

---

## 8. Project Team

Titles are exact. Full resumes are in Appendix A. Allocations are proposed commitments for the delivery window described in Section 4.

| Name | Title | Role on COL-26-139 | Proposed allocation |
| --- | --- | --- | --- |
| Athif Shaffy | Founder & CEO | Engagement lead. Single point of accountability, City relationship, scope decisions, escalation. Attends demonstration. | Phases 0 to 5, approximately 30 percent through go-live |
| Ertugrul Sahin | Senior Software Developer | Solution architect and technical lead. Platform configuration, ingest connectors, validation, security and performance. Attends demonstration. | Phases 0 to 4, approximately 70 percent through go-live |
| Laxman KC | Software Developer | Ingest implementation, scheduling and alerting, export and endpoints, testing. | Phases 1 to 4, approximately 60 percent through go-live |
| Deepshika Ghale | UI Consultant | Interface configuration, chart and map presentation, City branding, WCAG 2.1 AA design and testing. Attends demonstration. | Phases 1 to 3, approximately 40 percent |
| Shubham Dhamane | Business Analyst | Requirements and source register, validation rules with data owners, user acceptance testing coordination, staff training and documentation. Attends demonstration. | Phases 0 to 5, approximately 40 percent |
| Cheick Ismael Maiga | Technical Advisor, P.Eng. | Advisory. Technical review at architecture sign off and before go-live. Not day-to-day delivery staff and not independent of The Alpha Nova. | Advisory, as required |
| Dr. Markus Lehmann | Strategic Advisor | Advisory. Enterprise architecture and technology strategy review. | Advisory, as required |
| Prof. Dr. Steffen Moritz | Lead Scientific Advisor | Advisory. Data presentation and reporting rigour. | Advisory, as required |

### 8.1 Disclosures

We would rather disclose these than have the City find them.

**Dr. Markus Lehmann** holds an advisory relationship with The Alpha Nova as Strategic Advisor. He is named here as an advisor to this engagement. He is not offered as a client reference.

**Prof. Dr. Steffen Moritz** occupies two roles simultaneously. He is our Lead Scientific Advisor, and he is the University Medical Center Hamburg-Eppendorf client on the COGITO engagement cited in Section 2.2 and offered as a reference in Section 9. The City should weigh that reference knowing he is also an advisor to our company. We are providing him as a reference because he is the person who can actually speak to the COGITO work, and we are disclosing the dual role so the City can discount it as it sees fit.

**Optional local advisor.** Sidney Shapiro has agreed in principle to review our approach for this opportunity. No hours have been committed, no fee has been agreed, and he is not named as key personnel in this response. If the City would value a Lethbridge based reviewer on the engagement we can add that, with his bio and affiliation stated exactly as he approves it. **[ATHIF TO CONFIRM: whether to include Sidney Shapiro at all, and obtain his written bio and affiliation before any version of this document names him further. Do not commit his hours until Athif confirms.]**

### 8.2 Team continuity

The named individuals are the individuals who deliver. We do not substitute personnel after award without the City's written consent, and any proposed substitute would be of equivalent or greater qualification with resumes provided. Given the four year initial term, our succession position is that no single person holds undocumented knowledge: configuration is held as data, the deployment is documented, and Cheick Ismael Maiga's advisory review at architecture sign off exists partly to ensure a second qualified person understands the system.

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 8

---

## 9. References

Three live, confirmed contacts. Each one can speak to work our team actually did. We have not padded this list with municipal names we do not have.

**1. University Medical Center Hamburg-Eppendorf (UKE), COGITO**
Prof. Dr. Steffen Moritz
moritz@uke.de, +49 40 7410 56565
Relevance: multi language application with a clinician facing analytics and reporting surface, strict privacy requirements. **[ATHIF TO CONFIRM: "deployment across multiple institutions" and "peer reviewed validation" before they appear in the submitted reference block.]** Speaks to our ability to present data that professionals act on.
Disclosure: Prof. Dr. Moritz is also The Alpha Nova's Lead Scientific Advisor. See Section 8.1.

**2. One Chamber System, Chamber Perks**
Karen Hastie
karen@onechambersystem.com, +1 705 669 7343
Relevance: platform where staff publish, revise and retire content that members consume, with a member facing discovery experience and an administrative workflow behind it. Speaks to the publish and retire lifecycle in Section 3.4.

**3. Wheel It Transportation, Wheel It**
Shaunna Babyak
info@wheelittransportation.com, +1 705 929 8006
Relevance: public facing Canadian platform where accessibility is central to the user base rather than an afterthought. Speaks to Section 3.10.

**[ATHIF TO CONFIRM: notify all three contacts before submission that a City of Lethbridge evaluator may call, and confirm the number of references the RFQ actually requires. If the RFQ requires municipal references specifically, we do not have three and should say so rather than substitute.]**

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 9

---

## 10. Assumptions, Dependencies and Risks

### 10.1 Assumptions

1. The indicator set, sources and refresh frequencies are as stated in Attachments 1, 2 and 3, and are confirmed in Phase 0.
2. Every source the City names is accessible to us by a machine interface, a file delivery, or a City maintained spreadsheet, and the City can grant that access.
3. The City provides brand assets, GIS layers and identity provider configuration in Phase 1.
4. The portal publishes aggregate and open data. No personal information is published, and none is collected from public visitors.
5. The City reviews staging and returns written feedback within five business days at each review point.
6. Award occurs early enough to permit the plan in Section 4. If not, Section 4.4 applies.

### 10.2 Risks and mitigations

| Risk | Consequence | Mitigation |
| --- | --- | --- |
| Award later than assumed | 30 November go-live at risk | Staged go-live per Section 4.4, agreed in writing at kick off rather than negotiated in November |
| A named source has no usable machine interface | Manual refresh burden on City staff | Identified in Phase 0 source register, authenticated upload with the same validation and provenance as automated feeds |
| A source changes format or stops publishing during the term | Indicator goes stale silently | Validation rules, staleness alerting and quarantine per Section 3.3. Silence is itself an alert |
| Brand palette fails contrast requirements | Accessibility non compliance or brand deviation | Contrast validated in Phase 2, variance raised to the City for decision rather than absorbed |
| Strict reading of no United States suppliers | Hosting and ancillary service rework after award | Raised now in Section 3.8 with two options for the City to choose between before contract |
| City staff turnover over a term of up to twelve years | Portal knowledge lost, content stagnates | Recorded training, written administrator and author guides, configuration held as data, refresher training available under support |
| Indicator definitions disputed after publication | Credibility damage | Data dictionary generated from the indicator records, visible provenance and revision history |

### 10.3 Contractual matter we are raising rather than accepting quietly

The solicitation documents include a limitation of liability provision that, as drafted, does not cap the supplier's liability. **We are flagging this for Athif's decision and for discussion with the City rather than papering over it.** An uncapped liability exposure on a data publishing engagement of this size is not a term we can accept without review, and pretending otherwise at proposal stage only moves the problem to contract execution.

Our position, subject to Athif's instruction and to legal review, is that we would seek a liability cap proportionate to the contract value, with the customary carve outs, and that we would raise it as a proposed clarification rather than as an unqualified exception that risks the bid being set aside.

**[ATHIF TO CONFIRM, before submission: (1) legal review of the unlimited liability clause; (2) whether the City's process permits a noted exception or clarification request without rendering the submission non compliant, noting the question period closed 31 August 2026 so this can no longer be raised as a question; (3) whether our insurance limits can bear the exposure as drafted; (4) whether we bid at all on these terms. This is a genuine go or no go item and it should not be decided at 13:00 on 10 September.]**

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 10

---

## 11. Compliance Matrix

| RFQ requirement, as understood | Where we answer it | Status |
| --- | --- | --- |
| Public access, 24/7, no login | 3.2 | Met |
| Multi source data ingest | 3.3 | Met, sources confirmed in Phase 0 |
| Automatic refresh | 3.3 | Met, per source schedules |
| Staff publish and retire, role based access control | 3.4 | Met |
| Charts | 3.5 | Met |
| Tables | 3.5 | Met |
| Maps | 3.5 | Met, subject to City GIS layers |
| Filters | 3.5 | Met, cross component with shareable URLs |
| Export | 3.6 | Met, CSV, Excel, image, PDF, JSON endpoint, embeds |
| City branding | 3.7 | Met, theme configuration |
| Canadian hosting preference | 3.8 | Met, all data in Canada |
| No United States suppliers | 3.8 | Question raised. Two options presented for City selection |
| Off the shelf or configurable rather than bespoke | 3.1, 3.12 | Met as configuration. We do not claim a shrink wrapped product with a municipal customer list |
| Go-live by 30 November 2026 | 4 | Committed, with Section 4.4 contingency if award slips |
| Term of four years plus two four year options | 6 | Addressed |
| Experience, 10 points | 2 | Answered, including the honest gap in 2.3 |
| Software, 50 points | 3 | Answered |
| Demonstration, 10 points | 5 | Available 28 or 29 September 2026 |
| Price, 30 points | 7, Schedule 1 Revision 1 | Schedule 1 only, Model 1 or Model 2, never both |
| Page limit of 30 pages excluding City appendices | Whole document | **[ATHIF TO CONFIRM after Word layout]** |
| Addendum 1 | Cover | Acknowledged in draft, **[ATHIF TO CONFIRM acknowledgement in the portal]** |
| Attachments 1 to 3 | 1.4 | **Not yet retrieved. Reconcile before submission** |
| Mandatory City forms | City appendices | **[ATHIF TO CONFIRM]** |
| Insurance, WCB, registration | City appendices | **[ATHIF TO CONFIRM]** |
| Limitation of liability | 10.3 | **Flagged, unresolved, go or no go** |

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 11

---

## 12. Appendix A: Resumes of Proposed Personnel

Facts below are as confirmed for this bid. Nothing has been inflated, and items awaiting Athif's confirmation are marked.

### Athif Shaffy
**Founder & CEO. Engagement lead.**
Greater Sudbury, Ontario

**Profile.** More than seven years of professional experience in software delivery and technology leadership. Founder and Chief Executive Officer of The Alpha Nova Inc., where he leads company strategy, client partnerships and product direction from the company's Greater Sudbury headquarters. On this engagement he is the City's single point of accountability: scope decisions, escalation, and the person who answers the phone in year three.

**Experience.**
- The Alpha Nova Inc., Founder & CEO, September 2020 to present. Greater Sudbury, Ontario. Founded and leads the company across artificial intelligence and intelligent systems, industrial Internet of Things and edge, software engineering and product engineering. Engagement lead on client delivery including COGITO with the University Medical Center Hamburg-Eppendorf, the Cambrian College Alumni platform, Wheel It and Chamber Perks.
- Maestro, November 2022 to February 2025. **[ATHIF TO CONFIRM: exact position title, employer legal name and a one line scope statement.]**
- Cambrian College, instructor. **[ATHIF TO CONFIRM: exact title, subject area and dates.]** Relevant here because teaching the material is a reasonable proxy for being able to train City staff, which is a Phase 3 deliverable.

**Education.** Bachelor of Science, First Class Honours, Staffordshire University. **[ATHIF TO CONFIRM: exact programme name and year of award.]**

**Community and recognition.**
- Google Developer Group Sudbury. **[ATHIF TO CONFIRM: role, organizer or member, and years.]**
- First place, Côté Gold Blast Captain DevFest Challenge. Artificial intelligence competition run by IAMGOLD's Côté Gold Mine with Laurentian University, Cambrian College and Google Developer Group Sudbury. First of twenty nine teams.
- First place, Comms-Denied Autonomy challenge, York, 2026. **[ATHIF TO CONFIRM: full event name and host institution.]**

**Relevance to COL-26-139.** Accountability across a four year initial term with two renewal options, delivery under a hard external deadline, and direct experience leading engagements where the client depends on published data being correct.

---

### Ertugrul Sahin
**Senior Software Developer. Solution architect and technical lead.**

**Profile.** Senior developer responsible for complex feature development and system architecture at The Alpha Nova, with a focus on robust, scalable backend systems and engineering quality across the team. On this engagement he owns the architecture: ingest connectors, validation, the publication data model, security posture and performance of the public surface.

**Experience.**
- The Alpha Nova Inc., Senior Software Developer, March 2026 to present. Leads complex feature development and system architecture, builds scalable backends, and guides engineering quality across the team.
- Cambrian College, research and development, March 2023 to March 2026. Applied research and development software engineering. **[ATHIF TO CONFIRM: exact position title within the college's research office and a one line scope statement.]**

**Education.** Computer Engineering, Beykent University. **[ATHIF TO CONFIRM: degree designation and year of award.]**

**Recognition.**
- First place, Côté Gold Blast Captain DevFest Challenge, first of twenty nine teams. Built the computer vision and analysis pipeline that produced the winning result.

**Relevance to COL-26-139.** Three years of applied research and development delivery followed by senior architecture ownership. The Côté Gold result is direct evidence of taking unfamiliar real world data through a working pipeline to a defensible output under a fixed deadline, which is what Phase 1 of Section 4 asks of him.

---

### Laxman KC
**Software Developer. Ingest, scheduling, export and testing.**

**Profile.** Developer who ships features across web and mobile products, turning requirements and designs into reliable, well tested code that holds up in production. On this engagement he implements the ingest schedules, the alerting that makes a silent source visible, the export paths and the read only data endpoints.

**Experience.**
- The Alpha Nova Inc., Software Developer, January 2024 to present. Feature development across web and mobile products, including data ingest and telemetry work.
- Cambrian College, research and development, December 2024 to present. Applied research and development engineering alongside his work at The Alpha Nova. **[ATHIF TO CONFIRM: exact position title, and confirm the concurrent arrangement is stated the way Laxman and the college want it stated.]**
- Production telemetry pipelines ingesting more than ninety thousand messages per day, covering scheduled collection, validation, failure handling and the dashboards built on top. This is the closest thing in our record to the ingest reliability problem in Section 3.3.

**Education.** Diploma, Internet of Things. **[ATHIF TO CONFIRM: institution and year of award.]**

**Recognition.**
- Multiple awards in 2026 hackathons and technical competitions. **[ATHIF TO CONFIRM: which events and placements, so we can name them specifically rather than in aggregate.]**

**Relevance to COL-26-139.** Direct, hands on experience with high frequency data ingest, validation and failure handling. Economic indicator refresh is a lower volume version of a problem he already runs in production.

---

### Deepshika Ghale
**UI Consultant. Interface, visualization presentation, branding and accessibility.**
Greater Sudbury, Ontario

**Profile.** User interface and user experience consultant who advises The Alpha Nova on interface design and user experience, turning complex flows into intuitive, scalable interfaces using Figma and rapid prototyping. On this engagement she configures the public presentation, applies the City's visual identity, and owns WCAG 2.1 AA conformance in design and testing.

**Experience.**
- The Alpha Nova Inc., UI Consultant, March 2025 to present. Interface and user experience advisory across client engagements, design systems, prototyping in Figma, and design quality review.
- Cambrian College, research and development, April 2024 to April 2025. Applied research and development design work. **[ATHIF TO CONFIRM: exact position title.]**

**Skills.** Interface design and design systems, Figma, interactive prototyping, accessible interface patterns, responsive layout, data visualization presentation and legibility.

**Recognition.**
- First place, Cursor Sudbury 2026. **[ATHIF TO CONFIRM: full event name and host.]**

**Relevance to COL-26-139.** The portal's rated value depends on whether a resident, a councillor and a site selector can each find and read the number they came for. That is an interface problem before it is a data problem, and it is hers.

---

### Shubham Dhamane
**Business Analyst. Requirements, validation rules, user acceptance testing and training.**
Greater Sudbury, Ontario

**Profile.** Business analyst who bridges business and engineering, translating client goals into clear requirements and holding delivery to measurable value. On this engagement he produces the Phase 0 requirements and source register that becomes the acceptance baseline, agrees the validation rules with each City data owner, coordinates user acceptance testing, and delivers staff training and the written administrator and author guides.

**Experience.**
- The Alpha Nova Inc., Business Analyst, **[ATHIF TO CONFIRM: start date.]** Requirements definition, stakeholder facilitation, acceptance criteria and delivery of documentation across client engagements.
- **[ATHIF TO CONFIRM: prior relevant employment, dates and one line scope, plus education and any certification such as business analysis or project management credentials. Do not list a certification we cannot produce.]**

**Relevance to COL-26-139.** The single largest risk in a fixed date portal project is an indicator set that is agreed loosely in October and disputed in November. His Phase 0 register exists to prevent exactly that.

---

### Cheick Ismael Maiga
**Technical Advisor, P.Eng. Independent technical review.**
Canada

**Profile.** Professional Engineer and Technical Advisor to The Alpha Nova, advising across our engineering engagements and bringing hands on engineering depth and rigour to demanding technical work.

**Role on this engagement.** Advisory, at two defined gates: technical review of the architecture at the end of Phase 1, and a pre go-live review in Phase 4. His involvement also ensures a second qualified engineer understands the deployment, which is a continuity control for a term that may run twelve years. He is The Alpha Nova's Technical Advisor, not an independent third-party reviewer.

**[ATHIF TO CONFIRM: province of P.Eng. licensure and whether the City requires evidence of licensure or a permit to practise in Alberta for advisory work of this kind. Do not assert Alberta licensure.]**

---

### Dr. Markus Lehmann
**Strategic Advisor. Technology strategy and enterprise architecture review.**

**Profile.** Advises The Alpha Nova on technology strategy and enterprise architecture, bringing industry experience to complex engagements.

**Role on this engagement.** Advisory, as required, on platform direction and long term architectural sustainability across the initial and optional terms.

**Disclosure.** Dr. Lehmann holds an advisory relationship with The Alpha Nova. He is not presented as an independent client reference for this bid. See Section 8.1.

---

### Prof. Dr. Steffen Moritz
**Lead Scientific Advisor. Data presentation and reporting rigour.**

**Profile.** Head of the Clinical Neuropsychology Working Group in the Department of Psychiatry and Psychotherapy at the University Medical Center Hamburg-Eppendorf, and Professor of Clinical Psychology. Lead Scientific Advisor to The Alpha Nova, and collaborator with our team on the COGITO application.

**Role on this engagement.** Advisory, as required, on the rigour of how data is presented and qualified, which is directly relevant to the provenance and revision handling in Section 3.3.

**Disclosure.** Prof. Dr. Moritz is both our Lead Scientific Advisor and the University Medical Center Hamburg-Eppendorf client on the COGITO engagement cited in Section 2.2 and offered as Reference 1 in Section 9. The City should weigh that reference accordingly. See Section 8.1.

---

### Sidney Shapiro
**Optional local reviewer. Not proposed as key personnel in this response.**

Sidney Shapiro has agreed in principle to review our approach for this opportunity. No hours are committed and no fee is agreed. He is named here only so that Athif can decide whether to include him.

**[ATHIF TO CONFIRM before he appears in any submitted document: his written bio, his exact affiliation and title as he wishes it stated, his consent to be named in a City of Lethbridge submission, and the scope of his involvement. Do not commit his hours until Athif confirms the bio.]**

The Alpha Nova | Economic and Investment Data Portal | COL-26-139
Confidential | INTERNAL DRAFT | Page 12

---

# INTERNAL. ATHIF ONLY. STRIP THIS PAGE BEFORE SUBMISSION.

## Go or no go, decide before 8 September

- [ ] **Unlimited liability clause.** Section 10.3. Legal review needed. Question period closed 31 August 2026, so this cannot be asked as a question any more. Options are bid as is, bid with a noted clarification and accept the non compliance risk, or no bid. This is the real decision on this file.
- [ ] **Attachments 1, 2 and 3.** Not retrieved. Download from lethbridge.bidsandtenders.ca and reconcile Sections 3.3, 3.5, 3.12 and 11. Nothing in this draft invents a wishlist indicator and it must stay that way.
- [ ] **Schedule 1 Revision 1.** Confirm it is the revision issued under Addendum 1. Choose Model 1 or Model 2, one only. Submitting both risks non compliance.
- [ ] **No dollars in the technical file.** Search the final document for currency symbols and figures before upload.

## Compliance mechanics

- [ ] Addendum 1 acknowledged inside the bidsandtenders portal, not just noted on our cover.
- [ ] Page count under 30, excluding City appendices, verified after Word or PDF layout. This markdown is longer than its laid out page count will suggest, and it will still need trimming. Cut candidates, in order: Section 2.2 narrative, Section 3.12 table, Section 10.2 table.
- [ ] All City mandatory forms completed and attached.
- [ ] Insurance certificate, WCB Alberta position and Alberta extra provincial registration resolved. None asserted in the technical file.
- [ ] Every communication through the portal only. Do not email nicki.vaneck@lethbridge.ca directly.
- [ ] Hosting decision under Section 3.8 settled enough to submit. Do not name a hosting provider until it is.

## People

- [ ] Confirm all resume gaps in Appendix A. Athif's Maestro title, Cambrian instructor title, Staffordshire programme name, GDG Sudbury role, York 2026 event name. Ertugrul's Cambrian title and Beykent degree designation. Laxman's Cambrian title, IoT diploma institution, and which 2026 hackathons. Deepshika's Cambrian title and the Cursor Sudbury event name. Shubham's start date, prior employment and education.
- [ ] Cheick's P.Eng. province, and whether Alberta practice permission is needed for advisory work.
- [ ] Sidney Shapiro. He said yes to reviewing. Do not commit his hours or publish a bio until Athif confirms the wording with him.
- [ ] Warn all three references that a Lethbridge evaluator may call. Confirm the RFQ's required reference count and format.
- [ ] Confirm the Moritz and Lehmann disclosures in Section 8.1 read the way Athif wants them to read. They are deliberate and they should stay.

## Positioning check

- [ ] No generative artificial intelligence framing anywhere. This is a clean data portal buy. Verified in this draft. Keep it that way through every edit.
- [ ] No claim of a municipal economic and investment portal reference. Section 2.3 states the gap plainly. Do not let a later edit soften it into an implication we do not have.
- [ ] No em dashes. No Passau. No Colombo. No three continents.

## Submission

- Close: Thursday 10 September 2026, 14:00 MDT.
- Target submit: **Tuesday 8 September 2026**, or Wednesday 9 September at the latest. Never close day.
- Demonstration hold: 28 and 29 September 2026, top three only. Put both days in the calendar now for Athif, Ertugrul, Deepshika and Shubham.
- Go-live commitment if we win: 30 November 2026.

**The Alpha Nova | Confidential | INTERNAL DRAFT. NOT FOR SUBMISSION.**
