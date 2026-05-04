# ZDI-12-144: EMC AutoStart ftAgent Opcode 0x4B Subcode 0x1D4C Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-144
- **ZDI-CAN:** ZDI-CAN-1485
- **Date:** 2012-08-17
- **CVE:** CVE-2012-0409
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-144/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the EMC Autostart ftAgent, which is deployed on machines managed by EMC Autostart by default. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing routines for op-codes used by EMC Autostart ftAgent's proprietary network protocol. This ftAgent.exe service listens on TCP port 8045, and performs arithmetic for memory size calculation using values read from the network without validation. This arithmetic is susceptible to integer overflow, causing the memory allocation to be undersized, ultimately allowing for heap-based memory corruption. An attacker can exploit this condition to gain remote code execution as user SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/522835/30/0/threaded

## Disclosure Timeline

- 2012-01-12 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
