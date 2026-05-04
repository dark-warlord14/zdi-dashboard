# ZDI-17-047: Bitdefender Internet Security NSIS Pages Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-047
- **ZDI-CAN:** ZDI-CAN-4357
- **Date:** 2017-01-20
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Bitdefender
- **Affected Products:** Internet Security
- **Credit:** Pagefault
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Bitdefender Internet Security. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within nsis.xmd. The issue results from the lack of proper validation of user-supplied data which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Update to Version: 7.68928, Signature number: 7876821 or higher

## Disclosure Timeline

- 2017-01-03 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
