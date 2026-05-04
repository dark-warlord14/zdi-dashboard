# ZDI-26-079: Ivanti Endpoint Manager ROI SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-079
- **ZDI-CAN:** ZDI-CAN-26863
- **Date:** 2026-02-12
- **CVE:** CVE-2026-1602
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-079/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the ROI class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://hub.ivanti.com/s/article/Security-Advisory-EPM-February-2026-for-EPM-2024?language=en_US

## Disclosure Timeline

- 2025-09-02 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
