# ZDI-12-111: SAP Netweaver ABAP msg_server.exe Opcode 0x43 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-111
- **ZDI-CAN:** ZDI-CAN-1394
- **Date:** 2012-06-28
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** SAP
- **Affected Products:** NetWeaver
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-111/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of SAP Netweaver ABAP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the msg_server.exe listening on 3900 by default. When the msg_server parses a message with opcode 0x43 and sub-opcode 0x04 it uses a user suplied size field to copy a string into a static sized stack buffer. The resulting buffer overflow can lead to remote code execution under the context of the process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://websmp230.sap-ag.de/sap(bD1lbiZjPTAwMQ==)/bc/bsp/spn/sapnotes/index2.htm?numm=1649840

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-06-28 - Coordinated public release of advisory
