# ZDI-25-946: (0Day) Ivanti Endpoint Manager Report_RunPatch SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-946
- **ZDI-CAN:** ZDI-CAN-26859
- **Date:** 2025-10-07
- **CVE:** CVE-2025-62386
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-946/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the Report_RunPatch class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

06/27/25 – ZDI reported the vulnerability to the vendor 07/29/25 - the vendor requested an extension until March 2026 09/26/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product. The vendor published a security advisory on 10/13/2025 https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Endpoint-Manager-EPM-October-2025?language=en_US

## Disclosure Timeline

- 2025-06-27 - Vulnerability reported to vendor
- 2025-10-07 - Coordinated public release of advisory
- 2025-10-16 - Advisory Updated
