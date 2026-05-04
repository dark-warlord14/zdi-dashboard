# ZDI-07-017: Oracle E-Business Suite Arbitrary Document Download Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-017
- **ZDI-CAN:** ZDI-CAN-132
- **Date:** 2007-04-18
- **CVE:** CVE-2007-2135
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Oracle / PeopleSoft
- **Affected Products:** Database Server
- **Credit:** Joxean Koret
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-017/
## Vulnerability Details

This vulnerability allows remote attackers to download any existing document in the APPS.FND_DOCUMENTS table on vulnerable installations of Oracle E-Business Suite. Authentication is not required to exploit this vulnerability. The specific flaw exists in the ADI_BINARY component of the E-Business Suite. The component exposes a parameter that can also be passed to ADI_DISPLAY_REPORT to allow an attacker to view any document in the APPS.FND_DOCUMENTS table. An attacker can cycle through all document IDs to display each document that exists.

## Additional Details

Oracle / PeopleSoft has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2007.html

## Disclosure Timeline

- 2007-01-29 - Vulnerability reported to vendor
- 2007-04-18 - Coordinated public release of advisory
