# ZDI-11-351: WellinTech KingView HistoryServer.exe Opcode 3 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-351
- **ZDI-CAN:** ZDI-CAN-1261
- **Date:** 2011-12-22
- **CVE:** CVE-2011-4536
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** WellinTech
- **Affected Products:** KingView
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-351/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wellintek KingView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the protocol parsing code inside nettransdll.dll. The parent service is called HistoryServer.exe and listens on port 777. When a packet with op-code 3 is received, the service allocates memory from the heap based on the 10th and 11th bytes of the packet (element count). Packet data is then copied into the allocated buffer based on the first two bytes of the packet (packet size). These values can be manipulated to create a heap overflow and and attacker can exploit this to remotely execute arbitrary code in the context of the service (Local System).

## Additional Details

WellinTech has issued an update to correct this vulnerability. More details can be found at: http://www.kingview.com/news/detail.aspx?contentid=587

## Disclosure Timeline

- 2011-11-09 - Vulnerability reported to vendor
- 2011-12-22 - Coordinated public release of advisory
