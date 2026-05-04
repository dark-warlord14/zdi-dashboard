# ZDI-26-241: (Pwn2Own) QNAP QHora-322 qvpn_db_mgr username SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-241
- **ZDI-CAN:** ZDI-CAN-28424
- **Date:** 2026-03-30
- **CVE:** CVE-2025-62846
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Bongeun Koo (@kiddo_pwn) and Evangelos Daravigkas (@freddo_1337) of Team DDOS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-241/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP QHora-322 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the qvpn_db_mgr module. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-26-12

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
