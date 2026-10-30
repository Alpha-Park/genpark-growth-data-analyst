# -*- coding: utf-8 -*-
"""
GenPark Growth Data Analyst FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkGrowthDataAnalyst

mcp = FastMCP("genpark-growth-data-analyst")
analyst = GenParkGrowthDataAnalyst()

@mcp.tool()
def build_cohort_retention_triangle(cohort_events_json: str) -> str:
    """
    Builds standard SaaS cohort retention triangle matrix.
    """
    events = json.loads(cohort_events_json)
    res = analyst.build_cohort_retention_triangle(events)
    return json.dumps(res, indent=2)

@mcp.tool()
def test_feature_adoption_granger_causality(
    feature_adoption_series_json: str,
    retention_series_json: str,
    lag_p: int = 2
) -> str:
    """
    Conducts bivariate Granger Causality test to determine whether feature adoption Granger-causes retention.
    """
    f = json.loads(feature_adoption_series_json)
    r = json.loads(retention_series_json)
    res = analyst.test_feature_adoption_granger_causality(f, r, lag_p)
    return json.dumps(res, indent=2)

@mcp.tool()
def estimate_churn_hazard_rate_cox(
    customer_lifespans_days_json: str,
    churned_flags_json: str
) -> str:
    """
    Estimates discrete hazard rate and median survival lifespan.
    """
    lifespans = json.loads(customer_lifespans_days_json)
    flags = json.loads(churned_flags_json)
    res = analyst.estimate_churn_hazard_rate_cox(lifespans, flags)
    return json.dumps(res, indent=2)

def main():
    print("Testing Growth Data Analyst:")
    c = [{"cohort": "2026-01", "cohort_size": 100, "active_users": [100, 45, 35]}]
    print(build_cohort_retention_triangle(json.dumps(c)))

if __name__ == "__main__":
    main()
