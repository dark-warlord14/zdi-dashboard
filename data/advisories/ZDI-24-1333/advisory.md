# ZDI-24-1333: NVIDIA Onyx Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1333
- **ZDI-CAN:** ZDI-CAN-24764
- **Date:** 2024-10-09
- **CVE:** CVE-2024-0113
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NVIDIA
- **Affected Products:** Onyx
- **Credit:** Lachlan Davidson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1333/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NVIDIA Onyx switches. Authentication is not required to exploit this vulnerability. The specific flaw exists within the /admin/launch endpoint. When parsing the script query parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

NVIDIA has issued an update to correct this vulnerability. More details can be found at: https://nvidia.custhelp.com/app/answers/detail/a_id/5563

## Disclosure Timeline

- 2024-08-20 - Vulnerability reported to vendor
- 2024-10-09 - Coordinated public release of advisory
- 2024-10-09 - Advisory Updated
