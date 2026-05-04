# ZDI-06-030: CA BrightStor ARCserve Discovery Service Remote Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-030
- **ZDI-CAN:** ZDI-CAN-041
- **Date:** 2006-10-05
- **CVE:** CVE-2006-5143
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** livesploit.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Computer Associates BrightStor ARCserve Backup, Enterprise Backup, Server Protection Suite and Business Protection Suite. Authentication is not required to exploit this vulnerability and both client and servers are affected. The problem specifically exists within the discovery service which communicates initially over UDP port 41524 and then over TCP port 41523. Due to invalid bounds checking during TCP communications, a stack based buffer overflow may occur in ASBRDCST.DLL during a call to vsprintf().

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/basbr-secnotice.asp

## Disclosure Timeline

- 2006-04-07 - Vulnerability reported to vendor
- 2006-10-05 - Coordinated public release of advisory
