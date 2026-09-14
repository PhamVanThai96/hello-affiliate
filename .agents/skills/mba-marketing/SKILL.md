---
name: mba-marketing
description: >-
  Provides strategic business administration (MBA) frameworks integrated with high-conversion Content Marketing execution.
  Use this skill whenever the user requests: business model diagnostics, corporate strategy (PESTEL, Porter, Blue Ocean, VRIO, BSC),
  financial and unit economics modeling (CLV, CAC, WACC, NPV, Break-Even CVP, Working Capital CCC), pricing strategy design,
  content marketing architecture (3H mix, Content Pillars, Topic Clusters, Buyer Persona, 5A Journey Map),
  high-conversion copywriting (AIDA, PAS, FAB, StoryBrand SB7), short-form video optimization (Hook-Body-CTA pacing & scoring),
  SEO/GEO search optimization, or SME operations and startup failure autopsy.
---

# MBA & Content Marketing Strategic Intelligence Skill

This skill equips the agent with executive-level corporate management acumen combined with tactical, machine-speed content marketing execution. It bridges the gap between high-level business mechanics (Finance, Strategy, Operations) and ground-level customer acquisition (Copywriting, Video Physics, Funnel Architecture).

---

## 1. Quick Reference & Reference Directory

All specialized reference documents are stored under `./references/` and should be consulted via progressive disclosure:

| Domain | Key Reference Files | When to Read |
|---|---|---|
| **Master Index & Logic** | [00_ONTOLOGY_INDEX.json](./references/00_ONTOLOGY_INDEX.json)<br>[01_HEURISTICS_ENGINE.json](./references/01_HEURISTICS_ENGINE.json)<br>[cross_domain_synthesis.md](./references/cross_domain_synthesis.md) | For concept graph lookup, IF-THEN decision rules, and cross-domain synergy analysis |
| **Quantitative Formulations** | [02_QUANTITATIVE_FORMULAS.json](./references/02_QUANTITATIVE_FORMULAS.json) | For exact formulas, variable units, and financial/marketing benchmark thresholds |
| **Content Foundations & 3 Layers** | [01_core_foundations.yaml](./references/content_marketing/01_core_foundations.yaml) | For product value decomposition (Functional, Emotional, Symbolic) and audience matching |
| **Strategy, 3H & Clusters** | [02_strategy_architectures.yaml](./references/content_marketing/02_strategy_architectures.yaml) | For 3H volume allocation, Content Pillars, Topic Clusters, and 5A Journey Mapping |
| **Copywriting & Video Scripts** | [03_copywriting_creation.yaml](./references/content_marketing/03_copywriting_creation.yaml) | For PAS/FAB/AIDA/SB7 copywriting and 0-3s hook / 3-15s retain video pacing |
| **SEO, GEO & Repurposing** | [04_seo_geo_distribution.yaml](./references/content_marketing/04_seo_geo_distribution.yaml) | For Search Intent, On-Page SEO, GEO (LLM citations), and 1-to-10 repurposing algorithms |
| **Analytics & Optimization** | [05_analytics_optimization.yaml](./references/content_marketing/05_analytics_optimization.yaml) | For Funnel KPIs, GA4 attribution models, and content decay audit matrices |
| **AI Workflows & Prompts** | [06_ai_workflows_prompts.yaml](./references/content_marketing/06_ai_workflows_prompts.yaml) | For prompt engineering frameworks (RTF/CREATE) and 5-agent production pipelines |
| **MBA Strategy & Models** | [01_strategic_management.yaml](./references/mba_management/01_strategic_management.yaml) | For PESTEL, Porter's 5 Forces, VRIO, BCG, Ansoff, Blue Ocean ERRC, and Balanced Scorecards |
| **MBA Marketing & Pricing** | [02_marketing_management.yaml](./references/mba_management/02_marketing_management.yaml) | For STP Engine, 4P/7P/4C mix, 10 Pricing models, Keller CBBE, and Behavioral Nudges |
| **Corporate Finance & Valuation**| [03_corporate_finance.yaml](./references/mba_management/03_corporate_finance.yaml) | For TVM, Capital Budgeting (NPV/IRR), WACC, MM Capital Structure, CCC, and DCF Valuation |
| **Managerial Accounting & CVP**  | [04_accounting_control.yaml](./references/mba_management/04_accounting_control.yaml) | For Break-Even (BEP), CVP analysis, ABC costing, Variance analysis, and 25+ Financial Ratios |
| **Organizational Behavior**      | [05_organizational_behavior.yaml](./references/mba_management/05_organizational_behavior.yaml)| For Motivation (Herzberg/SDT), Situational Leadership, Tuckman stages, and Kotter 8-step change |
| **Operations Research & SCM**   | [06_operations_supply_chain.yaml](./references/mba_management/06_operations_supply_chain.yaml)| For Little's Law, Theory of Constraints (TOC), Lean TIMWOODS, DMAIC, and EOQ inventory |
| **SME 0-to-1 Operations**        | [07_sme_operations_playbook.yaml](./references/mba_management/07_sme_operations_playbook.yaml)| For SME cash runway survival, F&B/Retail unit benchmarks, and software stack selection |
| **Case Autopsies**               | [08_case_autopsies.yaml](./references/mba_management/08_case_autopsies.yaml) | For strategic/financial post-mortems of Soya Garden, Mixue, Bách Hóa Xanh, VinFast, 7-Eleven, Coffee House, and 20+ strategic framework cases |
| **Real Estate Valuation**         | [01_valuation_and_market_knowledge.yaml](./references/real_estate/01_valuation_and_market_knowledge.yaml) | For property valuation methods, market cycle analysis, legal/planning checks, investment return metrics (VN market) |
| **Real Estate Action Playbook**   | [02_action_playbook.yaml](./references/real_estate/02_action_playbook.yaml) | For phase-gated investment roadmap, due diligence protocol, transaction execution checklist |
| **Affiliate Ads Campaign Logic**  | [01_campaign_and_landing_page_playbook.yaml](./references/affiliate_ads/01_campaign_and_landing_page_playbook.yaml) | For Google Ads campaign planning rules, keyword analysis logic, landing page scoring criteria |

