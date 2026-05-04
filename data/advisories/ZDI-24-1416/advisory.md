# ZDI-24-1416: Schneider Electric EcoStruxure Data Center Expert Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1416
- **ZDI-CAN:** ZDI-CAN-23489
- **Date:** 2024-10-17
- **CVE:** CVE-2024-8530
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Data Center Expert
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1416/
## Vulnerability Details

The vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric EcoStruxure Data Center Expert. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of log files. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose sensitive information, leading to further compromise.

## Additional Details

https://www.cisa.gov/news-events/ics-advisories/icsa-24-289-02 https://community.se.com/t5/Data-Center-Expert-release-notes/EcoStruxure-IT-Data-Center-Expert-8-2-0-release-notes/ta-p/463789

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-18 - Advisory Updated
