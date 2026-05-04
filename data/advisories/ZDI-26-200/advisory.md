# ZDI-26-200: (Pwn2Own) QNAP TS-453E nvrlog_event_add msg SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-200
- **ZDI-CAN:** ZDI-CAN-28436
- **Date:** 2026-03-16
- **CVE:** CVE-2025-62849
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-453E
- **Credit:** YingMuo (@YingMuo) of DEVCORE Research Team, HexRabbit (@h3xr4bb1t) of DEVCORE Research Team, LJP (@ljp_tw) of DEVCORE Research Team, nella17 (@nella17tw), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-200/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-453E devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the msg parameter provided to the nvrlog_event_add endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-45

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-17 - Advisory Updated
