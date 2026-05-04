# ZDI-12-104: SAP Netweaver ABAP msg_server.exe Parameter Value Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-104
- **ZDI-CAN:** ZDI-CAN-1395
- **Date:** 2012-06-27
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** NetWeaver
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP NetWeaver ABAP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way SAP NetWeaver handles packages with opcode 0x43. If a package with sub opcode 0x4 contains a long parameter value string NetWeaver will eventually write a \x00 byte onto the stack to mark the end of the string. The location of this null byte is dependent on user supplied data and the resulting stack corruption can lead to remote code execution under the context of the running process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://websmp230.sap-ag.de/sap(bD1lbiZjPTAwMQ==)/bc/bsp/spn/sapnotes/index2.htm?numm=1649838

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-06-27 - Coordinated public release of advisory
