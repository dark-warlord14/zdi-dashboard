# ZDI-11-264: Symantec Veritas Storage Foundation vxsvc.exe Value Unpacking Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-264
- **ZDI-CAN:** ZDI-CAN-1110
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0547
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas Storage Foundation
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-264/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Veritas Storage Foundation Administrator Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within vxsvc.exe process. The problem affecting the part of the server running on tcp port 2148 is an integer overflow in the function vxveautil.kv_binary_unpack where a 32-bit field is used to allocate an amount of memory equal to its value plus 1. This can be made to miscalculate a heap buffer which can be subsequently overflowed allowing an attacker to execute arbitrary code under the context of SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110815_00

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
