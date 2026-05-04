# ZDI-06-020: Apple iTunes AAC File Parsing Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-020
- **ZDI-CAN:** ZDI-CAN-043
- **Date:** 2006-06-29
- **CVE:** CVE-2006-1467
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** iTunes
- **Credit:** ATmaCA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-020/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple iTunes. Exploitation requires an attacker to convince a target user into opening a malicious play list file. The specific flaw exists during the processing of malicious AAC media files such as those with extensions .M4A and .M4P. During the parsing of the sample table size atom (STSZ), a malformed 'sample_size_table' value can trigger an integer overflow leading to an exploitable memory corruption.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://docs.info.apple.com/article.html?artnum=303952

## Disclosure Timeline

- 2006-04-07 - Vulnerability reported to vendor
- 2006-06-29 - Coordinated public release of advisory
