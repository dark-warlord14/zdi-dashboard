# ZDI-20-1206: Microhard Bullet-LTE Basic Authorization Header Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1206
- **ZDI-CAN:** ZDI-CAN-10596
- **Date:** 2020-08-26
- **CVE:** CVE-2020-17407
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microhard
- **Affected Products:** Bullet-LTE
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1206/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microhard Bullet-LTE. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of authentication headers. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in R112

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-08-26 - Coordinated public release of advisory
- 2020-09-17 - Advisory Updated
