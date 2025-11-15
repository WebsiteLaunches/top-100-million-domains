# Frequently Asked Questions (FAQ)

## General Questions

### What is this dataset?

The Top 100 Million Domains is a free, open-source list of the internet's most authoritative domains, ranked by our proprietary WebL Site Authority algorithm that combines Common Crawl data with internal quality signals.

### How often is it updated?

The dataset is updated **monthly** (subject to data availability). Watch or star this repository to get notified of updates.

### Is it really free?

Yes! The dataset is completely free for both commercial and non-commercial use under the MIT License. No attribution required (but appreciated!).

### How is this different from Alexa or Majestic Million?

| Feature | Our List | Alexa | Majestic Million |
|---------|----------|-------|------------------|
| Size | 100M domains | 1M (discontinued) | 1M |
| Free | ✅ Yes | ❌ No | ✅ Yes |
| Site Authority | ✅ Yes (WSA) | Traffic only | Backlinks only |
| Updates | Monthly | - | Daily |

**We're 100x larger and combine multiple quality signals.**

---

## Data Questions

### Where does the data come from?

1. **Common Crawl** - Open web crawl data (billions of pages)
2. **RDAP** - Domain registration data
3. **Internal Signals** - Proprietary traffic, trust, and quality metrics

See [Methodology](methodology.md) for details.

### How accurate is the ranking?

The ranking is based on objective, data-driven metrics. However:
- Rankings lag real-world changes (monthly updates)
- New viral sites may take time to appear
- Geographic/language bias exists (see Methodology)

**For top 10k domains**: Very accurate (99%+ precision)
**For top 1M domains**: Highly accurate (95%+ precision)
**For all 100M domains**: Good directional accuracy

### Why isn't [domain X] ranked higher/lower?

Rankings depend on:
- Link equity from authoritative sites
- Domain age and history
- Web presence and traffic
- Trust signals

A domain might have high traffic but low DA if it lacks authoritative backlinks, or vice versa.

### Can I trust these rankings for SEO?

Yes, but use them as **one signal among many**. Consider:
- Your specific niche/industry
- Geographic target audience
- Recent trends (our data lags by ~30 days)
- Combine with other tools (Ahrefs, SEMrush, Moz)

### Do rankings change every month?

Yes, but:
- **Top 100**: Very stable (few changes)
- **Top 10k**: Stable (some movement)
- **Top 1M**: Moderate changes
- **Lower ranks**: More volatility

---

## Technical Questions

### What format is the data in?

Simple **CSV** (comma-separated values):
- One domain per line
- No headers
- Plain text format
- UTF-8 encoding

Example:
```
google.com
youtube.com
facebook.com
```

### How large are the files?

| File | Size | Download Time (10 Mbps) |
|------|------|-------------------------|
| top-1k-domains.csv | 13KB | Instant |
| top-10k-domains.csv | 127KB | <1 second |
| top-100k-domains.csv | 1.4MB | 1 second |
| top-1m-domains.csv | 15MB | 12 seconds |
| top-10m-domains.csv | 163MB | 2 minutes |
| top-100m-domains.csv | 1.7GB | 23 minutes |

### Can I download the full 100M list?

Yes! It's 1.7GB. Options:
1. **Direct download** from GitHub (may be slow)
2. **Git clone** the repository
3. **Torrent** (coming soon for faster downloads)
4. **API** (paid tier for streaming access)

### How do I load such a large file?

**Don't load it all into memory!** Stream it:

**Python:**
```python
with open('top-100m-domains.csv', 'r') as f:
    for line in f:  # Streams line-by-line
        domain = line.strip()
        # Process domain
```

**Bash:**
```bash
# Search for a specific domain
grep "example.com" top-100m-domains.csv

# Get top 1000
head -n 1000 top-100m-domains.csv

# Count total
wc -l top-100m-domains.csv
```

### Can I query specific domains without downloading?

Not yet, but coming soon! We're building a free API:

```bash
# Future API (coming Q1 2026)
curl https://api.websitelaunches.com/v1/rank/google.com
# {"domain": "google.com", "rank": 1, "da": 996}
```

---

## Usage Questions

### Can I use this commercially?

**Yes!** MIT License allows commercial use. Use it for:
- SEO tools and services
- Domain marketplaces
- Research products
- ML training data
- Anything else

