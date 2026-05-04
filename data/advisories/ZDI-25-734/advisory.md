# ZDI-25-734: (Pwn2Own) QNAP QHora-322 IPMI Use of Weak Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-734
- **ZDI-CAN:** ZDI-CAN-25633
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-734/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IPMI interface. The issue results from the use of the WAN MAC address as a default password. An attacker can leverage this vulnerability to bypass authentication on the remote management interface.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
