# ZDI-23-241: Oracle WebLogic Server IIOP Protocol Deserialization of Untrusted Data Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-241
- **ZDI-CAN:** ZDI-CAN-17322
- **Date:** 2023-03-15
- **CVE:** CVE-2023-21838
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic Server
- **Credit:** r00t4dm
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-241/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Oracle WebLogic Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the IIOP protocol. Crafted data in an IIOP protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2023.html

## Disclosure Timeline

- 2022-07-08 - Vulnerability reported to vendor
- 2023-03-15 - Coordinated public release of advisory
