# ZDI-22-408: (Pwn2Own) Cisco RV340 Firmware Update Missing Integrity Check Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-408
- **ZDI-CAN:** ZDI-CAN-15611
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20703
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Bien Pham (@bienpnn) from Team Orca of Sea Security (security.sea.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-408/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of firmware updates. The issue results from the lack of proper validation of a firmware image when performing an upgrade. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-11-24 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
