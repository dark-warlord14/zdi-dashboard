# ZDI-23-1419: Microsoft Exchange ApprovedApplicationCollection Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1419
- **ZDI-CAN:** ZDI-CAN-21498
- **Date:** 2023-09-12
- **CVE:** CVE-2023-36756
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1419/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the lack of protection against deserialization of the ApprovedApplicationCollection class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36756

## Disclosure Timeline

- 2023-06-27 - Vulnerability reported to vendor
- 2023-09-12 - Coordinated public release of advisory
