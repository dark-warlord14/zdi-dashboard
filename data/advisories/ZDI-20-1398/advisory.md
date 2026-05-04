# ZDI-20-1398: Microsoft SharePoint DataFormWebPart Server-Side Include Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1398
- **ZDI-CAN:** ZDI-CAN-11267
- **Date:** 2020-12-04
- **CVE:** CVE-2020-0971
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1398/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft SharePoint Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of web parts of type DataFormWebPart. By specifying a custom DataFormWebPart, an attacker can cause the server to process arbitrary server-side includes. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-0971

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-12-04 - Coordinated public release of advisory
