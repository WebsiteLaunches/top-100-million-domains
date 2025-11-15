# Use Cases - Practical Applications

This document provides detailed examples of how to use the Top 100 Million Domains dataset in real-world scenarios.

## Table of Contents

- [SEO & Marketing](#seo--marketing)
- [Domain Investing](#domain-investing)
- [Brand Protection](#brand-protection)
- [Machine Learning](#machine-learning)
- [Cybersecurity](#cybersecurity)
- [Academic Research](#academic-research)
- [Web Development](#web-development)

---

## SEO & Marketing

### Competitor Benchmarking

**Goal**: Understand where your website ranks compared to competitors.

```python
import csv

# Your domain and competitors
my_domain = "mywebsite.com"
competitors = [
    "competitor1.com",
    "competitor2.com",
    "competitor3.com",
    "competitor4.com"
]

# Search top 1M
with open('top-1m-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip()

        if domain == my_domain:
            print(f"✓ Your site ranks #{rank:,}")
        elif domain in competitors:
            print(f"  {domain} ranks #{rank:,}")
```

**Output:**
```
✓ Your site ranks #45,234
  competitor1.com ranks #23,105
  competitor2.com ranks #67,891
  competitor3.com ranks #89,234
```

### Link Building Target Identification

**Goal**: Find high-authority domains in your niche for outreach.

```python
import csv

# Find .edu domains in top 100k (great for backlinks)
edu_domains = []

with open('top-100k-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        if domain.endswith('.edu'):
            edu_domains.append(domain)

print(f"Found {len(edu_domains)} .edu domains in top 100k")
print("Top 10 .edu domains:")
for domain in edu_domains[:10]:
    print(f"  - {domain}")
```

### Content Gap Analysis

**Goal**: Identify what types of sites rank well in your category.

```python
# Find all news/media sites in top 10k
news_keywords = ['news', 'times', 'post', 'herald', 'tribune', 'journal']

with open('top-10k-domains.csv', 'r') as f:
    news_sites = [
        line.strip() for line in f
        if any(keyword in line.lower() for keyword in news_keywords)
    ]

print(f"Found {len(news_sites)} news sites in top 10k")
```

---

## Domain Investing

### Find Undervalued Domains

**Goal**: Discover domains with high authority but potentially available or underpriced.

```python
import csv

# Look for short domains (5-7 chars) in top 100k
short_high_authority = []

with open('top-100k-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip()
        name = domain.split('.')[0]  # Get name without TLD

        # Short name, high rank = valuable
        if 5 <= len(name) <= 7:
            short_high_authority.append((rank, domain, len(name)))

# Sort by rank (best first)
short_high_authority.sort()

print("Top 20 short domains with high authority:")
for rank, domain, length in short_high_authority[:20]:
    print(f"#{rank:,} - {domain} ({length} chars)")
```

### Expired Domain Monitoring

**Goal**: Track when valuable domains might become available.

```python
import whois  # pip install python-whois
from datetime import datetime, timedelta

# Check expiration dates for top domains
domains_to_monitor = []

with open('top-10k-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip()

        try:
            w = whois.whois(domain)
            exp_date = w.expiration_date

            if isinstance(exp_date, list):
                exp_date = exp_date[0]

            # Expiring in next 90 days?
            if exp_date and (exp_date - datetime.now()).days < 90:
                domains_to_monitor.append((rank, domain, exp_date))
        except:
            continue

print(f"Found {len(domains_to_monitor)} high-authority domains expiring soon")
```

### TLD Analysis

**Goal**: Understand which TLDs are most authoritative.

```python
from collections import Counter

tld_distribution = Counter()

with open('top-100k-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        tld = domain.split('.')[-1]
        tld_distribution[tld] += 1

print("Top 20 TLDs in top 100k:")
for tld, count in tld_distribution.most_common(20):
    percentage = (count / 100000) * 100
    print(f".{tld}: {count:,} ({percentage:.1f}%)")
```

---

## Brand Protection

### Monitor Brand Variations

**Goal**: Find domains similar to your brand that might be squatting or typosquatting.

```python
import difflib

your_brand = "acmecorp"
similar_threshold = 0.7  # 70% similarity

potential_threats = []

with open('top-1m-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip()
        domain_name = domain.split('.')[0]

        # Check similarity
        similarity = difflib.SequenceMatcher(
            None, your_brand, domain_name
        ).ratio()

        if similarity > similar_threshold and domain_name != your_brand:
            potential_threats.append((rank, domain, similarity))

print(f"Found {len(potential_threats)} similar domains:")
for rank, domain, sim in sorted(potential_threats, key=lambda x: x[2], reverse=True)[:20]:
    print(f"#{rank:,} - {domain} ({sim:.0%} similar)")
```

### Trademark Monitoring

**Goal**: Find domains containing your trademarked terms.

```python
trademarks = ["acme", "superfoo", "megabar"]

trademark_domains = {tm: [] for tm in trademarks}

with open('top-100k-domains.csv', 'r') as f:
    for rank, line in enumerate(f, 1):
        domain = line.strip().lower()

        for tm in trademarks:
            if tm in domain:
                trademark_domains[tm].append((rank, domain))

for tm, domains in trademark_domains.items():
    print(f"\n'{tm}' appears in {len(domains)} top-100k domains:")
    for rank, domain in domains[:5]:
        print(f"  #{rank:,} - {domain}")
```

---

## Machine Learning

### Training Data for Domain Classification

**Goal**: Create labeled dataset for machine learning models.

```python
import csv
import random

# Create training data: top 10k = "high quality", rest = "normal/low quality"
training_data = []

# Positive examples (high quality)
with open('top-10k-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        training_data.append((domain, 1))  # Label: 1 = high quality

# Negative examples (sample from lower ranks)
with open('top-10m-domains.csv', 'r') as f:
    domains = [line.strip() for line in f]

# Sample 10k random domains from rank 500k-10M
negative_samples = random.sample(domains[500000:], 10000)
for domain in negative_samples:
    training_data.append((domain, 0))  # Label: 0 = normal quality

# Shuffle
random.shuffle(training_data)

# Save for ML training
with open('domain_classification_training.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['domain', 'quality_label'])
    writer.writerows(training_data)

print(f"Created training dataset with {len(training_data)} examples")
print(f"  - {sum(1 for _, label in training_data if label == 1):,} high quality")
print(f"  - {sum(1 for _, label in training_data if label == 0):,} normal quality")
```

### Feature Engineering

**Goal**: Extract features from domains for ML models.

```python
import re

def extract_domain_features(domain):
    """Extract ML features from domain name"""
    name = domain.split('.')[0]
    tld = domain.split('.')[-1]

    return {
        'length': len(name),
        'has_numbers': bool(re.search(r'\d', name)),
        'has_hyphens': '-' in name,
        'tld': tld,
        'tld_is_com': tld == 'com',
        'tld_is_org': tld == 'org',
        'vowel_ratio': sum(1 for c in name if c in 'aeiou') / len(name) if name else 0,
        'consonant_clusters': len(re.findall(r'[bcdfghjklmnpqrstvwxyz]{3,}', name.lower())),
    }

# Extract features for top 1000
features = []
with open('top-1k-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        features.append(extract_domain_features(domain))

# Analyze
print(f"Average domain length in top 1k: {sum(f['length'] for f in features) / len(features):.1f}")
print(f"Percent with numbers: {sum(f['has_numbers'] for f in features) / len(features) * 100:.1f}%")
print(f"Percent .com: {sum(f['tld_is_com'] for f in features) / len(features) * 100:.1f}%")
```

---

## Cybersecurity

### Phishing Domain Detection

**Goal**: Identify potential phishing sites impersonating legitimate brands.

```python
# Load legitimate top domains
legitimate_domains = set()
with open('top-10k-domains.csv', 'r') as f:
    legitimate_domains = {line.strip() for line in f}

# Check suspicious domains against legitimate ones
def check_potential_phishing(domain):
    """Check if domain might be phishing attempt"""
    domain_lower = domain.lower()

    for legit in legitimate_domains:
        legit_name = legit.split('.')[0]

        # Check for common phishing patterns
        if legit_name in domain_lower and domain != legit:
            # Suspicious patterns
            if any(pattern in domain_lower for pattern in [
                'login', 'secure', 'verify', 'account', 'update',
                'confirm', 'banking', 'wallet', '-'
            ]):
                return True, legit

    return False, None

# Example usage
suspicious = "paypal-login-verify.com"
is_suspicious, legitimate = check_potential_phishing(suspicious)
if is_suspicious:
    print(f"⚠️  {suspicious} might be phishing {legitimate}")
```

### Malware C2 Domain Filtering

**Goal**: Filter out known good domains when analyzing C2 traffic.

```python
# Load top 1M domains (likely legitimate)
known_good = set()
with open('top-1m-domains.csv', 'r') as f:
    known_good = {line.strip() for line in f}

# Analyze DNS logs
def analyze_dns_logs(dns_log_file):
    """Flag suspicious domains not in top 1M"""
    suspicious_queries = []

    with open(dns_log_file, 'r') as f:
        for line in f:
            domain = line.strip().split()[-1]  # Simplified parsing

            if domain not in known_good:
                suspicious_queries.append(domain)

    return suspicious_queries

# This reduces noise by filtering out known-good domains
```

---

## Academic Research

### Web Ecosystem Analysis

**Goal**: Study the structure and evolution of the web.

```python
# Analyze domain age distribution in top sites
from collections import Counter
import whois

age_distribution = []

# Sample 1000 random domains from different tiers
sample_domains = []

with open('top-100k-domains.csv', 'r') as f:
    domains = [line.strip() for line in f]

# Stratified sampling
sample_domains.extend(domains[:100])        # Top 100
sample_domains.extend(domains[1000:1100])   # Rank 1k-1.1k
sample_domains.extend(domains[10000:10100]) # Rank 10k-10.1k

for domain in sample_domains:
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            age = (datetime.now() - creation_date).days / 365.25
            age_distribution.append(age)
    except:
        continue

print(f"Average age of sampled domains: {sum(age_distribution) / len(age_distribution):.1f} years")
print(f"Median age: {sorted(age_distribution)[len(age_distribution)//2]:.1f} years")
```

### Language and Geographic Analysis

**Goal**: Understand global distribution of authoritative domains.

```python
# Analyze ccTLDs (country code top-level domains)
from collections import Counter

cctld_distribution = Counter()

# Common ccTLDs
cctlds = {
    'uk': 'United Kingdom', 'de': 'Germany', 'jp': 'Japan',
    'fr': 'France', 'au': 'Australia', 'ca': 'Canada',
    'cn': 'China', 'ru': 'Russia', 'br': 'Brazil',
    'in': 'India', 'it': 'Italy', 'es': 'Spain'
}

with open('top-1m-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        tld = domain.split('.')[-1]

        if tld in cctlds:
            cctld_distribution[tld] += 1

print("Geographic distribution (top 1M):")
for tld, count in cctld_distribution.most_common():
    country = cctlds[tld]
    percentage = (count / 1000000) * 100
    print(f"{country} (.{tld}): {count:,} domains ({percentage:.2f}%)")
```

---

## Web Development

### DNS Prefetching Optimization

**Goal**: Prefetch DNS for the most common third-party domains.

```javascript
// Generate DNS prefetch hints for common third-parties
const topDomains = [
  'googleapis.com',
  'gstatic.com',
  'cloudflare.com',
  'cloudfront.net',
  'jquery.com',
  'bootstrapcdn.com'
  // ... from top-1k-domains.csv
];

// Add to HTML <head>
topDomains.forEach(domain => {
  const link = document.createElement('link');
  link.rel = 'dns-prefetch';
  link.href = `//${domain}`;
  document.head.appendChild(link);
});
```

### CDN Selection

**Goal**: Choose CDNs that host popular domains.

```python
# Find most common CDN providers in top 100k
cdn_keywords = ['cdn', 'cloudfront', 'cloudflare', 'fastly', 'akamai']

cdns = []
with open('top-100k-domains.csv', 'r') as f:
    for line in f:
        domain = line.strip()
        if any(keyword in domain.lower() for keyword in cdn_keywords):
            cdns.append(domain)

print(f"Found {len(cdns)} CDN domains in top 100k")
```

---

## More Examples

Browse the [examples/](../examples/) directory for complete, runnable code in:
- Python
- JavaScript
- PHP
- SQL

## Questions or New Use Cases?

Have a use case not covered here?
- [Open an issue](https://github.com/websitelaunches/top-100-million-domains/issues)
- Email: domains@websitelaunches.com

---

**Last Updated**: November 2025
