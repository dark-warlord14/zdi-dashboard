# ZDI-12-162: (0Day) HP Diagnostics Server magentservice.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-162
- **ZDI-CAN:** ZDI-CAN-1287
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Diagnostics Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-162/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Diagnostics Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the magentservice.exe process which listens on port 23472 by default. The process performs insufficient bounds checking on user-supplied data prior to copying it into a fixed-length buffer on the stack. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed message packets to the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline.

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
