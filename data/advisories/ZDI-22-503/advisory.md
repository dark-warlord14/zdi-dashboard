# ZDI-22-503: MyBB Admin Control Panel Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-503
- **ZDI-CAN:** ZDI-CAN-16517
- **Date:** 2022-03-11
- **CVE:** CVE-2022-24734
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MyBB
- **Affected Products:** MyBB
- **Credit:** Cillian Collins
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-503/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MyBB. Authentication is required to exploit this vulnerability. The specific flaw exists within the Control Panel. The issue results from the lack of proper validation of a user-supplied string before using it to construct server-side code. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

MyBB has issued an update to correct this vulnerability. More details can be found at: https://mybb.com/versions/1.8.30/

## Disclosure Timeline

- 2022-03-07 - Vulnerability reported to vendor
- 2022-03-11 - Coordinated public release of advisory
