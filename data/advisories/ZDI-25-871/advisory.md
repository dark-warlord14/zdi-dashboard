# ZDI-25-871: (Pwn2Own) QNAP QHora-322 miro_webserver_lib_RunExecBash Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-871
- **ZDI-CAN:** ZDI-CAN-25847
- **Date:** 2025-08-26
- **CVE:** CVE-2024-13087
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** nella17 (@nella17tw), working with DEVCORE Internship Program, and DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-871/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP QHora-322 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the miro_webserver_lib_RunExecBash function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-25-15

## Disclosure Timeline

- 2024-12-13 - Vulnerability reported to vendor
- 2025-08-26 - Coordinated public release of advisory
- 2025-08-26 - Advisory Updated
