# ZDI-24-1510: Ivanti Endpoint Manager GetComputerID SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1510
- **ZDI-CAN:** ZDI-CAN-25414
- **Date:** 2024-11-13
- **CVE:** CVE-2024-50330
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1510/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the GetComputerID method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-November-2024-for-EPM-2024-and-EPM-2022

## Disclosure Timeline

- 2024-10-08 - Vulnerability reported to vendor
- 2024-11-13 - Coordinated public release of advisory
- 2024-11-13 - Advisory Updated
