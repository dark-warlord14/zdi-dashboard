# ZDI-22-508: Cisco Nexus Dashboard Fabric Controller XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-508
- **ZDI-CAN:** ZDI-CAN-15192
- **Date:** 2022-03-11
- **CVE:** CVE-2015-3269
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Nexus Dashboard Fabric Controller
- **Credit:** kpc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-508/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Nexus Dashboard Fabric Controller. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the AMF protocol. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the fmserver user.

## Additional Details

Fixed in version 11.5(4) or later

## Disclosure Timeline

- 2021-09-10 - Vulnerability reported to vendor
- 2022-03-11 - Coordinated public release of advisory
