# ZDI-24-1123: (Pwn2Own) QNAP TS-464 Netmgr Endpoint Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1123
- **ZDI-CAN:** ZDI-CAN-22458
- **Date:** 2024-08-12
- **CVE:** CVE-2024-32765
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. An attacker must first obtain the ability to make modifications to device configuration in order to exploit this vulnerability. The specific flaw exists within the legacy_api endpoints. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-14

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-08-12 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
