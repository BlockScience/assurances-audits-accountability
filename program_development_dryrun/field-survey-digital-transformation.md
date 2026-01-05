---
type: vertex/doc
extends: doc
id: v:doc:field-survey-digital-transformation
name: Field Survey - Digital Transformation Program
description: Maps stakeholders, resources, and relationships for organizational digital transformation of a 150-person professional services firm
tags:
  - vertex
  - doc
  - field-survey
version: 1.0.0
created: 2026-01-05T10:00:00Z
modified: 2026-01-05T10:00:00Z
survey_scope: Meridian Consulting Group organizational operations, IT infrastructure, and workforce capabilities
actor_count: 8
resource_count: 9
relationship_count: 18
survey_date: 2026-01-05
geographical_bounds: Headquarters plus three regional offices (Northeast, Southeast, West Coast)
jurisdictional_bounds: Private professional services firm with client data handling obligations
---

# Field Survey - Digital Transformation Program

This field survey documents the current state of Meridian Consulting Group's operations, technology infrastructure, and workforce to inform the design of a comprehensive digital transformation program.

## Animating Purpose

### Why This Survey

Meridian Consulting Group is a 150-person professional services firm specializing in management consulting, strategy advisory, and organizational development. Founded in 1998, the firm has grown through acquisition and organic expansion but operates with fragmented systems, inconsistent processes, and a culture that has historically relied on senior partner relationships rather than institutionalized knowledge management.

Three forcing functions are driving digital transformation:

1. **Client Expectations:** Enterprise clients increasingly require secure collaboration platforms, real-time project dashboards, and demonstrated data governance—capabilities Meridian lacks
2. **Competitive Pressure:** Boutique competitors and Big Four digital practices offer integrated technology stacks that Meridian cannot match with current infrastructure
3. **Workforce Demographics:** 40% of staff are under 35 and expect modern collaboration tools; senior partners retiring within 5 years hold institutional knowledge that must be captured

The firm's current state includes: disparate document management (shared drives, email attachments, personal laptops), no unified CRM, manual time tracking, limited data analytics capability, and outdated on-premises email servers. Productivity losses, security risks, and inability to demonstrate value to clients are quantifiable business impacts.

This survey documents the landscape of stakeholders, systems, and organizational dynamics to inform architecture decisions for digital transformation.

### Scope Statement

This survey covers Meridian Consulting Group's organizational structure, IT infrastructure, business processes, client relationships, and workforce across all four locations, focusing on elements that would be affected by or required for digital transformation.

### Key Questions

This survey aims to answer:

1. Who are the key actors involved in operations, client delivery, technology decisions, and organizational culture?
2. What systems, processes, and infrastructure currently support firm operations?
3. How do actors depend on resources, and where are the critical pain points and dependencies?
4. What workforce skills and change readiness exist, and what gaps would transformation create?
5. What security, compliance, and data governance requirements constrain technology choices?

## Actors

The following actors have been identified within the survey scope.

| ID | Name | Type | Description | Accountability |
|----|------|------|-------------|----------------|
| A1 | Managing Partner Committee | Organization | Three-person executive committee governing firm strategy | Strategic direction, capital allocation, partner compensation, major investments |
| A2 | Practice Area Leaders | Role | Six senior partners leading industry and functional practices | Revenue targets, staff development, methodology, client relationships |
| A3 | IT Department | Organization | Four-person team managing technology infrastructure | Systems maintenance, user support, security, vendor management |
| A4 | Consultants (Staff Level) | Role | 85 staff consultants and analysts delivering client work | Client deliverables, utilization targets, professional development |
| A5 | Operations Team | Organization | 12-person team handling HR, finance, marketing, and administration | Recruiting, payroll, billing, proposals, facilities |
| A6 | Enterprise Clients | User Class | 45 ongoing client relationships with Fortune 500 companies | Project scopes, data security requirements, procurement processes |
| A7 | Change Champions Network | Role | Cross-functional group of 12 transformation advocates (to be formed) | Adoption support, feedback collection, peer training |
| A8 | External Partners | Organization | Technology vendors, implementation partners, training providers | Software licensing, implementation services, ongoing support |

