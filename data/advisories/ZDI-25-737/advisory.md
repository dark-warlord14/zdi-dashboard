# ZDI-25-737: (Pwn2Own) QNAP QHora-322 do_fetch Improper Certificate Validation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-737
- **ZDI-CAN:** ZDI-CAN-25530
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-737/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise transport security on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the do_fetch method. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
