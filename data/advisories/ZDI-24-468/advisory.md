# ZDI-24-468: Sante PACS Server PG Patient Query SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-468
- **ZDI-CAN:** ZDI-CAN-21579
- **Date:** 2024-05-17
- **CVE:** CVE-2023-51637
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sante
- **Affected Products:** PACS Server PG
- **Credit:** Guillaume CHANTREL, Florent Saudel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sante PACS Server PG. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the DICOM service, which listens on TCP port 11122 by default. When parsing the NAME element of the PATIENT record, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Fixed in version 3.3.7 https://www.santesoft.com/win/sante-pacs-server-pg/whats_new.html

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2024-05-17 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
