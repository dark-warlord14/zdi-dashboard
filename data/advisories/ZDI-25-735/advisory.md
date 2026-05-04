# ZDI-25-735: (Pwn2Own) QNAP QHora-322 local_pwd_reset HTTP Request Smuggling Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-735
- **ZDI-CAN:** ZDI-CAN-25631
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:N
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-735/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to smuggle arbitrary HTTP requests on affected installations of QNAP QHora-322 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the local_pwd_reset endpoint. The issue results from the inconsistent parsing of terminators of HTTP headers. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
