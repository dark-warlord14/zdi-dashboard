# ZDI-11-308: Cisco WebEx Player ATAS32.DLL linesProcessed Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-308
- **ZDI-CAN:** ZDI-CAN-1170
- **Date:** 2011-10-26
- **CVE:** CVE-2011-4004
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Aniway (Aniway.Anyway@gmail.com) Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-308/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in ATAS32.DLL during the parsing of values defined within the WRF file format. The vulnerable code trusts the linesProcessed value from the file, and uses it in some logic to determine the destination pointer for a memcpy. By supplying an overly large linesProcessed value, the subtraction would cause an integer underflow and allows an attacker control of the destination buffer pointer. This can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/go/psirt

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
