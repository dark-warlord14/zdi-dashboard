# ZDI-19-564: Adobe Flash Player LocalConnection Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-564
- **ZDI-CAN:** ZDI-CAN-8453
- **Date:** 2019-06-11
- **CVE:** CVE-2019-7845
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-564/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of LocalConnection objects. By performing actions in ActionScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb19-30.html

## Disclosure Timeline

- 2019-05-02 - Vulnerability reported to vendor
- 2019-06-11 - Coordinated public release of advisory
