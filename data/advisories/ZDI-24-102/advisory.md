# ZDI-24-102: Allegra SiteConfigAction Improper Access Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-102
- **ZDI-CAN:** ZDI-CAN-22512
- **Date:** 2024-02-09
- **CVE:** CVE-2023-51644
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-102/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Allegra. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of Struts. The issue results from improper access control. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://www.trackplus.com/en/service/release-notes-reader/7-5-1-release-notes-2.html

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
