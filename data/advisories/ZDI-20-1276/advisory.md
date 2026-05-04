# ZDI-20-1276: Oracle WebLogic Server IIOP Protocol Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1276
- **ZDI-CAN:** ZDI-CAN-11453
- **Date:** 2020-10-22
- **CVE:** CVE-2020-14841
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1276/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the IIOP protocol. Crafted data in an IIOP protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2020.html

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-10-22 - Coordinated public release of advisory
