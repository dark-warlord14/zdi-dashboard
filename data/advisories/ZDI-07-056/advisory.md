# ZDI-07-056: IBM DB2 DB2JDS Multiple Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-056
- **ZDI-CAN:** ZDI-CAN-125
- **Date:** 2007-10-10
- **CVE:** CVE-2007-2582
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** IBM
- **Affected Products:** DB2 Universal Database
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-056/
## Vulnerability Details

The most severe of these vulnerabilities allows remote attackers to execute arbitrary code on vulnerable installations of IBM DB2 Universal Database. Authentication is not required to exploit these vulnerabilities. The first flaw exists in the DB2JDS service listening on TCP port 6789. A specially crafted packet is improperly processed by an internal sprintf() call resulting in a stack overflow which can be leveraged to execute arbitrary code. Additionally, two DoS condition vulnerabilities were discovered. The first flaw is an overflow resulting from an invalid LANG paramater. The second DoS can be triggered by sending a packet over 32768 bytes in length, resulting in a MemTree overflow which will cause the process to terminate.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-1.ibm.com/support/docview.wss?uid=swg1IY97750

## Disclosure Timeline

- 2006-11-09 - Vulnerability reported to vendor
- 2007-10-10 - Coordinated public release of advisory
