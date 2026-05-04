# ZDI-14-014: Adobe Flash Player Jump Opcode Information Leak Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-014
- **ZDI-CAN:** ZDI-CAN-1993
- **Date:** 2014-02-05
- **CVE:** CVE-2014-0492
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the jump operation code. The issue lies in the failure of the ActionScript Virtual Machine to properly sanitize values before jumping to them. An attacker can leverage this vulnerability to leak addresses from Flash.ocx within the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/flash-player/apsb14-02.html

## Disclosure Timeline

- 2013-10-23 - Vulnerability reported to vendor
- 2014-02-05 - Coordinated public release of advisory
