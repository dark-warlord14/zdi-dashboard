# ZDI-25-258: (Pwn2Own) Adobe Acrobat Reader DC distributionURL JavaScript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-258
- **ZDI-CAN:** ZDI-CAN-23553
- **Date:** 2025-04-30
- **CVE:** CVE-2024-34099
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri of Haboob SA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-258/
## Vulnerability Details

This vulnerability allows remote attackers to bypass JavaScript API restrictions on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the distributionURL property. The application does not adequately restrict access to a protected API. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb24-29.html

## Disclosure Timeline

- 2024-04-24 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated
