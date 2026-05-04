# ZDI-25-026: Mintty Path Conversion Improper Input Validation Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-026
- **ZDI-CAN:** ZDI-CAN-24744
- **Date:** 2025-01-10
- **CVE:** CVE-2024-45301
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Mintty
- **Affected Products:** Mintty
- **Credit:** solid-snail
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-026/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Mintty. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of printed characters. Crafted sequences of escape characters can cause the product to fetch a resource from an arbitrary path. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

Fixed in version 3.7.5

## Disclosure Timeline

- 2024-08-16 - Vulnerability reported to vendor
- 2025-01-10 - Coordinated public release of advisory
- 2025-01-10 - Advisory Updated
