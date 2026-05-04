# ZDI-11-141: Nortel CS1000 Communications Server Remote Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-141
- **ZDI-CAN:** ZDI-CAN-950
- **Date:** 2011-04-20
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Nortel
- **Affected Products:** CS1000 Communications Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-141/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of Nortel CS1000 Communication Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the process listening on UDP port 5100. When parsing a request, it takes the size and subtracts 2. This can be abused to cause the integer to wrap negatively and subsequently cause the process to crash while copying memory. This can be abused by a remote attacker to crash the PBX server.

## Additional Details

Nortel has issued an update to correct this vulnerability. More details can be found at: https://support.avaya.com/css/P8/documents/100133768

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2011-04-20 - Coordinated public release of advisory
