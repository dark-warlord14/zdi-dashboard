# ZDI-16-636: Adobe Digital Editions FlateDecode Out-of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-636
- **ZDI-CAN:** ZDI-CAN-3923
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7888
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Digital Editions
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-636/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Digital Editions. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of FlateDecode streams in PDF files. The process does not properly validate user-supplied data which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/Digital-Editions/apsb16-45.html

## Disclosure Timeline

- 2016-07-26 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
