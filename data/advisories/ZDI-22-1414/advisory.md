# ZDI-22-1414: Adobe ColdFusion Solr Service XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1414
- **ZDI-CAN:** ZDI-CAN-16885
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38419
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1414/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe ColdFusion. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Apache Solr service. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb22-44.html

## Disclosure Timeline

- 2022-05-13 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
