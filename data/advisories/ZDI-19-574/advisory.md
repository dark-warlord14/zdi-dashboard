# ZDI-19-574: Electronic Arts Origin URI Handler Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-574
- **ZDI-CAN:** ZDI-CAN-8686
- **Date:** 2019-06-17
- **CVE:** CVE-2019-12828
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Electronic Arts
- **Affected Products:** Origin
- **Credit:** Ron Waisberg of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-574/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Electronic Arts Origin. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. There is an issue with the way the product handles URIs within certain schemes. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Fixed in version 10.5.38.26728 (PC) and 10.5.39.26720 (Mac)

## Disclosure Timeline

- 2019-05-08 - Vulnerability reported to vendor
- 2019-06-17 - Coordinated public release of advisory
- 2019-09-10 - Advisory Updated
