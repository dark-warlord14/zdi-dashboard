# ZDI-25-041: Ivanti Endpoint Manager updateAssetInfo SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-041
- **ZDI-CAN:** ZDI-CAN-25929
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13162
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Kevin Salapatek of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the updateAssetInfo method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-January-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-12-06 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
