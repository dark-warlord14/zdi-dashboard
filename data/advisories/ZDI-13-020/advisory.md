# ZDI-13-020: EMC NetWorker nsrck.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-020
- **ZDI-CAN:** ZDI-CAN-1542
- **Date:** 2013-02-11
- **CVE:** CVE-2012-4607
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** EMC
- **Affected Products:** NetWorker
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC NetWorker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the way nsrck.exe handles a remotely supplied string. When handling RPC calls for opcode 0x07 of program 0x0005F3D9, the nsrindexd.exe process starts a new nsrck.exe process using a user-supplied string parameter as a command argument. The vulnerable code directly uses the remote supplied command argument in a sprintf-like function without proper bounds checking. This can result in a buffer overflow which can lead to remote code execution under the context of the current process.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/525229/30/0/threaded

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
