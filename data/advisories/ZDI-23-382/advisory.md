# ZDI-23-382: Microsoft SharePoint WSSXmlUrlResolver Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-382
- **ZDI-CAN:** ZDI-CAN-20506
- **Date:** 2023-04-11
- **CVE:** CVE-2023-28288
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-382/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the WSSXmlUrlResolver class. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of IUSR.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28288

## Disclosure Timeline

- 2023-02-14 - Vulnerability reported to vendor
- 2023-04-11 - Coordinated public release of advisory
