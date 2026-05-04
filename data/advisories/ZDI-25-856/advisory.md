# ZDI-25-856: Ivanti Avalanche getCountMuStatDevicePropResultsFromMuListAgentIds SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-856
- **ZDI-CAN:** ZDI-CAN-27134
- **Date:** 2025-08-20
- **CVE:** CVE-2025-8296
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Kevin Salapatek
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-856/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the getCountMuStatDevicePropResultsFromMuListAgentIds function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-CVE-2025-8296-CVE-2025-8297?language=en_US

## Disclosure Timeline

- 2025-06-19 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated
