# ZDI-23-118: Oracle WebLogic Server ForeignOpaqueReference JNDI Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-118
- **ZDI-CAN:** ZDI-CAN-18409
- **Date:** 2023-02-09
- **CVE:** CVE-2023-21838
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-118/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebLogic Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ForeignOpaqueReference class. The issue results from the lack of proper validation of user-supplied data, which can result in execution of arbitrary Java code. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2023.html

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
