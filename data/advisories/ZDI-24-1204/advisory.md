# ZDI-24-1204: Microsoft SharePoint SPThemes Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1204
- **ZDI-CAN:** ZDI-CAN-23930
- **Date:** 2024-09-10
- **CVE:** CVE-2024-38018
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1204/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of serialized instances of the SPThemes class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38018

## Disclosure Timeline

- 2024-04-12 - Vulnerability reported to vendor
- 2024-09-10 - Coordinated public release of advisory
- 2024-09-10 - Advisory Updated
