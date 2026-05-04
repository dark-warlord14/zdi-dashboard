# ZDI-16-358: (Pwn2Own) Apple OS X WindowServer Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-358
- **ZDI-CAN:** ZDI-CAN-3611
- **Date:** 2016-05-26
- **CVE:** CVE-2016-1804
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Liang Chen Yubin Fu Marco Grassi of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-358/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CFData objects within the WindowServer process. An attacker can cause a CFData object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the WindowServer.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-26 - Coordinated public release of advisory
