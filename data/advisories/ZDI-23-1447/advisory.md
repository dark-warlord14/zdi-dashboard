# ZDI-23-1447: Microsoft Exchange ExFileLog Deserialization of Untrusted Data Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1447
- **ZDI-CAN:** ZDI-CAN-21487
- **Date:** 2023-09-19
- **CVE:** CVE-2023-36757
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1447/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the lack of protection against deserialization of the ExFileLog class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36757

## Disclosure Timeline

- 2023-06-27 - Vulnerability reported to vendor
- 2023-09-19 - Coordinated public release of advisory
