# ZDI-23-1794: Schneider Electric APC Easy UPS Online deletePdfReportFile Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1794
- **ZDI-CAN:** ZDI-CAN-21370
- **Date:** 2023-12-15
- **CVE:** CVE-2023-6407
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1794/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Schneider Electric APC Easy UPS Online. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the deletePdfReportFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icaa-23-346-01

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2023-12-15 - Coordinated public release of advisory
