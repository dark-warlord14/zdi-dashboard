# ZDI-22-856: (Pwn2Own) OPC Foundation UA .NET Standard Improper Input Validation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-856
- **ZDI-CAN:** ZDI-CAN-17205
- **Date:** 2022-06-16
- **CVE:** CVE-2022-29865
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Daan Keuper & Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-856/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of certificates. The issue results from the lack of proper validation of a user-supplied certificate. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-29865.pdf

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-06-16 - Coordinated public release of advisory
- 2022-06-16 - Advisory Updated
