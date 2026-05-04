# ZDI-11-274: EMC Autostart ftAgent Opcode 0x140 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-274
- **ZDI-CAN:** ZDI-CAN-1255
- **Date:** 2011-08-23
- **CVE:** CVE-2011-2735
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-274/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC AutoStart. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Agent Service (ftAgent.exe). The Agent Service listens on TCP port 8045 for communications between AutoStart nodes. When handling messages with opcode 0x140 the process performs arithmetic on an unvalidated user-supplied value used to determine the size of a new heap buffer, allowing a potential integer wrap to cause a heap buffer overflow. Remote, unauthenticated attackers can exploit this vulnerability by sending malformed message packets to the target, which can ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/519371

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2011-08-23 - Coordinated public release of advisory
