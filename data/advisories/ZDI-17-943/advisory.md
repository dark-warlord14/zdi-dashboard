# ZDI-17-943: Bitdefender Internet Security Emulator 0x10A Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-943
- **ZDI-CAN:** ZDI-CAN-5102
- **Date:** 2017-12-12
- **CVE:** CVE-2017-17409
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-943/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within emulator 0x10A in cevakrnl.xmd. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Fixed with update id: 73456

## Disclosure Timeline

- 2017-10-12 - Vulnerability reported to vendor
- 2017-12-12 - Coordinated public release of advisory
