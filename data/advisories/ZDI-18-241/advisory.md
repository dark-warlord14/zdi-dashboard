# ZDI-18-241: Microsoft Internet Explorer VML textpath Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-241
- **ZDI-CAN:** ZDI-CAN-5369
- **Date:** 2018-03-19
- **CVE:** CVE-2018-0929
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-241/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VML markup that displays text along a path. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-0929

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-03-19 - Coordinated public release of advisory
- 2018-03-19 - Advisory Updated
