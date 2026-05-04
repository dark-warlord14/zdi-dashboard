# ZDI-25-288: Fortinet FortiWeb cgi_httpcontentrouting_post Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-288
- **ZDI-CAN:** ZDI-CAN-25181
- **Date:** 2025-05-13
- **CVE:** CVE-2025-25254
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiWeb
- **Credit:** Kentaro Kawane of GMO Cybersecurity by Ierae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fortinet FortiWeb. Authentication is required to exploit this vulnerability. The specific flaw exists within the cgi_httpcontentrouting_post function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.com/psirt/FG-IR-24-474

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-05-13 - Coordinated public release of advisory
- 2025-05-13 - Advisory Updated
