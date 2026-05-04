# ZDI-17-334: Bitdefender Internet Security Dalvik Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-334
- **ZDI-CAN:** ZDI-CAN-4522
- **Date:** 2017-05-11
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-334/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within dalvik.xmd. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Vendor released a fix: update 7.70461.

## Disclosure Timeline

- 2017-03-24 - Vulnerability reported to vendor
- 2017-05-11 - Coordinated public release of advisory
