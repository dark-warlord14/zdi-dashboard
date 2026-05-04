# ZDI-25-095: Fortinet FortiWeb gui_upload_compress_act Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-095
- **ZDI-CAN:** ZDI-CAN-25180
- **Date:** 2025-02-24
- **CVE:** CVE-2024-50569
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the gui_upload_compress_act function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-24-438

## Disclosure Timeline

- 2024-10-16 - Vulnerability reported to vendor
- 2025-02-24 - Coordinated public release of advisory
- 2025-02-24 - Advisory Updated