### Actor Definitions

#### A1: Managing Partner Committee

The MPC consists of three equity partners who collectively own 60% of the firm. They meet weekly on operational matters and quarterly on strategic planning. Average tenure is 22 years. Technology decisions historically have been reactive and underfunded. The committee has approved this transformation initiative with a \$2.5M budget over 24 months.

#### A2: Practice Area Leaders

Six practice leaders manage industry verticals (Financial Services, Healthcare, Technology) and functional capabilities (Strategy, Operations, People & Organization). They control staffing decisions for their teams and maintain key client relationships. Technology adoption varies significantly—Healthcare practice uses some modern tools while Financial Services relies on legacy spreadsheets.

#### A3: IT Department

A small team led by the IT Director (15-year tenure) manages on-premises infrastructure, desktop support, and vendor relationships. Current focus is "keeping the lights on" with minimal capacity for strategic initiatives. The team lacks cloud architecture skills and modern development practices. Budget has been flat at \$350K annually for five years.

#### A4: Consultants (Staff Level)

85 consultants range from analysts (1-3 years) to senior managers (8-12 years). Utilization targets are 75% billable. Staff report frustration with document management, difficulty finding prior work products, and embarrassment when client technology exceeds firm capability. Turnover is 18% annually, partly attributed to outdated tools.

#### A5: Operations Team

Operations handles back-office functions including recruiting, HR administration, finance, billing, marketing, and facilities. Systems are siloed—separate applications for time tracking, expenses, CRM (partially adopted), and accounting. Manual reconciliation between systems consumes significant effort each month.

#### A6: Enterprise Clients

Fortune 500 clients represent 70% of revenue. These clients increasingly require: vendor security assessments, SOC 2 compliance evidence, secure file sharing, real-time project status visibility, and demonstrated data governance. Three RFPs were lost in the past year partly due to technology capability gaps.

#### A7: Change Champions Network

A network of transformation advocates will be recruited from across practices and levels. Champions receive additional training, serve as local support resources, provide feedback to the transformation team, and model desired behaviors. This actor does not yet exist but is critical for adoption.

#### A8: External Partners

Technology vendors (Microsoft, Salesforce), implementation partners (consulting firms specializing in technology deployment), and training providers will be engaged. Current vendor relationships are transactional; strategic partnerships for transformation require development.

## Resources

The following resources have been identified within the survey scope.

| ID | Name | Type | Description | Status |
|----|------|------|-------------|--------|
| R1 | On-Premises Email (Exchange 2016) | Technology | Self-hosted email with 500GB total storage, no mobile optimization | Active - End of extended support 2025, security risk |
| R2 | Shared Network Drives | Infrastructure | Windows file servers at each office, VPN for remote access | Active - Disorganized, slow over VPN, no version control |
| R3 | Legacy CRM (ACT!) | Technology | Contact database used by 30% of firm, data quality issues | Partial - Incomplete data, poor adoption, no integration |
| R4 | Time & Expense System | Technology | Desktop application (Deltek Vision), manual entry, month-end processing | Active - No mobile, delayed billing, reconciliation burden |
| R5 | Accounting System | Technology | QuickBooks Enterprise, managed by Operations | Active - Not integrated, manual journal entries from billing |
| R6 | Headquarters Office | Infrastructure | 15,000 sq ft, 80 workstations, server room, conference facilities | Active - Lease renewal 2027, considering space reduction |
| R7 | Regional Offices (3) | Infrastructure | Smaller offices (10-25 people each), basic IT, limited conference facilities | Active - High real estate cost relative to utilization |
| R8 | Knowledge Repository | Process | Informal collection of templates, prior deliverables on shared drives | Degraded - Difficult to search, outdated, incomplete |
| R9 | Client Data | Information | Confidential client documents, financial models, strategic plans | Active - Scattered storage, inconsistent protection, audit risk |

### Resource Definitions

