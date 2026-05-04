# ZDI-12-165: (0Day) HP Operations Agent for NonStop Server HEALTH Packet Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-165
- **ZDI-CAN:** ZDI-CAN-1391
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Operations Agent for NonStop
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-165/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Operations Agent for NonStop Server. User interaction is required to exploit this vulnerability in that the target must check the status of an existing node on the network. The specific flaw exists within ELinkService process which listens on TCP ports 7771 and 8976 by default. The process performs insufficient bounds checking on user-supplied data within in a HEALTH packet prior to copying it into a fixed-length buffer on the stack. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed message packets to the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline.

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
