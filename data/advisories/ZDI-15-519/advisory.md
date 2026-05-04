# ZDI-15-519: Microsoft Office Visio UML Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-519
- **ZDI-CAN:** ZDI-CAN-3096
- **Date:** 2015-10-13
- **CVE:** CVE-2015-2557
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-519/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within UML parsing. By providing a malformed Visio file, an attacker is able to cause data to be written outside of a normal buffer. An attacker could use this to execute arbitrary code under the context of the Visio process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-110

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
