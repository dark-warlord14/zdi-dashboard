# ZDI-25-202: Fortinet FortiWeb cgi_xmlprotection_xmlschemafile_post Directory Traversal Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-202
- **ZDI-CAN:** ZDI-CAN-25559
- **Date:** 2025-04-07
- **CVE:** CVE-2024-55597
- **CVSS:** 5.5
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-202/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary XML schema files on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the cgi_xmlprotection_xmlschemafile_post function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create XML schema files in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.com/psirt/FG-IR-24-439

## Disclosure Timeline

- 2024-10-16 - Vulnerability reported to vendor
- 2025-04-07 - Coordinated public release of advisory
- 2025-04-07 - Advisory Updated
