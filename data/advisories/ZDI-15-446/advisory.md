# ZDI-15-446: (Pwn2Own) Adobe Flash Player DefineText Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-446
- **ZDI-CAN:** ZDI-CAN-2817
- **Date:** 2015-09-21
- **CVE:** CVE-2015-6678
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** k33nteam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-446/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the DefineText tag. A specially crafted DefineFont2 tag can overflow a buffer of size TotalNumberOfGlyph * 2 bytes. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-23.html

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-09-21 - Coordinated public release of advisory
