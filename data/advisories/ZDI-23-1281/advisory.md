# ZDI-23-1281: Apache ActiveMQ NMS Body Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1281
- **ZDI-CAN:** ZDI-CAN-19459
- **Date:** 2023-08-29
- **CVE:** N/A
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** ActiveMQ
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1281/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apache ActiveMQ NMS. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the Body accessor method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://www.mail-archive.com/dev@activemq.apache.org/msg68832.html

## Disclosure Timeline

- 2022-11-16 - Vulnerability reported to vendor
- 2023-08-29 - Coordinated public release of advisory
- 2023-11-21 - Advisory Updated
