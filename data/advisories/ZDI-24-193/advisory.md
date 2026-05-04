# ZDI-24-193: Sante PACS Server Token Endpoint SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-193
- **ZDI-CAN:** ZDI-CAN-21539
- **Date:** 2024-02-23
- **CVE:** CVE-2024-1863
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server
- **Credit:** Florent Saudel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-193/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of HTTP requests on port 3000. When parsing the token parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

fixed in version 3.3.6

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2024-02-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
