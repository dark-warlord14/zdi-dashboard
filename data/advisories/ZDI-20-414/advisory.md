# ZDI-20-414: Advantech WebAccess/NMS UsersInputAction Missing Authentication for Critical Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-414
- **ZDI-CAN:** ZDI-CAN-9769
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10625
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-414/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the usersInputAction.action endpoint. Authentication is missing for the critical function of creating new administrator accounts. An attacker can leverage this vulnerability to create new accounts, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
