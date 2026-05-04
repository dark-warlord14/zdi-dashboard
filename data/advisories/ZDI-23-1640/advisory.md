# ZDI-23-1640: Microsoft Exchange TransportConfigContainer Deserialization of Untrusted Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1640
- **ZDI-CAN:** ZDI-CAN-21958
- **Date:** 2023-11-15
- **CVE:** CVE-2023-36050
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1640/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information or relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the SerializationTypeConverter class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM or to relay NTLM credentials.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36050

## Disclosure Timeline

- 2023-08-16 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
