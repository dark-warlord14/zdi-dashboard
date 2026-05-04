# ZDI-21-1298: Ivanti Avalanche JNLP File Improper Access Control Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1298
- **ZDI-CAN:** ZDI-CAN-14123
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42124
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1298/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of JNLP files. The issue results from improper access control. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 6.3.3.

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
