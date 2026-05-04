# ZDI-25-756: (Pwn2Own) QNAP QHora-322 Improper Restriction of Communication Channel to Intended Endpoints Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-756
- **ZDI-CAN:** ZDI-CAN-25488
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-756/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to access the management interface on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the management interface. The issue results from exposing the management interface on the WAN side of the router over IPv6. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-16 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
