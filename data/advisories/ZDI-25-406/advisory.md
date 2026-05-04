# ZDI-25-406: SolarWinds Serv-U FTP Service Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-406
- **ZDI-CAN:** ZDI-CAN-25087
- **Date:** 2025-06-17
- **CVE:** CVE-2024-45711
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Serv-U
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-406/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Serv-U. Authentication is required to exploit this vulnerability. The specific flaw exists within the FTP service, which listens on TCP port 21 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_15-5_release_notes.htm#link3

## Disclosure Timeline

- 2024-09-04 - Vulnerability reported to vendor
- 2025-06-17 - Coordinated public release of advisory
- 2025-06-17 - Advisory Updated
