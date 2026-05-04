# ZDI-25-235: Ivanti Endpoint Manager OpenRecordSet SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-235
- **ZDI-CAN:** ZDI-CAN-25953
- **Date:** 2025-04-09
- **CVE:** CVE-2025-22461
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Kevin Salapatek
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-235/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the OpenRecordSet method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-April-2025-for-EPM-2024-and-EPM-2022-SU6

## Disclosure Timeline

- 2024-12-19 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
