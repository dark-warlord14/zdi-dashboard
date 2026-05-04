# ZDI-25-749: (Pwn2Own) QNAP QHora-322 qfirewall Improper Restriction of Communication Channel to Intended Endpoints Firewall Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-749
- **ZDI-CAN:** ZDI-CAN-25596
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Alain Rodel, Benjamin Walny (Neodyme AG)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-749/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass firewall rules on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of firewall rules. The issue results from failing to bind LAN IP ranges to the LAN interfaces. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
