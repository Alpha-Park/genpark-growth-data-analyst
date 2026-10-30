# -*- coding: utf-8 -*-
import json
from client import GenParkGrowthDataAnalyst

analyst = GenParkGrowthDataAnalyst()

# 1. Cohort Retention Triangle Matrix
cohorts = [
    {"cohort": "2026-01", "cohort_size": 1200, "active_users": [1200, 610, 480, 420, 390]},
    {"cohort": "2026-02", "cohort_size": 1500, "active_users": [1500, 780, 630, 560]},
    {"cohort": "2026-03", "cohort_size": 1800, "active_users": [1800, 950, 790]}
]
triangle = analyst.build_cohort_retention_triangle(cohorts)
print(f"Cohort Retention Triangle: {triangle['total_cohorts']} Cohorts (Benchmark M1: {triangle['day_30_retention_benchmark']}%)")
for c in triangle["cohort_retention_matrix"]:
    print(f"  {c['cohort']} ({c['cohort_size']} users): {c['retention_rates_pct']}")
print(f"  Avg Retention Curve: {triangle['average_retention_curve_pct']}")

# 2. Granger Causality Feature Adoption Test
feature_adoption = [15.0, 22.0, 35.0, 48.0, 65.0, 72.0, 85.0, 92.0, 96.0, 98.0]
retention = [42.0, 44.0, 48.0, 53.0, 59.0, 64.0, 70.0, 74.0, 77.0, 79.0]
granger = analyst.test_feature_adoption_granger_causality(feature_adoption, retention, lag_p=2)
print()
print(f"Granger Causality Test: F-Stat={granger['f_statistic']} | Causes Retention: {granger['granger_causes_retention']} ({granger['causal_strength']})")
print(f"  Implication: {granger['strategic_implication']}")

# 3. Kaplan-Meier Churn Hazard Rate Curve
lifespans = [5, 12, 14, 25, 30, 45, 60, 90, 120, 180, 240, 365]
churned = [True, True, True, True, True, True, False, True, False, True, False, False]
hazard = analyst.estimate_churn_hazard_rate_cox(lifespans, churned)
print()
print(f"Hazard Rate: Peak Hazard at Day {hazard['peak_hazard_day_checkpoint']} (Rate: {hazard['peak_hazard_rate']})")
print(f"  Critical Window: {hazard['critical_intervention_window']}")
