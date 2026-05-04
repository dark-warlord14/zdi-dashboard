# ZDI-11-263: Symantec Veritas Storage Foundation vxsvc.exe ASCII String Unpacking Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-263
- **ZDI-CAN:** ZDI-CAN-1112
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0547
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas Storage Foundation
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Veritas Storage Foundation Administrator Service. Authentication is not required to exploit this vulnerability. The specific flaw exists within vxsvc.exe. The problem affecting the part of the server running on TCP port 2148 is an integer overflow in the function vxveautil.value_binary_unpack during the handling of the ascii strings (opcode 6) where the 32-bit field supplied by the attacker is used for allocating a destination buffer by adding an additional byte to its value. This integer overflow can be used to create a small allocation which will be subsequently overflowed, allowing the attacker to execute arbitrary code under the context of the SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110815_00

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
