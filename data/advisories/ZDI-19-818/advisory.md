# ZDI-19-818: Adobe Flash Player PSDK Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-818
- **ZDI-CAN:** ZDI-CAN-9079
- **Date:** 2019-09-10
- **CVE:** CVE-2019-8070
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-818/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of objects in the PSDK namespace. By performing actions in ActionScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb19-46.html

## Disclosure Timeline

- 2019-07-25 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
