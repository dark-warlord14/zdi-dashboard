# ZDI-08-028: IBM Lotus Sametime Community Services Multiplexer Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-028
- **ZDI-CAN:** ZDI-CAN-247
- **Date:** 2008-05-21
- **CVE:** CVE-2008-2499
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Sametime
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Sametime. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of long URLs in the Community Services Multiplexer (StMux.exe) listening on TCP port 1533. A specially crafted URL can be passed into a vulnerable sscanf() function that will result in a stack overflow resulting in the ability to execute arbitrary code.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?rs=463&uid=swg21303920

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2008-05-21 - Coordinated public release of advisory
