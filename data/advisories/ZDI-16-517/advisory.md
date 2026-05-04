# ZDI-16-517: AlienVault Unified Security Management Remote Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-517
- **ZDI-CAN:** ZDI-CAN-3976
- **Date:** 2016-09-19
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** Peter Lapp (lappsec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-517/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication requirements on vulnerable installations of AlienVault Unified Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the logcheck function in session.inc. By providing a specific value as a user-agent, an attacker can bypass authentication to a number of pages. In addition to viewing information, it's possible to modify the application and achieve arbitrary code execution as root.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/7765/alienvault-v5-3-1-hotfix

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2016-09-19 - Coordinated public release of advisory
