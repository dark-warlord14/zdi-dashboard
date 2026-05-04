# ZDI-26-240: (Pwn2Own) QNAP QHora-322 qvpn_db_mgr role_type Improper Neutralization of Escape Sequences Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-240
- **ZDI-CAN:** ZDI-CAN-28423
- **Date:** 2026-03-30
- **CVE:** CVE-2025-62845
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Bongeun Koo (@kiddo_pwn) and Evangelos Daravigkas (@freddo_1337) of Team DDOS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-240/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected QNAP QHora-322 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the role_type parameter provided to the qvpn_db_mgr endpoint. The issue results from insufficient neutralization of special characters. An attacker can leverage this vulnerability to bypass QBelt VPN authentication.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-26-12

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
