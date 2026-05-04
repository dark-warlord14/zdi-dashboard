# ZDI-10-179: IBM TSM FastBack Mount Service Arbitrary Overwrite Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-179
- **ZDI-CAN:** ZDI-CAN-656
- **Date:** 2010-09-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM
- **Affected Products:** Tivoli Storage Manager
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-179/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Tivoli Storage Manager Fastback. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Mount service (FastBackMount.exe). This process listens by default on UDP port 30005. This process writes the value 0x01 to the address specified by the second DWORD from a packet received to it's UDP port. An attacker can exploit this behavior to execute arbitrary code by making several requests to this service.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21443820 Issue 1

## Disclosure Timeline

- 2010-01-06 - Vulnerability reported to vendor
- 2010-09-29 - Coordinated public release of advisory
