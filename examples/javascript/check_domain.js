/**
 * Check if a domain is in the Top 1k domains list
 * Node.js example
 */

const fs = require('fs');
const readline = require('readline');

async function checkDomain(domain, listFile = '../../data/top-1k-domains.csv') {
  console.log(`Checking if ${domain} is in top 1000...`);

  const fileStream = fs.createReadStream(listFile);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let rank = 0;
  for await (const line of rl) {
    rank++;
    if (line.trim().toLowerCase() === domain.toLowerCase()) {
      console.log(`✓ ${domain} is ranked #${rank}`);
      return rank;
    }
  }

  console.log(`✗ ${domain} not in top 1000`);
  return null;
}

// Browser-compatible version (fetch API)
async function checkDomainBrowser(domain) {
  const url = 'https://raw.githubusercontent.com/websitelaunches/top-100-million-domains/main/data/top-1k-domains.csv';

  try {
    const response = await fetch(url);
    const text = await response.text();
    const domains = text.split('\n');

    const rank = domains.findIndex(d => d.trim().toLowerCase() === domain.toLowerCase()) + 1;

    if (rank > 0) {
      console.log(`✓ ${domain} is ranked #${rank}`);
      return rank;
    } else {
      console.log(`✗ ${domain} not in top 1000`);
      return null;
    }
  } catch (error) {
    console.error('Error fetching domain list:', error);
    return null;
  }
}

// Run if called directly
if (require.main === module) {
  const domain = process.argv[2];

  if (!domain) {
    console.log('Usage: node check_domain.js <domain>');
    console.log('Example: node check_domain.js google.com');
    process.exit(1);
  }

  checkDomain(domain);
}

module.exports = { checkDomain, checkDomainBrowser };
