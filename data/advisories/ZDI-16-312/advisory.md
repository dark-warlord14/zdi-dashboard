# ZDI-16-312: Adobe Acrobat Pro DC FileAttachment point Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-312
- **ZDI-CAN:** ZDI-CAN-3517
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1065
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Brian Gorenc - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-312/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the handling of FileAttachment annotations. By setting the point attribute to a specific array, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
