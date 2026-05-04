# ZDI-17-248: Adobe Flash SWF Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-248
- **ZDI-CAN:** ZDI-CAN-4533
- **Date:** 2017-04-11
- **CVE:** CVE-2017-3060
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** b5e4b07ed250ac8014390628445b0d26
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within SWF parsing. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-10.html

## Disclosure Timeline

- 2017-02-13 - Vulnerability reported to vendor
- 2017-04-11 - Coordinated public release of advisory
