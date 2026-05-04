# ZDI-26-239: (Pwn2Own) QNAP QHora-322 login.newAuthMiddleware.Authenticator Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-239
- **ZDI-CAN:** ZDI-CAN-28422
- **Date:** 2026-03-30
- **CVE:** CVE-2025-62844
- **CVSS:** 5.6
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Bongeun Koo (@kiddo_pwn) and Evangelos Daravigkas (@freddo_1337) of Team DDOS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-239/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the qurouter_token parameter provided to the login.newAuthMiddleware.Authenticator endpoint. The issue results from allowing a user to authenticate using an arbitrary QCloud account. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-26-12

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
