# ZDI-21-885: Oracle Business Intelligence BIRemotingServlet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-885
- **ZDI-CAN:** ZDI-CAN-13036
- **Date:** 2021-07-22
- **CVE:** CVE-2021-2456
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** peterjson of RedTeam@VNG Corporation
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-885/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within BIRemotingServlet. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2021.html

## Disclosure Timeline

- 2021-03-18 - Vulnerability reported to vendor
- 2021-07-22 - Coordinated public release of advisory
