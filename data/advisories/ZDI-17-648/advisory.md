# ZDI-17-648: Bitdefender Internet Security Inno Header Strings Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-648
- **ZDI-CAN:** ZDI-CAN-4359
- **Date:** 2017-08-11
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within instyler.xmd. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

1/31/2017: The issue is now fixed: Version - 7.69318.

## Disclosure Timeline

- 2017-01-23 - Vulnerability reported to vendor
- 2017-08-11 - Coordinated public release of advisory
