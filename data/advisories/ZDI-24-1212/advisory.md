# ZDI-24-1212: Ivanti Endpoint Manager ImportXml XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1212
- **ZDI-CAN:** ZDI-CAN-24046
- **Date:** 2024-09-11
- **CVE:** CVE-2024-37397
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1212/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of ImportXml method. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-September-2024-for-EPM-2024-and-EPM-2022

## Disclosure Timeline

- 2024-06-28 - Vulnerability reported to vendor
- 2024-09-11 - Coordinated public release of advisory
- 2024-09-11 - Advisory Updated
