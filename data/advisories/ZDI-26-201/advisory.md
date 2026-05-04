# ZDI-26-201: (Pwn2Own) QNAP TS-453E Hyper Data Protector Plugin Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-201
- **ZDI-CAN:** ZDI-CAN-28358
- **Date:** 2026-03-16
- **CVE:** CVE-2025-59388
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-201/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP TS-453E devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of Bareos by the Hyper Data Protector Plugin. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-48

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
