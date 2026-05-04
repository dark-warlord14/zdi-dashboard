# ZDI-23-1107: (Pwn2Own) Adobe Acrobat Reader DC Object Prototype Pollution API Restrictions Bypass

## Metadata

- **ZDI ID:** ZDI-23-1107
- **ZDI-CAN:** ZDI-CAN-20712
- **Date:** 2023-08-15
- **CVE:** CVE-2023-26405
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri of Haboob SA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1107/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Object data types. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb23-24.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
