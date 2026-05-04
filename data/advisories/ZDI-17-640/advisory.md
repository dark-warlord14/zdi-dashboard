# ZDI-17-640: Microsoft Internet Explorer SVG Layout Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-640
- **ZDI-CAN:** ZDI-CAN-4777
- **Date:** 2017-08-08
- **CVE:** CVE-2017-8653
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 62600BCA031B9EB5CB4A74ADDDD6771E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-640/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the layout of HTML documents. By manipulating a document's elements, an attacker can trigger access to memory prior to initialization. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8653

## Disclosure Timeline

- 2017-05-16 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
