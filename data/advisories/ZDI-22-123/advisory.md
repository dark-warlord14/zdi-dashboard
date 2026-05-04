# ZDI-22-123: Oracle Business Intelligence ReportTemplateService XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-123
- **ZDI-CAN:** ZDI-CAN-15063
- **Date:** 2022-01-21
- **CVE:** CVE-2022-21346
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-123/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ReportTemplateService endpoint, which listens on TCP port 9502 by default. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2022.html

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2022-01-21 - Coordinated public release of advisory
