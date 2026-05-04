# ZDI-13-019: EMC NetWorker nsrindexd.exe Opcode 0x07 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-019
- **ZDI-CAN:** ZDI-CAN-1543
- **Date:** 2013-02-11
- **CVE:** CVE-2012-4607
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** EMC
- **Affected Products:** NetWorker
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC NetWorker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way nsrindexd.exe handles RPC calls with opcode 0x07 for program 0x0005F3D9. While processing this message a user supplied string is copied into a fixed size stack buffer. This can result in a buffer overflow which can lead to remote code execution under the context of the current process.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/525229/30/0/threaded

## Disclosure Timeline

- 2012-11-14 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
