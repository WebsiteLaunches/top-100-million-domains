# Top 100 Million Domains - The Internet's Most Comprehensive Site Authority List

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Updated](https://img.shields.io/badge/Updated-November%202025-brightgreen)](https://github.com/websitelaunches/top-100-million-domains)
[![Domains](https://img.shields.io/badge/Domains-100M-blue)](data/top-100m-domains.csv)

The most comprehensive, regularly updated list of the world's top 100 million domains, ranked by WebL Site Authority, age, and web presence.

**Perfect for:** SEO research, competitor analysis, domain investing, brand monitoring, machine learning, cybersecurity, and academic research.

## 🌟 What is this?

A free, open-source dataset of **100 million domains** ranked by a proprietary WebL Site Authority algorithm that combines:
- WebL Site Authority (WSA) scores (0-1000 scale)
- Domain age and registration history
- Web presence and link equity
- Traffic patterns and engagement signals

Our ranking methodology integrates domain intelligence, proprietary quality signals, and multiple data sources including [Common Crawl](https://commoncrawl.org/) web graphs.

## 📊 Quick Stats

- **Total Domains**: 100,000,000
- **Last Updated**: November 15, 2025
- **Data Sources**: Proprietary + Public Sources (incl. Common Crawl)
- **Update Frequency**: Monthly (subject to data availability)
- **License**: MIT (Free for commercial use)
- **File Size**: 1.7GB (full list)

## 🚀 Quick Start

```bash
# Download top 1,000 domains (13KB)
curl -O https://raw.githubusercontent.com/websitelaunches/top-100-million-domains/main/data/top-1k-domains.csv

# Download top 1 million domains (15MB)
curl -O https://raw.githubusercontent.com/websitelaunches/top-100-million-domains/main/data/top-1m-domains.csv
```

## 📁 Available Domain Lists

| File | Domains | Size | Best For |
|------|---------|------|----------|
| [top-100m-domains.csv](data/top-100m-domains.csv) | 100,000,000 | 1.7GB | Comprehensive analysis, AI training |
| [top-10m-domains.csv](data/top-10m-domains.csv) | 10,000,000 | 163MB | Machine learning training |
| [top-1m-domains.csv](data/top-1m-domains.csv) | 1,000,000 | 15MB | Domain investing, bulk analysis |
| [top-100k-domains.csv](data/top-100k-domains.csv) | 100,000 | 1.4MB | Market research, link building |
| [top-10k-domains.csv](data/top-10k-domains.csv) | 10,000 | 127KB | Competitor analysis, SEO benchmarking |
| [top-1k-domains.csv](data/top-1k-domains.csv) | 1,000 | 13KB | Quick reference, brand research |

## 🎯 Top 10 Domains (November 2025)

1. **google.com** - Search Engine Giant
2. **youtube.com** - Video Platform
3. **facebook.com** - Social Media
4. **amazon.com** - E-commerce Leader
5. **wikipedia.org** - Knowledge Base
6. **instagram.com** - Social Media
7. **twitter.com** - Social Media / News
8. **linkedin.com** - Professional Network
9. **reddit.com** - Community Platform
10. **netflix.com** - Streaming Service

[View full top 1000 →](data/top-1k-domains.csv)

## 💡 Use Cases

### 🔍 SEO & Competitive Research
```python
# Find where your competitors rank
import csv

competitors = ['competitor1.com', 'competitor2.com', 'competitor3.com']

with open('top-1m-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip()
        if domain in competitors:
            print(f"{domain} ranks #{rank:,} globally")
```

### 📈 Domain Investment Analysis
Identify undervalued domains by filtering the list by criteria like:
- High DA but recently dropped
- Short domains with authority
- Brandable domains in top 100k

### 🛡️ Brand Protection & Monitoring
Check if similar domains to your brand appear in the top rankings.

### 🤖 Machine Learning & AI
Use as training data for:
- Domain classification models
- Phishing detection systems
- Web scraping prioritization
- Search engine algorithms

### 📊 Market Research
Analyze domain patterns, industry trends, and web ecosystem changes.

[More use cases and examples →](docs/use-cases.md)

## 📈 Methodology

Our WebL Site Authority (WSA) scoring is calculated using:

1. **Common Crawl Web Graph Analysis**
   - Link equity and backlink profiles
   - Web crawl frequency and depth
   - Page rank algorithms

2. **Internal Domain Signals**
   - Domain age and registration history
   - Traffic patterns and engagement metrics
   - Brand recognition and trust signals
   - Historical performance data

3. **Proprietary Scoring Algorithm**
   - Combines multiple quality signals
   - Normalizes to 0-1000 scale
   - Weighted by reliability and recency

[Full methodology →](docs/methodology.md)

## 🔥 Why Use This List?

### vs Other Domain Lists

| Feature | Our List | Alexa (Discontinued) | Majestic Million | Tranco |
|---------|----------|---------------------|------------------|--------|
| **Total Domains** | 100M | 1M | 1M | 1M |
| **Update Frequency** | Monthly | - | Daily | Daily |
| **Free Access** | ✅ | ❌ | ✅ | ✅ |
| **Site Authority** | ✅ | ❌ | Partial | ❌ |
| **Historical Data** | ✅ | ❌ | ❌ | ✅ |
| **Multiple Formats** | ✅ | - | ✅ | ✅ |

**100x more comprehensive** than other free lists.

## 🚀 Powered by Website Launches

This dataset is maintained by **[Website Launches](https://websitelaunches.com)** - the platform for discovering newly launched websites daily.

### Want More Data?

Get enriched domain intelligence including:
- ✅ **Exact WebL Site Authority (WSA) scores** (0-1000)
- ✅ **Monthly traffic estimates**
- ✅ **Backlink counts & quality metrics**
- ✅ **Category & industry classification**
- ✅ **Historical ranking data**
- ✅ **API access** (3,000+ req/month)
- ✅ **Real-time updates**
- ✅ **Bulk exports** (JSON, CSV, Parquet)

**[Get Full Domain Intelligence →](https://websitelaunches.com/domains)**

## 📚 Documentation

- [Methodology](docs/methodology.md) - How domains are ranked
- [Use Cases](docs/use-cases.md) - Practical examples
- [FAQ](docs/faq.md) - Common questions
- [Changelog](CHANGELOG.md) - Update history

## 💻 Code Examples

### Python
```python
# Load and analyze top domains
import csv

with open('top-100k-domains.csv', 'r') as f:
    domains = [line.strip() for line in f]

# Find .ai domains in top 100k
ai_domains = [d for d in domains if d.endswith('.ai')]
print(f"Found {len(ai_domains)} .ai domains in top 100k")
```

### JavaScript
```javascript
// Fetch and parse top domains
fetch('https://raw.githubusercontent.com/websitelaunches/top-100-million-domains/main/data/top-1k-domains.csv')
  .then(r => r.text())
  .then(data => {
    const domains = data.split('\n');
    console.log(`Top domain: ${domains[0]}`);
  });
```

### PHP
```php
// Check if domain is in top 1M
$domain = 'example.com';
$top_domains = file('top-1m-domains.csv', FILE_IGNORE_NEW_LINES);
$rank = array_search($domain, $top_domains);

if ($rank !== false) {
    echo "$domain ranks #" . ($rank + 1);
} else {
    echo "$domain not in top 1M";
}
```

[More examples →](examples/)

## 🤝 Contributing

Found an issue or have a suggestion?

- 🐛 [Report a bug](https://github.com/websitelaunches/top-100-million-domains/issues)
- 💡 [Request a feature](https://github.com/websitelaunches/top-100-million-domains/issues)
- 📧 Email: support@websitelaunches.com

## 📅 Update Schedule

- **Monthly Updates**: 1st of each month
- **Format**: CSV (one domain per line)
- **Notification**: Watch this repo for updates

## 📜 License

MIT License - Free for commercial and non-commercial use.

**Attribution appreciated but not required.**

## ⭐ Star This Repo

Get notified of monthly updates by starring this repository!

## 📱 Stay Connected

- **Website**: [websitelaunches.com](https://websitelaunches.com)
- **Twitter**: [@websitelaunch](https://twitter.com/websitelaunch)
- **GitHub**: [websitelaunches](https://github.com/websitelaunches)
- **Email**: support@websitelaunches.com

---

**Maintained by**: [Website Launches](https://websitelaunches.com) | **Last Updated**: November 2025 | **Next Update**: December 2025
