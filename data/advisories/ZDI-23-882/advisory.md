# ZDI-23-882: (Pwn2Own) Microsoft SharePoint ValidateTokenIssuer Improper Verification of Cryptographic Signature Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-882
- **ZDI-CAN:** ZDI-CAN-20716
- **Date:** 2023-06-16
- **CVE:** CVE-2023-29357
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Nguyễn Tiến Giang (@testanull) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-882/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Microsoft SharePoint. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ValidateTokenIssuer method. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29357

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
- 2024-10-25 - Advisory Updated
