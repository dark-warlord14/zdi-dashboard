# ZDI-24-824: (Pwn2Own) QNAP TS-464 Cloud Utility Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-824
- **ZDI-CAN:** ZDI-CAN-22462
- **Date:** 2024-06-21
- **CVE:** CVE-2024-27124
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-824/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of password reset requests. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
