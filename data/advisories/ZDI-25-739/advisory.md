# ZDI-25-739: (Pwn2Own) QNAP QHora-322 Improper Restriction of Communication Channel to Intended Endpoints Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-739
- **ZDI-CAN:** ZDI-CAN-25634
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-739/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP QHora-322 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SSH daemon. The issue results from exposing SSH on the WAN side of the router by installing a debug firmware build, which an attacker can accomplish by abusing other vulnerabilities. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
