# ZDI-25-892: Microsoft .NET IsTypeAuthorized Deserialization of Untrusted Data Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-892
- **ZDI-CAN:** ZDI-CAN-24739
- **Date:** 2025-09-09
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-892/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft .NET. Interaction with the .NET framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementations of the IsTypeAuthorized method on .NET workflow classes. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Fixed in versions SP2016, SP2019, and SPSE Sept 2024 PU

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2025-09-09 - Coordinated public release of advisory
- 2025-09-09 - Advisory Updated
