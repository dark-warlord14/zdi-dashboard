# ZDI-25-918: Fortinet FortiWeb _cmf_get_config_file_path Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-918
- **ZDI-CAN:** ZDI-CAN-27382
- **Date:** 2025-09-26
- **CVE:** CVE-2025-53609
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Jason McFadyen of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-918/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the _cmf_get_config_file_path method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-25-512

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-09-26 - Coordinated public release of advisory
- 2025-10-06 - Advisory Updated
