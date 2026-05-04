# ZDI-17-983: Quest NetVault Backup Server Process Manager Service NVBUPolicy Get Method SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-983
- **ZDI-CAN:** ZDI-CAN-4229
- **Date:** 2017-12-15
- **CVE:** CVE-2017-17418
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Quest
- **Affected Products:** NetVault Backup
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-983/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Quest NetVault Backup. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of NVBUPolicy Get method requests. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the underlying database.

## Additional Details

Fixed in NVBU 11.4.5

## Disclosure Timeline

- 2017-12-06 - Vulnerability reported to vendor
- 2017-12-15 - Coordinated public release of advisory
