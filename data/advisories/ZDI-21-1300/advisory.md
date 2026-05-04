# ZDI-21-1300: Ivanti Avalanche User Management Improper Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1300
- **ZDI-CAN:** ZDI-CAN-14188
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42126
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1300/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the userManagement.jsf page. The issue results from improper authentication. An attacker can leverage this vulnerability to escalate privileges to the level of admin.

## Additional Details

Fixed in version 6.3.3.

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
