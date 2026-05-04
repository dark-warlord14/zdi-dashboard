# ZDI-23-1339: Synology RT6600ax WEB API Endpoint Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1339
- **ZDI-CAN:** ZDI-CAN-19741
- **Date:** 2023-09-07
- **CVE:** CVE-2023-41738
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Synology
- **Affected Products:** RT6600ax
- **Credit:** Discovered by: Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1339/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Synology RT6600ax routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the WEB API endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Synology has issued an update to correct this vulnerability. More details can be found at: https://www.synology.com/en-global/security/advisory/Synology_SA_23_10

## Disclosure Timeline

- 2022-12-02 - Vulnerability reported to vendor
- 2023-09-07 - Coordinated public release of advisory
