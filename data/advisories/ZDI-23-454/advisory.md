# ZDI-23-454: Ivanti Avalanche EnterpriseServer GetSettings Exposed Dangerous Method Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-454
- **ZDI-CAN:** ZDI-CAN-17750
- **Date:** 2023-04-24
- **CVE:** CVE-2023-28126
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-454/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the GetSettings class. The issue results from the exposure of a dangerous method or function to unprivileged users. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/New-Avalanche-Landing-Page?language=en_US

## Disclosure Timeline

- 2022-07-07 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
