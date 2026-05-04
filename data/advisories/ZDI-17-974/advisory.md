# ZDI-17-974: Quest NetVault Backup Server Process Manager Service NVBUEventHistory Get Method SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-974
- **ZDI-CAN:** ZDI-CAN-4223
- **Date:** 2017-12-15
- **CVE:** CVE-2017-17412
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Quest
- **Affected Products:** NetVault Backup
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-974/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Quest NetVault Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of GET method requests. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code in the context of the underlying database.

## Additional Details

Fixed in NVBU 11.4.5

## Disclosure Timeline

- 2017-12-06 - Vulnerability reported to vendor
- 2017-12-15 - Coordinated public release of advisory
