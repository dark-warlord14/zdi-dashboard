# ZDI-24-1165: Allegra getLinkText Server-Side Template Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1165
- **ZDI-CAN:** ZDI-CAN-23609
- **Date:** 2024-08-22
- **CVE:** CVE-2024-30372
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1165/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Allegra. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of getLinkText method. The issue results from the lack of proper validation of a user-supplied string before processing it with the template engine. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://alltena.com/en/resources/release-notes/relnotes-7-5-2

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
