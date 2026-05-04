# ZDI-12-119: EMC AutoStart ftAgent Opcode 0x41 Subcode 0x00 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-119
- **ZDI-CAN:** ZDI-CAN-1445
- **Date:** 2012-07-12
- **CVE:** CVE-2012-0409
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC Autostart. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ftAgent.exe service, which listens by default on TCP port 8045. When handling messages with opcode 65 (0x41) and subcode 00, the vulnerable function uses a uninitialized stack variable in calculating a memory pointer. Also, the function uses signed extension and signed comparison when checking the uninitialized stack variable, which allows arbitrary negative values to bypass the check. This could result in corruption of a controlled memory location, which can be leveraged to execute code under the context of the SYSTEM user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/522835/30/0/threaded

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-07-12 - Coordinated public release of advisory
