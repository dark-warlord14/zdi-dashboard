# ZDI-21-066: SolarWinds Orion Platform ExportToPDF Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-066
- **ZDI-CAN:** ZDI-CAN-11917
- **Date:** 2021-09-20
- **CVE:** CVE-2020-27870
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Platform
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-066/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of SolarWinds Orion Platform. Authentication is required to exploit this vulnerability. The specific flaw exists within ExportToPDF.aspx. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Fixed in Orion Platform 2020.2.1 Hot Fix 2 - released on 12/15/2020

## Disclosure Timeline

- 2020-10-14 - Vulnerability reported to vendor
- 2021-09-20 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
