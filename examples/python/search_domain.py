#!/usr/bin/env python3
"""
Search for a domain's rank in the Top 100M Domains list
"""

import sys

def find_domain_rank(domain, list_file='../../data/top-100m-domains.csv'):
    """Find the rank of a domain in the list"""
    print(f"Searching for: {domain}")
    print(f"In file: {list_file}")
    print("-" * 50)

    try:
        with open(list_file, 'r') as f:
            for rank, line in enumerate(f, 1):
                current_domain = line.strip()

                if current_domain == domain:
                    print(f"✓ Found: {domain}")
                    print(f"  Rank: #{rank:,}")
                    print(f"  Top {(rank/100000000)*100:.4f}% of all domains")
                    return rank

                # Show progress every 10M domains
                if rank % 10000000 == 0:
                    print(f"  Searched {rank:,} domains...")

        print(f"✗ Domain not found in top 100M")
        return None

    except FileNotFoundError:
        print(f"Error: File not found: {list_file}")
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python search_domain.py <domain>")
        print("Example: python search_domain.py google.com")
        sys.exit(1)

    domain = sys.argv[1].lower().strip()
    find_domain_rank(domain)
