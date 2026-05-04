# ZDI-20-114: Cisco Data Center Network Manager getInventoryIslList XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-114
- **ZDI-CAN:** ZDI-CAN-9247
- **Date:** 2020-01-03
- **CVE:** CVE-2019-15983
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** Data Center Network Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-114/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco Data Center Network Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the getInventoryIslList SOAP endpoint of DashboardWSService/DashboardWS. Due to the improper restriction of XML External Entity (XXE) references, a specially crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker could leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20200102-dcnm-xml-ext-entity

## Disclosure Timeline

- 2019-10-22 - Vulnerability reported to vendor
- 2020-01-03 - Coordinated public release of advisory
