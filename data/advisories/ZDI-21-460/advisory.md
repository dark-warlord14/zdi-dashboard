# ZDI-21-460: Oracle Business Intelligence T3 Protocol Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-460
- **ZDI-CAN:** ZDI-CAN-12609
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2302
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** Quynh Le of VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-460/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the T3 protocol. Crafted data in a T3 protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2021-01-22 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
