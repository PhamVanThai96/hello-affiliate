#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MBA & Marketing Quantitative Calculator CLI
Helper utility for the mba-marketing skill.
Calculates key financial, operational, and marketing metrics accurately based on standardized formulas.
"""

import sys
import math
import argparse
import json


def calc_clv(arpu, gross_margin_pct, churn_rate):
    """Customer Lifetime Value: (ARPU * Gross_Margin_Pct) / Churn_Rate"""
    if churn_rate <= 0:
        raise ValueError("Churn rate must be > 0")
    clv = (arpu * gross_margin_pct) / churn_rate
    return {"clv": round(clv, 2), "formula": "(ARPU * Gross_Margin) / Churn_Rate"}


def calc_bep(fixed_costs, price, variable_cost):
    """Break-even point in units and revenue."""
    cm = price - variable_cost
    if cm <= 0:
        raise ValueError("Price must be greater than Variable Cost per unit")
    cm_ratio = cm / price
    bep_units = fixed_costs / cm
    bep_revenue = fixed_costs / cm_ratio
    return {
        "unit_contribution_margin": round(cm, 2),
        "contribution_margin_ratio": round(cm_ratio, 4),
        "break_even_units": math.ceil(bep_units),
        "break_even_revenue": round(bep_revenue, 2)
    }


def calc_wacc(equity_val, debt_val, cost_equity, cost_debt_pretax, tax_rate):
    """Weighted Average Cost of Capital (WACC)."""
    total_val = equity_val + debt_val
    if total_val <= 0:
        raise ValueError("Total Capital (Equity + Debt) must be > 0")
    we = equity_val / total_val
    wd = debt_val / total_val
    cost_debt_after_tax = cost_debt_pretax * (1 - tax_rate)
    wacc = (we * cost_equity) + (wd * cost_debt_after_tax)
    return {
        "weight_equity": round(we, 4),
        "weight_debt": round(wd, 4),
        "cost_debt_after_tax": round(cost_debt_after_tax, 4),
        "wacc": round(wacc, 4),
        "wacc_percent": f"{round(wacc * 100, 2)}%"
    }


def calc_ccc(dio, dso, dpo):
    """Cash Conversion Cycle: DIO + DSO - DPO."""
    ccc = dio + dso - dpo
    return {
        "cash_conversion_cycle_days": round(ccc, 1),
        "interpretation": "Negative CCC means operations are financed via supplier float (advantageous)." if ccc < 0 else "Positive CCC requires working capital financing."
    }


def calc_littles_law(throughput, flow_time):
    """Little's Law: WIP = Throughput * Flow Time."""
    wip = throughput * flow_time
    return {
        "wip": round(wip, 2),
        "formula": "WIP = Throughput * Flow_Time",
        "guidance": "To compress Flow Time without reducing Throughput, you MUST cap and reduce WIP."
    }


def calc_video_score(engage_score, growth_score, retention_score):
    """Video Composite Score: 0.35 * Engage + 0.10 * Growth + 0.55 * Retention."""
    composite = (0.35 * engage_score) + (0.10 * growth_score) + (0.55 * retention_score)
    classification = "Viral / Top Performer (Scale & Replicate)" if composite >= 80 else ("Standard / Healthy Performance" if composite >= 60 else "Underperforming (Refactor Hook & Pacing)")
    return {
        "composite_score": round(composite, 2),
        "classification": classification
    }


def main():
    parser = argparse.ArgumentParser(description="MBA & Marketing Quantitative Metric Engine")
    subparsers = parser.add_subparsers(dest="command", help="Available calculation commands")

    # CLV
    p_clv = subparsers.add_parser("clv", help="Calculate Customer Lifetime Value")
    p_clv.add_argument("--arpu", type=float, required=True, help="Average Revenue Per User per month")
    p_clv.add_argument("--margin", type=float, required=True, help="Gross Margin % (e.g. 0.65)")
    p_clv.add_argument("--churn", type=float, required=True, help="Monthly churn rate % (e.g. 0.05)")

    # BEP
    p_bep = subparsers.add_parser("bep", help="Calculate Break-Even Point (CVP)")
    p_bep.add_argument("--fixed-costs", type=float, required=True, help="Total Fixed Costs")
    p_bep.add_argument("--price", type=float, required=True, help="Selling Price per unit")
    p_bep.add_argument("--variable-cost", type=float, required=True, help="Variable Cost per unit")

    # WACC
    p_wacc = subparsers.add_parser("wacc", help="Calculate Cost of Capital (WACC)")
    p_wacc.add_argument("--equity", type=float, required=True, help="Market Value of Equity")
    p_wacc.add_argument("--debt", type=float, required=True, help="Market Value of Debt")
    p_wacc.add_argument("--ke", type=float, required=True, help="Cost of Equity % (e.g. 0.14)")
    p_wacc.add_argument("--kd", type=float, required=True, help="Pre-tax Cost of Debt % (e.g. 0.08)")
    p_wacc.add_argument("--tax-rate", type=float, default=0.20, help="Corporate Tax Rate (default 0.20)")

    # CCC
    p_ccc = subparsers.add_parser("ccc", help="Calculate Cash Conversion Cycle")
    p_ccc.add_argument("--dio", type=float, required=True, help="Days Inventory Outstanding")
    p_ccc.add_argument("--dso", type=float, required=True, help="Days Sales Outstanding")
    p_ccc.add_argument("--dpo", type=float, required=True, help="Days Payable Outstanding")

    # Little's Law
    p_little = subparsers.add_parser("littles-law", help="Calculate WIP using Little's Law")
    p_little.add_argument("--throughput", type=float, required=True, help="Production/Departure rate per time unit")
    p_little.add_argument("--flow-time", type=float, required=True, help="Lead time from entry to completion")

    # Video score
    p_video = subparsers.add_parser("video-score", help="Calculate Short-form Video Quality Composite Score")
    p_video.add_argument("--engage", type=float, required=True, help="Engagement sub-score (0-100)")
    p_video.add_argument("--growth", type=float, required=True, help="Growth/Follow sub-score (0-100)")
    p_video.add_argument("--retention", type=float, required=True, help="Retention/Watch-time sub-score (0-100)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "clv":
            res = calc_clv(args.arpu, args.margin, args.churn)
        elif args.command == "bep":
            res = calc_bep(args.fixed_costs, args.price, args.variable_cost)
        elif args.command == "wacc":
            res = calc_wacc(args.equity, args.debt, args.ke, args.kd, args.tax_rate)
        elif args.command == "ccc":
            res = calc_ccc(args.dio, args.dso, args.dpo)
        elif args.command == "littles-law":
            res = calc_littles_law(args.throughput, args.flow_time)
        elif args.command == "video-score":
            res = calc_video_score(args.engage, args.growth, args.retention)
        else:
            res = {"error": "Unknown command"}

        print(json.dumps(res, indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
