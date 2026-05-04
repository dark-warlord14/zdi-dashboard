# ZDI-14-324: Adobe Reader 3DIF Plugin Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-324
- **ZDI-CAN:** ZDI-CAN-2300
- **Date:** 2014-09-16
- **CVE:** CVE-2014-0561
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Tom Ferris - Security-Protocols.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-324/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the 3DIF Plugin (3difr.x3d). By providing a crafted PDF, an attacker is able to overflow a heap buffer allocated by the 3DIF plugin, and could use this vulnerability to execute arbitrary code in the context of the viewing process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://t.info.adobesystems.com//r/?id=t35c7e2bc,808fe4f,83a379a

## Disclosure Timeline

- 2014-05-06 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
