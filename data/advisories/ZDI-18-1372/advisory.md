# ZDI-18-1372: Adobe Acrobat Pro DC search Javascript Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1372
- **ZDI-CAN:** ZDI-CAN-6903
- **Date:** 2018-12-12
- **CVE:** CVE-2018-16044
- **CVSS:** 4.2
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1372/
## Vulnerability Details

This vulnerability allows remote attackers to bypass Javascript API restrictions on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the search object. By creating a specially crafted PDF with specific Javascript instructions, it is possible to bypass the Javascript API restrictions. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-07-23 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
