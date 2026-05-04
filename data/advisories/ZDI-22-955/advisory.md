# ZDI-22-955: Sante PACS Server SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-955
- **ZDI-CAN:** ZDI-CAN-17331
- **Date:** 2022-07-07
- **CVE:** CVE-2022-2272
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Florent Saudel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-955/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Sante PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the login endpoint. When parsing the username element, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in Sante PACS Server Version 3.0.5 https://www.santesoft.com/win/sante-pacs-server-pg/whats_new.html

## Disclosure Timeline

- 2022-06-06 - Vulnerability reported to vendor
- 2022-07-07 - Coordinated public release of advisory
- 2022-07-07 - Advisory Updated
