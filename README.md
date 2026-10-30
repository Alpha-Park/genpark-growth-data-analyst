# genpark-growth-data-analyst

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Growth Data Analyst is a zero-dependency SaaS product analytics and retention econometrics engine implementing cohort retention triangle heatmaps, bivariate Granger causality F-tests on feature adoption, and discrete Kaplan-Meier churn hazard rate estimations.

```mermaid
flowchart TD
    A[User Birth Cohort Events] --> B[Retention Triangle Matrix Generator]
    B --> C[Empirical SaaS Retention Curve]
    D[Feature Adoption & Retention Series] --> E[Granger Causality F-Test]
    E --> F[Causal Significance & Impact Verdict]
    G[Customer Lifespan & Churn Event Stream] --> H[Hazard Rate & Survival Function]
    H --> I[Critical Retention Intervention Window]
```

## Features
- **Cohort Retention Triangles**: Calculates multi-period retention matrices and average longitudinal survival curves.
- **Granger Causality Testing**: Computes F-statistics to rigorously verify whether feature adoption causes retention gains.
- **Churn Hazard Inflection**: Pinpoints exact customer drop-off days to trigger proactive customer success playbooks.

## Quickstart

```python
from client import GenParkGrowthDataAnalyst

analyst = GenParkGrowthDataAnalyst()
cohorts = [{"cohort": "2026-01", "cohort_size": 100, "active_users": [100, 50, 40]}]
res = analyst.build_cohort_retention_triangle(cohorts)
print("Avg Retention:", res["average_retention_curve_pct"])
```

## License
MIT
