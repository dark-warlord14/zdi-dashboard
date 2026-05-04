# ZDI-24-1206: Microsoft SharePoint SPAutoSerializingObject Deserialization of Untrusted Data Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1206
- **ZDI-CAN:** ZDI-CAN-24482
- **Date:** 2024-09-10
- **CVE:** CVE-2024-43466
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1206/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the SPAutoSerializingObject class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43466

## Disclosure Timeline

- 2024-06-26 - Vulnerability reported to vendor
- 2024-09-10 - Coordinated public release of advisory
- 2024-09-10 - Advisory Updated
