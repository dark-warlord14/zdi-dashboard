# ZDI-23-1048: (0Day) Inductive Automation Ignition SimpleXMLReader XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1048
- **ZDI-CAN:** ZDI-CAN-17571
- **Date:** 2023-08-08
- **CVE:** CVE-2023-39472
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1048/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Inductive Automation Ignition. Authentication is required to exploit this vulnerability. The specific flaw exists within the SimpleXMLReader class. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the SYSTEM.

## Additional Details

06/01/22 – ZDI reported the vulnerability to the vendor. 06/02/22 – The vendor acknowledged the report. 07/18/23 – The ZDI asked for an update. 07/21/23 – The vendor states that the case is still in active development. 08/01/23 – ZDI informed the vendor that the case will be published as a zero-day advisory on 08/08/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-06-01 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2023-08-08 - Advisory Updated
