# ZDI-20-690: IBM WebSphere Application Server IIOP Deserialization of Untrusted Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-690
- **ZDI-CAN:** ZDI-CAN-10756
- **Date:** 2020-06-05
- **CVE:** CVE-2020-4449
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** WebSphere
- **Credit:** tint0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-690/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of IBM WebSphere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the IIOP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6220296

## Disclosure Timeline

- 2020-04-17 - Vulnerability reported to vendor
- 2020-06-05 - Coordinated public release of advisory
