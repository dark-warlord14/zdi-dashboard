# ZDI-25-741: (Pwn2Own) QNAP QHora-322 openvpn_cli user_name SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-741
- **ZDI-CAN:** ZDI-CAN-25580
- **Date:** 2025-07-31
- **CVE:** CVE-2024-50389
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-741/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability, however a specific configuration is necessary. The specific flaw exists within the openvpn_cli module. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/zh-tw/security-advisory/qsa-24-45

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
