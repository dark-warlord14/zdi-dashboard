# ZDI-12-025: EMC Networker indexd.exe Opcode 0x01 Parsing Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-12-025
- **ZDI-CAN:** ZDI-CAN-1451
- **Date:** 2012-02-08
- **CVE:** CVE-2012-0395
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** NetWorker
- **Credit:** Tal zeltzer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way the indexd.exe handles rpc calls with opcode 0x1 for program 0x0005F3D9. While processing this message a user supplied string is copied into a fixed size stack buffer. This can result in a buffer overflow which can lead to remote code execution under the context of the current process.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/521374/100/0/threaded

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
