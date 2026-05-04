# ZDI-24-1150: Ivanti Avalanche decodeToMap XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1150
- **ZDI-CAN:** ZDI-CAN-22083
- **Date:** 2024-08-15
- **CVE:** CVE-2024-38653
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Lucas Miller of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1150/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the decodeToMap method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-Ivanti-Avalanche-6-4-4-CVE-2024-38652-CVE-2024-38653-CVE-2024-36136-CVE-2024-37399-CVE-2024-37373?language=en_US

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2024-08-15 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
