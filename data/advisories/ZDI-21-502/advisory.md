# ZDI-21-502: ISC BIND TKEY Query Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-502
- **ZDI-CAN:** ZDI-CAN-13506
- **Date:** 2021-04-30
- **CVE:** N/A
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** ISC
- **Affected Products:** BIND
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-502/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ISC BIND. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of TKEY queries. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the "bind" user.

## Additional Details

Fixed in BIND 9 releases (9.11.31, 9.16.15)

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-04-30 - Coordinated public release of advisory
