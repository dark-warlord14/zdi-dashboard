# ZDI-16-009: Adobe Reader DC FileAttachment point Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-009
- **ZDI-CAN:** ZDI-CAN-3021
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0931
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Brian Gorenc - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the handling of FileAttachment annotations. By setting the point attribute to a specific array, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
