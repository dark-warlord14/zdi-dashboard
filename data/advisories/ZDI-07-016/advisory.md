# ZDI-07-016: Oracle E-Business Suite Arbitrary Node Deletion Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-016
- **ZDI-CAN:** ZDI-CAN-136
- **Date:** 2007-04-17
- **CVE:** CVE-2007-2170
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle / PeopleSoft
- **Affected Products:** Database Server
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-016/
## Vulnerability Details

This vulnerability allows remote attackers to delete any existing Document Management node on vulnerable installations of Oracle E-Business Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists in the APPLSYS.FND_DM_NODES package. The procedure to delete nodes does not check for a valid session thereby allowing an attacker to arbitrarily delete any node registered, including the root node.

## Additional Details

Oracle / PeopleSoft has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2007.html

## Disclosure Timeline

- 2007-01-29 - Vulnerability reported to vendor
- 2007-04-17 - Coordinated public release of advisory
