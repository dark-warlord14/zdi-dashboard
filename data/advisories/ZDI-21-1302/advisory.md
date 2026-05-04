# ZDI-21-1302: Ivanti Avalanche EnterpriseServer Service SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1302
- **ZDI-CAN:** ZDI-CAN-15200
- **Date:** 2021-11-18
- **CVE:** CVE-2021-42131
- **CVSS:** 9.1
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1302/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SettingsDaoImpl class. A crafted request can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 6.3.3.

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2021-11-18 - Coordinated public release of advisory
- 2022-05-26 - Advisory Updated
