# ZDI-24-827: (Pwn2Own) QNAP TS-464 username Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-827
- **ZDI-CAN:** ZDI-CAN-22497
- **Date:** 2024-06-21
- **CVE:** CVE-2024-32766
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Tri and Bien Pham (@bienpnn) from Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-827/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the username parameter. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
