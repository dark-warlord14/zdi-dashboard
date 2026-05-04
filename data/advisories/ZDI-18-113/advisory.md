# ZDI-18-113: Trend Micro Control Manager TMCM_MembershipProvider ValidateUser Password Hash Usage Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-113
- **ZDI-CAN:** ZDI-CAN-5233
- **Date:** 2018-01-10
- **CVE:** CVE-2018-3601
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-113/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Trend Micro Control Manager. User interaction is not required to exploit this vulnerability. The specific flaw exists within the handling of challenges for authentication. The implementation of the challenge allows an attacker to authenticate to the system if they have possession of the password hash but not the password for a user. An attacker can leverage this vulnerability in conjunction with other vulnerabilities to bypass authentication.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119158

## Disclosure Timeline

- 2017-10-17 - Vulnerability reported to vendor
- 2018-01-10 - Coordinated public release of advisory
