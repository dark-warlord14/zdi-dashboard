# ZDI-20-336: (Pwn2Own) TP-Link Archer A7 tdpServer Use of Hard-coded Cryptographic Key Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-336
- **ZDI-CAN:** ZDI-CAN-9652
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10884
- **CVSS:** 8.1
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-336/
## Vulnerability Details

This vulnerability allows network-adjacent attackers execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the tdpServer service, which listens on UDP port 20002 by default. This issue results from the use of hard-coded encryption key. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
