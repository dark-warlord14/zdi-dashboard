# ZDI-24-1417: Schneider Electric EcoStruxure Data Center Expert Improper Verification of Cryptographic Signature Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1417
- **ZDI-CAN:** ZDI-CAN-23203
- **Date:** 2024-10-17
- **CVE:** CVE-2024-8531
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Data Center Expert
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1417/
## Vulnerability Details

The vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric EcoStruxure Data Center Expert. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of upgrade bundles. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

https://www.cisa.gov/news-events/ics-advisories/icsa-24-289-02 https://community.se.com/t5/Data-Center-Expert-release-notes/EcoStruxure-IT-Data-Center-Expert-8-2-0-release-notes/ta-p/463789

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-18 - Advisory Updated
