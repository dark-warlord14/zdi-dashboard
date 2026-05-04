# ZDI-07-058: Oracle E-Business Suite SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-058
- **ZDI-CAN:** ZDI-CAN-159
- **Date:** 2007-10-31
- **CVE:** CVE-2007-5766
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle / PeopleSoft
- **Affected Products:** E-Business Suite
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-058/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL on vulnerable installations of Oracle E-Business Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists in the okxLOV.jsp page in the Administration console. This page allows an attacker to specify arguments to a WHERE SQL command without sanitation, allowing for arbitrary SQL injection in the context of the APPS user.

## Additional Details

Oracle / PeopleSoft has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuoct2007.html

## Disclosure Timeline

- 2007-01-29 - Vulnerability reported to vendor
- 2007-10-31 - Coordinated public release of advisory
