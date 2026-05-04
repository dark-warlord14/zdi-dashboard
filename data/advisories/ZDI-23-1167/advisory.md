# ZDI-23-1167: Ivanti Avalanche decodeToMap XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1167
- **ZDI-CAN:** ZDI-CAN-21030
- **Date:** 2023-08-23
- **CVE:** CVE-2023-32567
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:L
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1167/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the decodeToMap method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2023-08-23 - Coordinated public release of advisory
