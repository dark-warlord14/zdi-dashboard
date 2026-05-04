# ZDI-10-200: Tivoli Storage Manager FastBack 0xfafbfcfd Packet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-200
- **ZDI-CAN:** ZDI-CAN-700
- **Date:** 2010-10-12
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-200/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Tivoli Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within FastBackServer.exe which listens by default on TCP port 1320. When handling a packet with header type 0xFAFBFCFD the process blindly copies user supplied data into a heap buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21443820 Issue 2

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
