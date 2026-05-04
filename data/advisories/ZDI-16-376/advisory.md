# ZDI-16-376: Oracle Java Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-376
- **ZDI-CAN:** ZDI-CAN-3467
- **Date:** 2016-06-29
- **CVE:** CVE-2016-3443
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** bo13oy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-376/
## Vulnerability Details

This vulnerability allows remote attackers to leak arbitrary information on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of font files. The issue lies in insufficient validation of supplied font data in Java, where specific font data can force reading memory past the end of an allocated object. An attacker can leverage this vulnerability to leak arbitrary information.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuapr2016v3-2985753.html

## Disclosure Timeline

- 2016-01-12 - Vulnerability reported to vendor
- 2016-06-29 - Coordinated public release of advisory
