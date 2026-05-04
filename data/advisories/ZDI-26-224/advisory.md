# ZDI-26-224: (Pwn2Own) Samsung Galaxy S25 Samsung Account Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-224
- **ZDI-CAN:** ZDI-CAN-28456
- **Date:** 2026-03-23
- **CVE:** CVE-2025-58486
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Samsung
- **Affected Products:** Galaxy S25
- **Credit:** Ken Gannon / 伊藤 剣 (@yogehi) of Mobile Hacking Lab, and Dimitrios Valsamaras (@Ch0pin)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary script on affected installations of Samsung Galaxy S25. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Samsung Account application. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute script in the context of the current WebView.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungmobile.com/serviceWeb.smsb?year=2025&month=12

## Disclosure Timeline

- 2025-11-20 - Vulnerability reported to vendor
- 2026-03-23 - Coordinated public release of advisory
- 2026-03-23 - Advisory Updated
