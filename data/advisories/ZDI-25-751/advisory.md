# ZDI-25-751: (Pwn2Own) QNAP QHora-322 IPv6 Incorrectly Specified Destination in a Communication Channel Network Spoofing Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-751
- **ZDI-CAN:** ZDI-CAN-25625
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar from Computest Sector 7
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-751/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to redirect localhost traffic on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the /etc/hosts file. The issue results from the router issuing DNS requests for localhost on the WAN. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
