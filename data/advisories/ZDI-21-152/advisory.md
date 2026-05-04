# ZDI-21-152: Cisco Multiple Routers Authorization Header Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-152
- **ZDI-CAN:** ZDI-CAN-11694
- **Date:** 2021-02-09
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Multiple Routers
- **Credit:** T Shiomitsu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-152/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV16x and RV26x routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of file downloads. When parsing the Authorization header, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in version 1.0.01.02

## Disclosure Timeline

- 2020-10-21 - Vulnerability reported to vendor
- 2021-02-09 - Coordinated public release of advisory
