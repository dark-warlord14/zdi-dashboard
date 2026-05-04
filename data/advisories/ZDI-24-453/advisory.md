# ZDI-24-453: Microsoft SharePoint BaseXmlDataSource XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-453
- **ZDI-CAN:** ZDI-CAN-23586
- **Date:** 2024-05-14
- **CVE:** CVE-2024-30043
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-453/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the BaseXmlDataSource class. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30043

## Disclosure Timeline

- 2024-03-07 - Vulnerability reported to vendor
- 2024-05-14 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
