# ZDI-16-191: Adobe Reader Out-Of-Bounds Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-191
- **ZDI-CAN:** ZDI-CAN-3253
- **Date:** 2016-03-08
- **CVE:** CVE-2016-1009
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Jaanus Kp - Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDFs. The issue lies in the failure to ensure that indexes are within the bounds of an allocated buffer. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-09.html

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
