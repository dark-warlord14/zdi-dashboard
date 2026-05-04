# ZDI-23-1156: Advantech R-SeeNet Use Of Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1156
- **ZDI-CAN:** ZDI-CAN-19580
- **Date:** 2023-08-21
- **CVE:** CVE-2023-2611
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** R-SeeNet
- **Credit:** Esjay (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1156/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Advantech R-SeeNet. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the database. The issue results from the existence of an additional user in the database that is not visible in the web application. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-173-02

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
