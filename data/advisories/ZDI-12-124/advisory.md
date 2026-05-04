# ZDI-12-124: EMC AutoStart ftAgent Opcode 50 Subcode 42 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-124
- **ZDI-CAN:** ZDI-CAN-1450
- **Date:** 2012-07-12
- **CVE:** CVE-2012-0409
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC Autostart. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ftAgent.exe service, which listens by default on TCP port 8045. When handling messages with opcode 50 (0x32) and subcode 42 (0x2a), the process performs arithmetic on an unvalidated user-supplied value used to determine the size of a new heap buffer, allowing a potential integer wrap to cause a heap buffer overflow. This vulnerability can be leveraged to execute code under the context of the SYSTEM user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/522835/30/0/threaded

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-07-12 - Coordinated public release of advisory
