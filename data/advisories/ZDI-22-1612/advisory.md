# ZDI-22-1612: ManageEngine ServiceDesk Plus getAsDoc XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1612
- **ZDI-CAN:** ZDI-CAN-18280
- **Date:** 2022-11-21
- **CVE:** CVE-2022-40771
- **CVSS:** 5.5
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** ManageEngine
- **Affected Products:** ServiceDesk Plus
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1612/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ManageEngine ServiceDesk Plus. Authentication is required to exploit this vulnerability. The specific flaw exists within the getAsDoc function. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM or to create a denial-of-service condition on the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/products/service-desk/CVE-2022-40771.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
