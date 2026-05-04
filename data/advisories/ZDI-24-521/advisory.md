# ZDI-24-521: (Pwn2Own) Phoenix Contact CHARX SEC-3100 OCPP charx_pack_logs Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-521
- **ZDI-CAN:** ZDI-CAN-23391
- **Date:** 2024-05-29
- **CVE:** CVE-2024-28136
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** @ByteInsight
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-521/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Phoenix Contact CHARX SEC-3100 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the Charger ID parameter to the Get Diagnostics command. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-019/

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
