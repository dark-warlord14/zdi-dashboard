# ZDI-25-383: Siemens TeleControl Server Basic VerifyUser SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-383
- **ZDI-CAN:** ZDI-CAN-25914
- **Date:** 2025-06-16
- **CVE:** CVE-2025-27539
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** TeleControl Server Basic
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-383/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens TeleControl Server Basic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the VerifyUser method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of NETWORK SERVICE.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-443402.html

## Disclosure Timeline

- 2025-02-21 - Vulnerability reported to vendor
- 2025-06-16 - Coordinated public release of advisory
- 2025-06-16 - Advisory Updated
