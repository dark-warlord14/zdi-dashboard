# ZDI-15-565: Adobe Flash AS2 MovieClip setMask Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-565
- **ZDI-CAN:** ZDI-CAN-3291
- **Date:** 2015-11-10
- **CVE:** CVE-2015-7660
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** bilou
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-565/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the setMask method. By manipulating the arguments passed to the setMask method, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-28.html

## Disclosure Timeline

- 2015-09-15 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
