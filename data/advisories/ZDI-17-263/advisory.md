# ZDI-17-263: Adobe Reader DC Collab shareFile Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-263
- **ZDI-CAN:** ZDI-CAN-4434
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3043
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-263/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Collab's shareFile function. The issue occurs when a PDF file is opened from the Cloud. The Collab.shareFile function does not properly check the file path, which results in reading arbitrary memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-11.html

## Disclosure Timeline

- 2017-01-13 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
