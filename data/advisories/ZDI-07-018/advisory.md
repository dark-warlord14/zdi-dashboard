# ZDI-07-018: IBM Tivoli Monitoring Express Universal Agent Heap Overflow Vunlerability

## Metadata

- **ZDI ID:** ZDI-07-018
- **ZDI-CAN:** ZDI-CAN-069
- **Date:** 2007-04-17
- **CVE:** CVE-2007-2137
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Monitoring Express
- **Credit:** CIRT.DK
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-018/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Monitoring Express. Authentication is not required to exploit this vulnerability. The specific flaws exist in the Tivoli Universal Agent Primary Service (TCP 10110), Monitoring Agent for Windows OS - Primary (TCP 6014) and Tivoli Enterprise Portal Server (TCP 14206) services. When a long string is sent to these services, it will result in a heap overflow during a call to a vulnerable function in kde.dll resulting in the ability to execute arbitrary code.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?uid=swg24012341

## Disclosure Timeline

- 2006-09-14 - Vulnerability reported to vendor
- 2007-04-17 - Coordinated public release of advisory
