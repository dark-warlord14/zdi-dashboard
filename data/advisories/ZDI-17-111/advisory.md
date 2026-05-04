# ZDI-17-111: Adobe Acrobat Reader DC Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-111
- **ZDI-CAN:** ZDI-CAN-3920
- **Date:** 2017-02-16
- **CVE:** CVE-2017-2939
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** 734388278a34721ed1869ab23235b2c976a145e2
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-111/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-01.html

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2017-02-16 - Coordinated public release of advisory
