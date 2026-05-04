# ZDI-21-174: IBM WebSphere EDataGraphImpl Deserialization of Untrusted Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-174
- **ZDI-CAN:** ZDI-CAN-12478
- **Date:** 2021-02-10
- **CVE:** CVE-2021-20353
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** IBM
- **Affected Products:** WebSphere
- **Credit:** r00t4dm at Cloud-Penetrating Arrow Lab and Longofo at Knownsec 404 Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-174/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of IBM WebSphere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the EDataGraphImpl class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6413709

## Disclosure Timeline

- 2020-12-11 - Vulnerability reported to vendor
- 2021-02-10 - Coordinated public release of advisory
