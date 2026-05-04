# ZDI-25-743: (Pwn2Own) QNAP TS-464 qnap_exec Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-743
- **ZDI-CAN:** ZDI-CAN-25585
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Corentin "@OnlyTheDuck" BAYET from REverse Tactics
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-743/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of QNAP TS-464 devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the qnap_exec function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
