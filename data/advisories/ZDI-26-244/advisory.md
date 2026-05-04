# ZDI-26-244: (Pwn2Own) QNAP QHora-322 miro_webserver_controllers_api_login_singIn Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-244
- **ZDI-CAN:** ZDI-CAN-25846
- **Date:** 2026-03-30
- **CVE:** CVE-2024-13088
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** nella17 (@nella17tw), working with DEVCORE Internship Program, and DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-244/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the miro_webserver_controllers_api_login_singIn function. The issue results from allowing a user to authenticate using an arbitrary QCloud account. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-15

## Disclosure Timeline

- 2024-12-13 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
