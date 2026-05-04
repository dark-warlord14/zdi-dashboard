# ZDI-23-1637: Microsoft Exchange IsUNCPath Improper Input Validation NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1637
- **ZDI-CAN:** ZDI-CAN-21983
- **Date:** 2023-11-15
- **CVE:** CVE-2023-36035
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1637/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the IsUNCPath method. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to relay NTLM credentials in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36035

## Disclosure Timeline

- 2023-08-25 - Vulnerability reported to vendor
- 2023-11-15 - Coordinated public release of advisory
