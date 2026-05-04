# ZDI-25-760: (Pwn2Own) QNAP TS-464 rsync Daemon Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-760
- **ZDI-CAN:** ZDI-CAN-25536
- **Date:** 2025-07-31
- **CVE:** CVE-2024-50388
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Team Viettel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-760/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-464 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the provided username and password during authentication. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-41

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
