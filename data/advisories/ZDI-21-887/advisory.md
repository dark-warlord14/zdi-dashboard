# ZDI-21-887: Oracle Business Intelligence DOMParser XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-887
- **ZDI-CAN:** ZDI-CAN-13067
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2401
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** Jang Laptop of VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-887/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DOMParser endpoint, which listens on TCP port 9502 by default. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-03-24 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
