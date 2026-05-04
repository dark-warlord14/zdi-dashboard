# ZDI-20-333: (Pwn2Own) TP-Link Archer A7 DNS Response Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-333
- **ZDI-CAN:** ZDI-CAN-9660
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10881
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-333/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DNS responses. A crafted DNS message can trigger an overflow of a fixed-length, stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the root user.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-15 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
