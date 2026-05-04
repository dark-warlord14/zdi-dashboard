# ZDI-20-878: IBM WebSphere Application Server SOAP Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-878
- **ZDI-CAN:** ZDI-CAN-10767
- **Date:** 2020-07-20
- **CVE:** CVE-2020-4464
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** WebSphere
- **Credit:** tint0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-878/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IBM WebSphere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the SOAP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6250059

## Disclosure Timeline

- 2020-04-22 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
