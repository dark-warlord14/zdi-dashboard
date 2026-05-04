# ZDI-20-128: Oracle WebLogic Server T3 Protocol Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-128
- **ZDI-CAN:** ZDI-CAN-9020
- **Date:** 2020-01-15
- **CVE:** CVE-2020-2555
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** WebLogic
- **Credit:** Jang from VNPT ISC
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle WebLogic. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the T3 protocol on TCP port 7001. When deserializing objects embedded with T3 protocol messages, the server allows deserialization of classes that may lead to arbitrary code execution. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2020.html

## Disclosure Timeline

- 2019-10-22 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