**No attribution required** (but we'd appreciate a mention!).

### Can I redistribute this data?

Yes, under the MIT License you can:
- ✅ Redistribute the raw data
- ✅ Create derivative works
- ✅ Sell products based on this data
- ✅ Include in commercial software

Just include the MIT License notice.

### Can I create a competing product?

Yes, but please consider:
- Giving credit where credit is due
- Not just rebranding our exact work
- Adding value to the ecosystem

We're open-source friendly - use responsibly!

### How should I cite this in academic work?

**Citation format:**
```
Website Launches (2025). Top 100 Million Domains Dataset.
Retrieved from https://github.com/websitelaunches/top-100-million-domains
```

**BibTeX:**
```bibtex
@misc{top100mdomains2025,
  title={Top 100 Million Domains Dataset},
  author={{Website Launches}},
  year={2025},
  howpublished={\url{https://github.com/websitelaunches/top-100-million-domains}},
  note={Accessed: 2025-11-15}
}
```

---

## Product Questions

### Is there an API?

**Coming Q1 2026!** It will include:
- Domain rank lookup
- Batch queries
- Historical data
- Real-time updates
- Enriched metadata

[Join waitlist →](https://websitelaunches.com/domains)

### What about enriched data?

The GitHub dataset includes just **domain names and ranking**.

For enriched data, see our paid tiers:
- ✅ Exact WebL Site Authority (WSA) scores (0-1000)
- ✅ Monthly traffic estimates
- ✅ Backlink counts
- ✅ Category classification
- ✅ Historical trends
- ✅ Competitive intelligence

[Learn more →](https://websitelaunches.com/domains)

### Why should I pay if the data is free?

Free tier (GitHub):
- Domain names + ranking
- CSV format
- Monthly updates
- Manual downloads

Paid tier:
- **Enriched metadata** (DA scores, traffic, backlinks)
- **API access** (programmatic queries)
- **Real-time updates** (daily/weekly)
- **Historical data** (track changes over time)
- **Support** (dedicated help)
- **Custom datasets** (filtered by criteria)

Think of it as: **Free = domain list, Paid = domain intelligence**

---

## Troubleshooting

### The download is too slow

Options:
1. **Use Git LFS** (Large File Storage)
2. **Download smaller subsets** (top-1m instead of top-100m)
3. **Use our API** (coming soon - faster streaming)
4. **Wait for torrent** (coming soon)

### I found an error in the rankings

Please [open an issue](https://github.com/websitelaunches/top-100-million-domains/issues) with:
- Domain name
- Current rank
- Why you think it's wrong
- Supporting evidence

We review all reports!

### A domain is missing

Possible reasons:
- Not in top 100M (there are billions of domains)
- Too new (registered after our last update)
- Filtered out (adult content, spam, etc.)
- Data quality issue

Check if it appears in our next monthly update.

### Can you add feature X?

We love feedback! Please:
1. [Open an issue](https://github.com/websitelaunches/top-100-million-domains/issues)
2. Describe the feature
3. Explain the use case
4. We'll discuss feasibility

---

## Business Questions

### Who maintains this?

**[Website Launches](https://websitelaunches.com)** - A platform for discovering newly launched websites daily.

### Why are you giving this away for free?

1. **Community benefit**: Open data helps everyone
2. **SEO & marketing**: Drives awareness of Website Launches
3. **Upsell opportunity**: Free tier → paid enriched data
4. **Research value**: Academic and industry research

It's a win-win!

### How do you make money?

- **Paid API** access for enriched data
- **Enterprise** subscriptions with custom features
- **Website Launches** platform (our main product)

The free dataset is our contribution to the open data ecosystem.

### Can we partner?

Yes! We're open to:
- Data partnerships
- Integration partnerships
- Research collaborations
- Commercial licensing

Email: domains@websitelaunches.com

---

## Still Have Questions?

- **Technical questions**: [Open an issue](https://github.com/websitelaunches/top-100-million-domains/issues)
- **Business inquiries**: support@websitelaunches.com
- **General support**: support@websitelaunches.com
- **Twitter**: [@websitelaunch](https://twitter.com/websitelaunch)

---

**Last Updated**: November 2025
