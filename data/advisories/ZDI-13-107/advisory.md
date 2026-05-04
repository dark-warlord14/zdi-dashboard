# ZDI-13-107: Apple Safari Array Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-107
- **ZDI-CAN:** ZDI-CAN-1704
- **Date:** 2013-05-30
- **CVE:** CVE-2013-0997
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-107/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JSArray objects. The issue lies in the usage of a custom sort comparison function. By manipulating a JSArray object an attacker can force controlled memory to be accessed. An attacker can lever this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
