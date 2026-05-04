# ZDI-17-927: Adobe Acrobat Pro DC iframe Same Origin Policy Bypass Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-927
- **ZDI-CAN:** ZDI-CAN-4756
- **Date:** 2017-11-21
- **CVE:** CVE-2017-16369
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-927/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of HTML to PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in bypassing the same origin policy. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-36.html

## Disclosure Timeline

- 2017-06-22 - Vulnerability reported to vendor
- 2017-11-21 - Coordinated public release of advisory
