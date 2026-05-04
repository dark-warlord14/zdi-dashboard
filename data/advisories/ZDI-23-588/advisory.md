# ZDI-23-588: Trend Micro Mobile Security for Enterprises widgetforsecurity WFUser Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-588
- **ZDI-CAN:** ZDI-CAN-19722
- **Date:** 2023-05-12
- **CVE:** CVE-2023-32524
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Mobile Security for Enterprises
- **Credit:** Poh Jia Hao of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-588/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Trend Micro Mobile Security for Enterprises. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WFUser class defined within the web/widgetforsecurity path. The issue results from improper implementation of the authentication mechanism. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000293106

## Disclosure Timeline

- 2023-01-19 - Vulnerability reported to vendor
- 2023-05-12 - Coordinated public release of advisory
