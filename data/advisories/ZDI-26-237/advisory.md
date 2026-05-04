# ZDI-26-237: (Pwn2Own) QNAP QHora-322 ip6_wanifset Improper Restriction of Communication Channel to Intended Endpoints Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-237
- **ZDI-CAN:** ZDI-CAN-28371
- **Date:** 2026-03-30
- **CVE:** CVE-2025-62843
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Bongeun Koo (@kiddo_pwn) and Evangelos Daravigkas (@freddo_1337) of Team DDOS
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-237/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass firewall rules on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of firewall rules. The issue results from failing to match IPv6 firewall rules on PPPoE connections. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-26-12

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
