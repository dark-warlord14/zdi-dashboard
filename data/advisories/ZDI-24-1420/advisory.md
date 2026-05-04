# ZDI-24-1420: Schneider Electric EcoStruxure Data Center Expert XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1420
- **ZDI-CAN:** ZDI-CAN-23502
- **Date:** 2024-10-18
- **CVE:** CVE-2015-0250
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Schneider Electric
- **Affected Products:** EcoStruxure Data Center Expert
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1420/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Schneider Electric EcoStruxure Data Center Expert. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the exportSvg method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://community.se.com/t5/Data-Center-Expert-release-notes/EcoStruxure-IT-Data-Center-Expert-8-2-0-release-notes/ta-p/463789

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-10-18 - Coordinated public release of advisory
- 2024-10-18 - Advisory Updated
