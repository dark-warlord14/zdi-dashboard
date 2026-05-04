# ZDI-13-009: (Mobile Pwn2Own) Apple Safari shiftCount/splice Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-009
- **ZDI-CAN:** ZDI-CAN-1657
- **Date:** 2013-02-01
- **CVE:** CVE-2012-3748
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple, Apple
- **Affected Products:** iPhone, Safari
- **Credit:** Joost Pol and Daan Keuper of Certified Secure
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Array objects. When splicing a sparse array, the size of a sparse array is not properly validated. In addition, parameters checked at the beginning of a function are never again validated despite being modified later on. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5567 Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5567

## Disclosure Timeline

- 2012-09-02 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
