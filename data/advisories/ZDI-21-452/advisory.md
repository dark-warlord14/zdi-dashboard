# ZDI-21-452: Oracle Business Intelligence APSWebModule Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-452
- **ZDI-CAN:** ZDI-CAN-11709
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2244
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** peterjson of RedTeam@VNG Corporation
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-452/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within APSWebModule. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2020-12-23 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
