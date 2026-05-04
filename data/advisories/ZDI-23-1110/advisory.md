# ZDI-23-1110: (Pwn2Own) Adobe Acrobat Reader DC Net.HTTP.request URL Restriction Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1110
- **ZDI-CAN:** ZDI-CAN-20744
- **Date:** 2023-08-15
- **CVE:** CVE-2023-26406
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri of Haboob SA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the enforcement of the allowlist for domains. The issue lies in improper verification of approved domains for content delivery. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-24.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
