# ZDI-26-209: (Pwn2Own) Samsung Galaxy S25 Samsung Members Open Redirect Security Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-209
- **ZDI-CAN:** ZDI-CAN-28455
- **Date:** 2026-03-16
- **CVE:** CVE-2025-21079
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S25
- **Credit:** Ken Gannon / 伊藤 剣 (@yogehi) of Mobile Hacking Lab, and Dimitrios Valsamaras (@Ch0pin)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-209/
## Vulnerability Details

This vulnerability allows remote attackers to bypass security on affected installations of Samsung Galaxy S25. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Samsung Members application. An attacker can force a redirection to a site that serves malicious content. An attacker can leverage this in conjunction with other vulnerabilities to start arbitrary Android exported activites, leading to further compromise.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2025&month=11

## Disclosure Timeline

- 2025-11-18 - Vulnerability reported to vendor
- 2026-03-16 - Coordinated public release of advisory
- 2026-03-16 - Advisory Updated
