# ZDI-17-107: Adobe Digital Editions PDF Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-107
- **ZDI-CAN:** ZDI-CAN-3983
- **Date:** 2017-02-14
- **CVE:** CVE-2017-2975
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Digital Editions
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-107/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Digital Editions. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of fonts inside PDF files. A crafted PDF can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/Digital-Editions/apsb17-05.html

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2017-02-14 - Coordinated public release of advisory
