# ZDI-20-668: Adobe Character Animator EPS BoundingBox Element Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-668
- **ZDI-CAN:** ZDI-CAN-10879
- **Date:** 2020-05-25
- **CVE:** CVE-2020-9586
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Character Animator
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-668/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Character Animator. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the BoundingBox element in PostScript. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://helpx.adobe.com/security/products/character_animator/apsb20-25.html

## Disclosure Timeline

- 2020-04-07 - Vulnerability reported to vendor
- 2020-05-25 - Coordinated public release of advisory