---

## 2. Standard Operating Procedures (Agent Runbooks)

When addressing a user inquiry, follow this 4-phase structured workflow:

### Phase 1: Strategic Diagnostic & Context Framing
1. Identify the core domain and industry context.
2. Query [01_HEURISTICS_ENGINE.json](./references/01_HEURISTICS_ENGINE.json) to locate applicable strategic rules.
3. If addressing a macro competitive challenge:
   - Evaluate external headwinds using **PESTEL** and **Porter's 5 Forces**.
   - Audit internal defensibility using **VRIO** (check if advantage is merely temporary).
   - Use **Blue Ocean ERRC Grid** to break out of red ocean price wars.

### Phase 2: Quantitative Modeling & Economic Boundaries
1. Always compute unit economics before proposing marketing budgets:
   - Calculate Unit Contribution Margin: `CM = Price - Variable_Cost`.
   - Set the hard ceiling: `Allowable CAC <= CM * Safety_Margin`.
   - Verify health ratio: `CLV / CAC >= 3.0` and `Payback Period <= 12 months`.
2. For operational or financial calculations, run the automated CLI tool:
   ```bash
   # Calculate Break-Even Point (CVP)
   python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py bep --fixed-costs [FC] --price [P] --variable-cost [VC]

   # Calculate Customer Lifetime Value (CLV)
   python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py clv --arpu [ARPU] --margin [Margin] --churn [Churn]

   # Calculate Cost of Capital (WACC)
   python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py wacc --equity [E] --debt [D] --ke [Ke] --kd [Kd]

   # Calculate Cash Conversion Cycle (CCC)
   python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py ccc --dio [DIO] --dso [DSO] --dpo [DPO]

   # Calculate Video Quality Score
   python3 .agents/skills/mba-marketing/scripts/calculate_metrics.py video-score --engage [Score] --growth [Score] --retention [Score]
   ```

### Phase 3: Content Marketing Architecture & Funnel Deployment
1. **Deconstruct Product Value (Three Layers)**:
   - Functional (Physical specs) -> Emotional (Relief & satisfaction) -> Symbolic (Identity & status).
2. **Structure the Content Mix (3H Framework)**:
   - **Hero (10-15%)**: Major launches, emotional films, large-scale virality.
   - **Hub (50-60%)**: Recurring series, podcasts, community engagement, brand voice.
   - **Help/Hygiene (25-30%)**: Evergreen SEO, tutorials, troubleshooting, FAQs.
   - **Buffer (10-15%)**: Real-time trend capitalization & newsjacking.
3. **Select the Persuasion Copywriting Engine**:
   - `PAS` for acute problem-solving / pain-relief products.
   - `FAB` for technical features and specs-heavy consumer goods.
   - `StoryBrand SB7` for high-ticket services and brand transformation journeys.
4. **Short-Video Engineering (TikTok / Reels)**:
   - Enforce 4-tier timeline pacing: Hook (0-3s) -> Retention Setup (3-15s) -> Core Value (15-45s) -> Frictionless CTA (45-60s).
   - Target benchmark: 3s Stop Rate `> 65%`, Completion Rate `> 25%`.

### Phase 4: Operational Flow & Bottleneck Elimination
1. Apply **Little's Law** to content editorial pipelines: `WIP = Throughput * Flow Time`.
   - Always recommend capping Work-In-Progress (WIP) on the Kanban board to accelerate publishing speed.
2. Apply **Theory of Constraints (TOC)**:
   - Protect the bottleneck station (e.g. video editor or expert review) with an upstream buffer.
3. Implement **1-to-10 Content Repurposing**:
   - Deconstruct 1 master pillar asset into 10 atomic distribution formats to drive marginal distribution cost to zero.

---

## 3. Heuristic Rules of Thumb for Common Dilemmas

- **If an SME has < 3 months of cash runway:** Freeze Capex, renegotiate supplier credit (extend DPO), liquidate slow inventory (compress DIO), and pivot content entirely to high-margin BOFU cash conversion.
- **If TikTok video retention drops sharply in first 3 seconds:** Delete channel logos/intros; replace with visual pattern interrupt and contrarian curiosity hook within 0.5 seconds.
- **If customer acquisition costs (CAC) are rising:** Stop expanding paid ad spend; shift budget into building Evergreen Topic Clusters for organic SEO and GEO (Generative Engine Optimization).
- **If team conflicts arise during scaling:** Diagnose using Lencioni's 5 Dysfunctions (start by establishing vulnerability-based trust before forcing accountability).
