# ZDI-21-454: Oracle WebLogic Server T3 Protocol Deserialization of Untrusted Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-454
- **ZDI-CAN:** ZDI-CAN-12492
- **Date:** 2021-04-22
- **CVE:** CVE-2021-2211
- **CVSS:** 4.9
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic Server
- **Credit:** Quynh Le of VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-454/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Oracle WebLogic Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of the T3 protocol. Crafted data in a T3 protocol message can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2021.html

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-04-22 - Coordinated public release of advisory
