# ZDI-23-1106: (Pwn2Own) Adobe Acrobat Reader DC Net.HTTP.request Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1106
- **ZDI-CAN:** ZDI-CAN-20745
- **Date:** 2023-08-15
- **CVE:** CVE-2023-26407
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri of Haboob SA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1106/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Net.HTTP.request objects. By performing actions in JavaScript, an attacker can launch an executable file. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-24.html

## Disclosure Timeline

- 2023-08-15 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
