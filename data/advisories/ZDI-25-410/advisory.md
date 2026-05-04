# ZDI-25-410: Allegra calculateTokenExpDate Password Recovery Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-410
- **ZDI-CAN:** ZDI-CAN-27104
- **Date:** 2025-06-19
- **CVE:** CVE-2025-6216
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** Swagat
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-410/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Allegra. Authentication is not required to exploit this vulnerability. The specific flaw exists within the password recovery mechanism. The issue results from reliance upon a predictable value when generating a password reset token. An attacker can leverage this vulnerability to bypass authentication on the application.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://alltena.com/en/resources/release-notes/release-notes-for-release-8-1-4-and-release-7-5-2

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-06-19 - Coordinated public release of advisory
- 2025-06-19 - Advisory Updated
