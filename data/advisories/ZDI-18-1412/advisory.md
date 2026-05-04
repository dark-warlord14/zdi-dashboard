# ZDI-18-1412: Adobe Reader DC Onix NextKey Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1412
- **ZDI-CAN:** ZDI-CAN-7005
- **Date:** 2018-12-17
- **CVE:** CVE-2018-16009
- **CVSS:** 7.7
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1412/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the NextKey method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-07-30 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
