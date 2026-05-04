# ZDI-20-337: (Pwn2Own) TP-Link Archer A7 DNS Response Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-337
- **ZDI-CAN:** ZDI-CAN-9661
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10885
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-337/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DNS responses. The issue results from the lack of proper validation of DNS reponses prior to further processing. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the root user.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
