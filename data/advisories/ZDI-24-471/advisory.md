# ZDI-24-471: (Pwn2Own) QNAP TS-464 authLogin SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-471
- **ZDI-CAN:** ZDI-CAN-22494
- **Date:** 2024-05-19
- **CVE:** CVE-2024-21901
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** LJP (@ljp_tw) and YingMuo (@YingMuo), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-471/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the authLogin endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
