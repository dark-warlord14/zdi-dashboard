# ZDI-21-657: ISC BIND TKEY Query Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-657
- **ZDI-CAN:** ZDI-CAN-13347
- **Date:** 2021-06-07
- **CVE:** CVE-2021-25216
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ISC
- **Affected Products:** BIND
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-657/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ISC BIND. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of TKEY queries. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the "bind" user.

## Additional Details

ISC has issued an update to correct this vulnerability. More details can be found at: https://kb.isc.org/v1/docs/cve-2021-25216

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-06-07 - Coordinated public release of advisory
