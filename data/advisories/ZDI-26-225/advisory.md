# ZDI-26-225: (Pwn2Own) Samsung Galaxy S25 Samsung Account Open Redirect Security Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-225
- **ZDI-CAN:** ZDI-CAN-28457
- **Date:** 2026-03-23
- **CVE:** CVE-2025-58487
- **CVSS:** 5.6
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S25
- **Credit:** Ken Gannon / 伊藤 剣 (@yogehi) of Mobile Hacking Lab, and Dimitrios Valsamaras (@Ch0pin)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-225/
## Vulnerability Details

This vulnerability allows remote attackers to bypass security on affected installations of Samsung Galaxy S25. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Samsung Account application. An attacker can force a redirection to a site that serves malicious content. An attacker can leverage this vulnerability to start arbitrary Android exported activites.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2025&month=12

## Disclosure Timeline

- 2025-11-20 - Vulnerability reported to vendor
- 2026-03-23 - Coordinated public release of advisory
- 2026-03-23 - Advisory Updated
