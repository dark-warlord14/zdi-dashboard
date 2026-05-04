# ZDI-16-697: Bitdefender Internet Security AutoIt v3 Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-697
- **ZDI-CAN:** ZDI-CAN-4176
- **Date:** 2017-08-01
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-697/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within unpack.xmd. The issue results from the lack of proper validation of user-supplied data which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

The fix build version is: 7.68372.

## Disclosure Timeline

- 2016-12-01 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
