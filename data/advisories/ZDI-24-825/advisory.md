# ZDI-24-825: (Pwn2Own) QNAP TS-464 Log Upload Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-825
- **ZDI-CAN:** ZDI-CAN-22463
- **Date:** 2024-06-21
- **CVE:** CVE-2023-51364
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Le Huu Quang Linh, Do Minh Tuan & Billy Jheng Bing-Jhong of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-825/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of log uploads. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-14

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
