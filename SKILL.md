---
name: genpark-growth-data-analyst
description: Comprehensive account health monitoring, providing executive summaries and identifying high-leverage growth opportunities.
---

# GenPark Growth Data Analyst

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Overview
This skill acts as a fractional Head of Growth. It ingests vast amounts of campaign data and outputs concise, executive-level insights, highlighting exactly what is working, what is broken, and what actions have the highest potential upside.

## Capabilities
- **Account Health Summarization**: Calculates blended CPA, overall ROAS, and total conversion velocity, comparing against prior periods (e.g., vs last week).
- **Opportunity Identification**: Pinpoints specific actions that will move the needle (e.g., "Meta is underweighted", "Google bids need adjustment").
- **Impact Forecasting**: When asked "If we act on these, what's the upside?", the agent uses historical data to project the impact of suggested changes.

## Usage Instructions
1. Feed the agent the latest performance export or connect it to the live data warehouse.
2. Request a "Daily Health Check".
3. The agent will respond with a prioritized list of insights and a recommended "Sprint Plan".
