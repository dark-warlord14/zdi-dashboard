# ZDI-16-320: Adobe Reader DC XFA Page Array Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-320
- **ZDI-CAN:** ZDI-CAN-3507
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1072
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Sebastian Apelt siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-320/
## Vulnerability Details

This vulnerability allows remote attackers to gain information about the layout of memory on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Page array. A specially crafted PDF file can force Adobe Reader DC to read memory past the end of the Page object array. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
