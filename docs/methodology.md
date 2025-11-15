# Methodology - How Domains Are Ranked

This document explains how the Top 100 Million Domains list is created and maintained.

## Overview

Our ranking system uses a proprietary WebL Site Authority algorithm that combines multiple data sources and signals to create the most comprehensive domain quality ranking available.

## Data Sources

Our ranking system combines multiple proprietary and public data sources to create the most accurate site authority scores.

### 1. Internal Domain Intelligence (Primary)

Our core ranking signals come from proprietary domain intelligence systems:

**Domain Registration Data:**
- Registration dates and domain age
- WHOIS history and patterns
- Registrar quality signals
- Registration stability metrics

**Web Presence Analysis:**
- Traffic patterns and trends
- User engagement signals
- Brand recognition scores
- Search engine visibility
- Social media authority

**Quality Indicators:**
- Content freshness and update frequency
- Site architecture and technical quality
- Mobile responsiveness
- Security certificates (HTTPS)
- Page load performance
- Trust and safety signals

### 2. Public Data Sources

We supplement our proprietary data with select public sources:

**Common Crawl Web Graphs:**
[Common Crawl](https://commoncrawl.org/) provides valuable web graph data that helps validate and enhance our rankings:
- Link relationships between domains
- Web crawl patterns
- Backlink profiles
- Historical web data

**RDAP (Registration Data Access Protocol):**
- Domain registration dates
- Registrar information
- Public WHOIS data

### 3. Historical Performance Tracking

Our systems continuously monitor domain performance to identify:
- Long-term authority trends
- Seasonal patterns
- Growth trajectories
- Stability indicators

## Ranking Algorithm

Our WebL Site Authority (WSA) score is calculated using a multi-factor algorithm:

### Core Components

**1. Link Equity Score**
- Primary ranking factor based on proprietary web graph analysis
- Validated against public data sources
- Uses modified PageRank algorithm
- Considers both quantity and quality of backlinks
- Discounts low-quality and spam links

**2. Domain Age Bonus**
- Older domains receive higher scores
- Non-linear scaling (diminishing returns after 10 years)
- Registration date verified through multiple sources
- Significant boost for established domains

**3. Web Presence Score**
- Traffic estimates and trends
- Engagement signals
- Brand recognition metrics
- Social media authority

**4. Trust Signals**
- HTTPS adoption
- Security practices
- Content quality indicators
- User trust metrics

### Scoring Scale

WebL Site Authority (WSA) scores range from **0 to 1000**:

- **900-1000**: Top tier (Google, Facebook, YouTube level)
- **700-899**: Major brands and platforms
- **500-699**: Established authority sites
- **300-499**: Growing sites with authority
- **100-299**: Emerging sites
- **0-99**: New or low-authority domains

### Normalization Process

1. Raw scores calculated for all domains
2. Scores normalized to 0-1000 scale
3. Logarithmic scaling applied (similar to Richter scale)
4. Top rankings receive disproportionate weight

This means a domain with WSA 900 has significantly more authority than WSA 800 (not just 12.5% more).

## Data Processing Pipeline

### Monthly Update Cycle

**Week 1: Data Collection**
1. Gather data from proprietary sources
2. Update internal quality signals
3. Fetch latest public data (RDAP, Common Crawl, etc.)
4. Collect traffic and engagement metrics

**Week 2: Processing**
1. Process 100M+ domains through ranking pipeline
2. Calculate proprietary authority scores
3. Compute domain age and trust bonuses
4. Integrate multi-source quality signals

**Week 3: Ranking**
1. Apply scoring algorithm
2. Normalize to 0-1000 scale
3. Sort by final DA score
4. Generate subset files

**Week 4: Validation & Release**
1. Quality checks and anomaly detection
2. Compare with previous month's data
3. Validate top 1000 manually
4. Publish updated lists

## Quality Assurance

### Automated Checks

- **Consistency validation**: Ensure ranks don't fluctuate wildly
- **Outlier detection**: Flag suspicious jumps in ranking
- **Duplicate detection**: Remove duplicate domains
- **Format validation**: Ensure clean CSV output

### Manual Review

- Top 1000 domains reviewed for accuracy
- Major ranking changes investigated
- Brand name verification
- Spam and low-quality domain filtering

## Limitations

### What This List Does NOT Include

- **Real-time data**: Updates are monthly, not daily
- **Private metrics**: We can't access analytics, exact traffic numbers
- **Social media followers**: Not directly measured
- **Revenue data**: Financial information not included
- **Subjective quality**: Can't measure content quality perfectly

### Known Biases

- **English language bias**: Common Crawl skews toward English sites
- **Commercial bias**: Business sites tend to rank higher
- **Geographic bias**: US/European sites may rank higher than equivalent Asian sites
- **Recency bias**: Newly popular sites may lag in rankings

## Transparency

While our exact algorithm is proprietary (to prevent gaming), the core principles are:

1. **Data-driven**: Based on verifiable public data
2. **Objective**: Minimal human intervention
3. **Consistent**: Same criteria applied to all domains
4. **Reproducible**: Rankings should make logical sense

## Differences from Other Rankings

### vs Alexa (Discontinued 2022)
- **More domains**: 100M vs 1M
- **Better methodology**: Web graph + multiple signals vs toolbar data
- **More transparent**: Open data sources

### vs Majestic Million
- **100x larger**: 100M vs 1M
- **More signals**: Age, trust, traffic vs just backlinks
- **Different focus**: Overall authority vs link profile only

### vs Tranco
- **Different goals**: Authority vs security/research
- **More comprehensive**: Multiple signals vs traffic proxies
- **Longer history**: More historical context

## Updates & Improvements

We continuously improve our methodology based on:
- Web ecosystem changes
- New data sources becoming available
- Community feedback
- Academic research

## Questions?

For methodology questions or suggestions:
- Open an issue: [GitHub Issues](https://github.com/websitelaunches/top-100-million-domains/issues)
- Email: domains@websitelaunches.com

---

**Last Updated**: November 2025 | [View Changelog](../CHANGELOG.md)
