# ZDI-26-216: (Pwn2Own) QNAP TS-453E smbd domain_name Argument Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-216
- **ZDI-CAN:** ZDI-CAN-28353
- **Date:** 2026-03-17
- **CVE:** CVE-2025-62847
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** YingMuo (@YingMuo) of DEVCORE Research Team, HexRabbit (@h3xr4bb1t) of DEVCORE Research Team, LJP (@ljp_tw) of DEVCORE Research Team, nella17 (@nella17tw), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-216/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP TS-453E devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of of the domain_name parameter. The issue results from the lack of proper validation of a user-supplied string before using it to prepare an argument for a system call. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-45

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-17 - Coordinated public release of advisory
- 2026-03-17 - Advisory Updated
