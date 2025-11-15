#!/usr/bin/env python3
"""
Analyze TLD (Top-Level Domain) distribution in the dataset
"""

from collections import Counter
import sys

def analyze_tlds(list_file='../../data/top-100k-domains.csv', top_n=20):
    """Analyze TLD distribution"""
    tld_counter = Counter()
    total_domains = 0

    print(f"Analyzing TLDs in: {list_file}")
    print("-" * 60)

    with open(list_file, 'r') as f:
        for line in f:
            domain = line.strip()
            if '.' in domain:
                tld = domain.split('.')[-1]
                tld_counter[tld] += 1
                total_domains += 1

    print(f"\nTotal domains analyzed: {total_domains:,}")
    print(f"\nTop {top_n} TLDs:\n")
    print(f"{'Rank':<6} {'TLD':<10} {'Count':<12} {'Percentage':<12}")
    print("-" * 60)

    for rank, (tld, count) in enumerate(tld_counter.most_common(top_n), 1):
        percentage = (count / total_domains) * 100
        print(f"{rank:<6} .{tld:<9} {count:<12,} {percentage:>10.2f}%")

if __name__ == '__main__':
    list_file = sys.argv[1] if len(sys.argv) > 1 else '../../data/top-100k-domains.csv'
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 20

    analyze_tlds(list_file, top_n)
