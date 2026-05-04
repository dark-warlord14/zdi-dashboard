# ZDI-23-1108: (Pwn2Own) Adobe Acrobat Reader DC Net.HTTP.request Exposed Dangerous Method Sandbox Escape

## Metadata

- **ZDI ID:** ZDI-23-1108
- **ZDI-CAN:** ZDI-CAN-20743
- **Date:** 2023-08-15
- **CVE:** CVE-2023-26405
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri of Haboob SA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1108/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Net.HTTP.request method. The component exposes an undocumented verb that allows an attacker to open a mini-browser session. An attacker can leverage this vulnerability to escape the sandbox and execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-24.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
