# ZDI-24-111: Allegra Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-111
- **ZDI-CAN:** ZDI-CAN-22360
- **Date:** 2024-02-09
- **CVE:** CVE-2023-51638
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-111/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Allegra. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of a database. The issue results from the use of a hardcoded password. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://www.trackplus.com/en/service/release-notes-reader/7-5-1-release-notes-2.html

## Disclosure Timeline

- 2023-11-03 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
