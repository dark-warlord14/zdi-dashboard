# ZDI-25-266: Apache ActiveMQ NMS Body Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-266
- **ZDI-CAN:** ZDI-CAN-22235
- **Date:** 2025-04-30
- **CVE:** CVE-2025-29953
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** ActiveMQ
- **Credit:** g7shot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-266/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apache ActiveMQ NMS. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the Body accessor method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://lists.apache.org/thread/vc1sj9y3056d3kkhcvrs9fyw5w8kpmlx

## Disclosure Timeline

- 2023-11-28 - Vulnerability reported to vendor
- 2025-04-30 - Coordinated public release of advisory
- 2025-04-30 - Advisory Updated
