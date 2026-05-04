# ZDI-24-1498: Ivanti Endpoint Manager Report_Run SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1498
- **ZDI-CAN:** ZDI-CAN-24294
- **Date:** 2024-11-13
- **CVE:** CVE-2024-34781
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1498/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the Report_Run class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-November-2024-for-EPM-2024-and-EPM-2022

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-11-13 - Coordinated public release of advisory
- 2024-11-13 - Advisory Updated