#### R1: On-Premises Email (Exchange 2016)

Email runs on physical servers at headquarters with disaster recovery at a colocation facility. Microsoft extended support ended October 2025, creating security exposure. Mobile access is limited; staff use personal email accounts for convenience. Storage quotas force deletion of older messages.

#### R2: Shared Network Drives

Each office has local file servers with folder structures that evolved organically. Cross-office file access requires VPN, which is slow and unreliable. No consistent naming conventions, folder structures vary by practice, and version control is manual ("Final_v3_REAL_Final.pptx"). Staff estimate 30 minutes daily searching for files.

#### R3: Legacy CRM (ACT!)

The firm purchased ACT! in 2008 but adoption stalled. Marketing maintains it for mailing lists; some partners track contacts; most consultants ignore it entirely. Data is incomplete and stale. No integration with other systems; duplicate entry common.

#### R4: Time & Expense System

Deltek Vision handles time entry, expense reporting, and billing. The system is powerful but underutilized—only basic features are configured. Time entry occurs weekly (policy) but often monthly (practice), delaying project profitability visibility. Expense reconciliation is manual.

#### R5: Accounting System

QuickBooks Enterprise handles general ledger, accounts payable, and financial reporting. Data flows one-way from billing system via manual journal entries. Month-end close takes 10 business days. No real-time financial visibility. Audit preparation is labor-intensive.

#### R6: Headquarters Office

The main office houses 80 of 150 staff including all support functions. The server room requires ongoing facilities investment. Space utilization has dropped to 60% with increased remote work post-pandemic. Lease renewal decision in 2027 creates opportunity to rethink physical footprint.

#### R7: Regional Offices

Three regional offices provide local presence for client relationships. Utilization is 40-50% on average days. Each office has basic IT infrastructure that is expensive to maintain per-capita. Staff increasingly question the need for permanent physical presence.

#### R8: Knowledge Repository

Prior client deliverables, methodology templates, and training materials exist but are scattered across shared drives, partner laptops, and email archives. Finding relevant prior work requires asking colleagues who might know. New consultants struggle to ramp up. Institutional knowledge walks out the door with departing staff.

#### R9: Client Data

Client data includes confidential strategic documents, financial models, market analyses, and interview notes. Data resides on shared drives, laptops, email, and occasionally personal cloud storage. No data classification scheme. Retention policies are informal. Client security questionnaires reveal gaps.

## Relationships

The following relationships connect actors and resources within the survey scope.

| ID | Source | Target | Type | Description |
|----|--------|--------|------|-------------|
| REL1 | A4 (Consultants) | R2 (Shared Drives) | depends-on | Daily work product storage and retrieval |
| REL2 | A4 (Consultants) | R8 (Knowledge Repository) | depends-on | Reference prior work for new engagements |
| REL3 | A6 (Enterprise Clients) | R9 (Client Data) | owns | Client data belongs to clients, firm is custodian |
| REL4 | A3 (IT) | R1 (Email) | maintains | IT responsible for email availability and security |
| REL5 | A3 (IT) | R2 (Shared Drives) | maintains | IT responsible for file server operations |
| REL6 | A5 (Operations) | R4 (Time System) | operates | Operations administers time and billing |
| REL7 | A5 (Operations) | R5 (Accounting) | operates | Operations manages financial systems |
| REL8 | A1 (MPC) | A2 (Practice Leaders) | directs | MPC sets strategy, practice leaders execute |
| REL9 | A2 (Practice Leaders) | A4 (Consultants) | manages | Practice leaders supervise consultant work |
| REL10 | A2 (Practice Leaders) | A6 (Clients) | serves | Practice leaders own client relationships |
| REL11 | A4 (Consultants) | A6 (Clients) | delivers-to | Consultants execute client work |
| REL12 | A8 (External Partners) | A3 (IT) | supports | Vendors provide technology and services |
| REL13 | A7 (Change Champions) | A4 (Consultants) | influences | Champions drive peer adoption |
| REL14 | A1 (MPC) | R6 (HQ Office) | controls | MPC makes real estate decisions |
| REL15 | A4 (Consultants) | R1 (Email) | depends-on | Primary communication channel |
| REL16 | A6 (Clients) | R1 (Email) | receives-from | Client communication via email |
| REL17 | A3 (IT) | R7 (Regional Offices) | maintains | IT supports regional infrastructure |
| REL18 | A5 (Operations) | R3 (CRM) | operates | Operations nominally owns CRM |

