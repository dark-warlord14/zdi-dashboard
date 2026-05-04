# ZDI-16-226: (Pwn2Own) Adobe Flash AS2 Transform matrix Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-226
- **ZDI-CAN:** ZDI-CAN-3613
- **Date:** 2016-04-08
- **CVE:** CVE-2016-1016
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Yuki Chen of Qihoo 360 Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Transform objects. By setting a special callback on the flash.geom.Matrix object, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb16-10.html

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-04-08 - Coordinated public release of advisory
