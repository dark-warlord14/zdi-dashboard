# ZDI-21-1324: Ivanti Avalanche EnterpriseServer Service Exposed Dangerous Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1324
- **ZDI-CAN:** ZDI-CAN-15137
- **Date:** 2021-11-19
- **CVE:** CVE-2021-42128
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1324/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SetUser class. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version Avalanche 6.3.3

## Disclosure Timeline

- 2021-09-22 - Vulnerability reported to vendor
- 2021-11-19 - Coordinated public release of advisory
- 2024-02-16 - Advisory Updated
