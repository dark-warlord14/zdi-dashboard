# ZDI-25-094: Fortinet FortiWeb cgi_grpc_idl_file_post Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-094
- **ZDI-CAN:** ZDI-CAN-25182
- **Date:** 2025-02-24
- **CVE:** CVE-2024-50567
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-094/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the cgi_grpc_idl_file_post function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-24-438

## Disclosure Timeline

- 2024-10-16 - Vulnerability reported to vendor
- 2025-02-24 - Coordinated public release of advisory
- 2025-02-24 - Advisory Updated
