# ZDI-25-044: Ivanti Avalanche SecureFilter Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-044
- **ZDI-CAN:** ZDI-CAN-25713
- **Date:** 2025-01-19
- **CVE:** CVE-2024-13179
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-044/
## Vulnerability Details

This vulnerability allows remote attackers to partially bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SecureFilter class. The issue results from incorrect string matching when making an authorization decision. An attacker can leverage this vulnerability to partially bypass authentication on the application.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-6-4-7-Multiple-CVEs

## Disclosure Timeline

- 2024-12-06 - Vulnerability reported to vendor
- 2025-01-19 - Coordinated public release of advisory
- 2025-01-19 - Advisory Updated