## Constraints and Boundaries

### In Scope

- All firm technology systems and infrastructure
- Business processes across all functions
- Workforce capabilities, skills, and change readiness
- Organizational culture and governance
- Client-facing capabilities and requirements
- Four physical locations and real estate considerations

### Out of Scope

- Client internal systems (though integration points are in scope)
- Detailed practice methodologies (content, not systems)
- Individual client relationships (aggregated as user class)
- Legal entity structure (will remain unchanged)

### Constraints

| Constraint | Source | Impact |
|------------|--------|--------|
| Budget ceiling \$2.5M | MPC authorization | Limits scope; prioritization required |
| 24-month timeline | MPC expectation | Phased approach necessary |
| No forced redundancies | Partnership agreement | Transformation must redeploy, not reduce |
| SOC 2 Type II requirement | Enterprise client RFPs | Security/compliance features mandatory |
| Billable utilization targets | Financial model | Training must minimize productivity impact |
| Partner autonomy culture | Organizational history | Cannot mandate; must persuade adoption |

## Current State Assessment

### Pain Points

| Area | Pain Point | Business Impact | Severity |
|------|------------|-----------------|----------|
| Document Management | File search wastes 30 min/day per consultant | \$800K annual productivity loss | High |
| Knowledge Management | New consultants take 6 months to become productive | Extended ramp time, quality risk | High |
| Client Perception | Lost 3 RFPs citing technology gaps | \$2M+ lost revenue opportunity | High |
| Security Posture | Cannot pass enterprise security assessments | Limits addressable market | High |
| Email System | End of support, mobile limitations | Security risk, productivity loss | Medium |
| Remote Collaboration | VPN slow, tools fragmented | Hybrid work friction | Medium |
| Financial Visibility | Month-end close takes 10 days | Delayed decisions | Medium |
| CRM Data Quality | 70% of firm doesn't use CRM | Pipeline invisibility | Medium |

### Readiness Assessment

| Dimension | Current State | Readiness | Notes |
|-----------|---------------|-----------|-------|
| Executive Sponsorship | MPC approved budget | High | Active engagement needed to sustain |
| Change Capacity | No recent major changes | Medium | Organization has capacity but no muscle |
| Technical Foundation | Legacy, fragmented | Low | Significant investment required |
| Skills | Traditional consulting skills | Medium | Digital skills gap, learning needed |
| Culture | Partner autonomy, relationship-based | Low | Transformation requires culture shift |
| Financial Resources | \$2.5M approved | Medium | Adequate for Phase 1; Phase 2 TBD |

## Recommendations for Architecture

Based on this survey, the architecture phase should consider:

1. **Cloud-First Strategy:** On-premises infrastructure is unsustainable; migrate to cloud services (Microsoft 365, Azure) for email, collaboration, and infrastructure

2. **Unified Platform Approach:** Reduce system fragmentation through integrated platform (Microsoft ecosystem provides email, files, Teams, SharePoint, Power Platform)

3. **Knowledge Management Priority:** Capture institutional knowledge before partner retirements; implement searchable repository early

4. **Security by Design:** Build SOC 2 compliance into architecture from start, not as afterthought

5. **Change Management Investment:** 20-25% of budget should support adoption through Champions network, training, and communication

6. **Phased Migration:** Sequence changes to manage disruption; email/collaboration first (visible wins), then back-office integration

7. **Real Estate Integration:** Use transformation to enable space reduction; factor savings into business case

---

**Note:** This field survey was created as part of a runbook demonstration. In production, this survey would be validated by firm leadership and subject matter experts before informing architecture decisions.
