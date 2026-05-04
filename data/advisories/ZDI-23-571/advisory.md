# ZDI-23-571: Microsoft SharePoint AdRotator Improper Input Validation NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-571
- **ZDI-CAN:** ZDI-CAN-20375
- **Date:** 2023-05-10
- **CVE:** CVE-2023-24950
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-571/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the AdRotator WebControl. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to relay NTLM credentials of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24950

## Disclosure Timeline

- 2023-02-10 - Vulnerability reported to vendor
- 2023-05-10 - Coordinated public release of advisory
