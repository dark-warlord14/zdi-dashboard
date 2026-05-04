# ZDI-12-018: Symantec PCAnywhere awhost32 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-018
- **ZDI-CAN:** ZDI-CAN-1273
- **Date:** 2012-01-25
- **CVE:** CVE-2011-3478
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Symantec
- **Affected Products:** PCAnywhere
- **Credit:** Tal zeltzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-018/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec PCAnywhere. Authentication is not required to exploit this vulnerability. The flaw exists within the awhost32 component which is used when handling incoming connections. This process listens on TCP port 5631. When handling an authentication request the process copies the user supplied username unsafely to a fixed-length buffer of size 0x108. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM account.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2012&suid=20120124_00

## Disclosure Timeline

- 2011-08-16 - Vulnerability reported to vendor
- 2012-01-25 - Coordinated public release of advisory
