# ZDI-21-195: ISC BIND TKEY Query Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-195
- **ZDI-CAN:** ZDI-CAN-12302
- **Date:** 2021-02-24
- **CVE:** CVE-2020-8625
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ISC
- **Affected Products:** BIND
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-195/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ISC BIND. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of TKEY queries. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the "bind" user.

## Additional Details

https://kb.isc.org/docs/cve-2020-8625

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
