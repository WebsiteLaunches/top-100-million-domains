<?php
/**
 * Find competitor domains in the top domains list
 */

function findCompetitors($competitors, $listFile = '../../data/top-100k-domains.csv') {
    echo "Searching for competitors in top 100k domains...\n";
    echo str_repeat("-", 60) . "\n";

    $results = [];
    $handle = fopen($listFile, 'r');

    if (!$handle) {
        die("Error: Could not open $listFile\n");
    }

    $rank = 0;
    while (($line = fgets($handle)) !== false) {
        $rank++;
        $domain = trim($line);

        if (in_array($domain, $competitors)) {
            $results[$domain] = $rank;
            echo sprintf("✓ Found: %-30s Rank: #%s\n", $domain, number_format($rank));
        }
    }

    fclose($handle);

    // Check for missing competitors
    $missing = array_diff($competitors, array_keys($results));
    if (!empty($missing)) {
        echo "\n✗ Not found in top 100k:\n";
        foreach ($missing as $domain) {
            echo "  - $domain\n";
        }
    }

    echo "\nSummary:\n";
    echo sprintf("  Found: %d/%d competitors\n", count($results), count($competitors));

    return $results;
}

// Example usage
if (php_sapi_name() === 'cli') {
    $competitors = [
        'amazon.com',
        'ebay.com',
        'walmart.com',
        'target.com',
        'shopify.com',
        'etsy.com'
    ];

    // Override with command line args if provided
    if ($argc > 1) {
        $competitors = array_slice($argv, 1);
    }

    $results = findCompetitors($competitors);

    // Sort by rank
    asort($results);

    echo "\nRanked competitors:\n";
    $position = 1;
    foreach ($results as $domain => $rank) {
        echo sprintf("%d. %s (#%s)\n", $position++, $domain, number_format($rank));
    }
}
