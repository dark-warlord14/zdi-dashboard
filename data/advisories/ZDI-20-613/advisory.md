# ZDI-20-613: Advantech WebAccess/SCADA BwWebSvc IOCTL 0x00013c71 SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-613
- **ZDI-CAN:** ZDI-CAN-9882
- **Date:** 2020-05-08
- **CVE:** CVE-2020-12014
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/SCADA
- **Credit:** Z0mb1E
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-613/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/SCADA. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of IOCTL 0x00013c71 in BwWebSvc.dll. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-128-36

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-05-08 - Coordinated public release of advisory
