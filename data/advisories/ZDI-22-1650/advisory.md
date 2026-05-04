# ZDI-22-1650: Microsoft Exchange OrganizationInitializationDefinition External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1650
- **ZDI-CAN:** ZDI-CAN-18958
- **Date:** 2022-11-22
- **CVE:** CVE-2022-41082
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1650/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the OrganizationInitializationDefinition class. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082

## Disclosure Timeline

- 2022-09-29 - Vulnerability reported to vendor
- 2022-11-22 - Coordinated public release of advisory
