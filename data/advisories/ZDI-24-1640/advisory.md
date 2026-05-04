# ZDI-24-1640: XnSoft XnView Classic RWZ File Parsing Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1640
- **ZDI-CAN:** ZDI-CAN-22913
- **Date:** 2024-12-02
- **CVE:** CVE-2024-11950
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** XnSoft
- **Affected Products:** XnView Classic
- **Credit:** Im Junhyuk, Jeong Soeun, Im Seongmin, Lee Jinhyeok, Hyun Chae-eul, Lee Hyungyu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1640/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of XnSoft XnView Classic. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RWZ files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 2.52.0

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
