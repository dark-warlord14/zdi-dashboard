# ZDI-24-509: Ivanti Endpoint Manager GetDBPatches SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-509
- **ZDI-CAN:** ZDI-CAN-23516
- **Date:** 2024-05-24
- **CVE:** CVE-2024-29826
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-509/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the GetDBPatches method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-May-2024?language=en_US

## Disclosure Timeline

- 2024-04-03 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
