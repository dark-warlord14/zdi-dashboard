# ZDI-22-1604: Microsoft Exchange SerializationTypeConverter Deserialization of Untrusted Data NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1604
- **ZDI-CAN:** ZDI-CAN-18882
- **Date:** 2024-10-16
- **CVE:** CVE-2022-41079
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1604/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the SerializationTypeConverter class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to relay NTLM credentials in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41079

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2024-10-16 - Coordinated public release of advisory
- 2024-10-16 - Advisory Updated
