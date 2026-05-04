# ZDI-16-442: Oracle Glassfish PartItem Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-442
- **ZDI-CAN:** ZDI-CAN-3510
- **Date:** 2016-07-21
- **CVE:** CVE-2016-3607
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Glassfish Server
- **Credit:** Alvaro Munoz (@pwntester) & Christian Schneider (@cschneider4711)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-442/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Glassfish Server. Authentication is not required to exploit this vulnerability. The PartItem class allows remote attackers to write to arbitrary files via a NULL byte in a file name in a serialized instance, when used in conjunction with a specific version of Oracle Java. An attacker could leverage this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujul2016-2881720.html

## Disclosure Timeline

- 2016-01-22 - Vulnerability reported to vendor
- 2016-07-21 - Coordinated public release of advisory
