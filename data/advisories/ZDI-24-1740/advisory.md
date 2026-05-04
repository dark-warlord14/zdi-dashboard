# ZDI-24-1740: WSO2 API Manager Exposed Dangerous Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1740
- **ZDI-CAN:** ZDI-CAN-23650
- **Date:** 2024-12-30
- **CVE:** CVE-2024-6914
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WSO2
- **Affected Products:** API Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1740/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of WSO2 API Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the user self-registration process. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

WSO2 has issued an update to correct this vulnerability. More details can be found at: https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2024/WSO2-2024-3561/

## Disclosure Timeline

- 2024-07-18 - Vulnerability reported to vendor
- 2024-12-30 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
