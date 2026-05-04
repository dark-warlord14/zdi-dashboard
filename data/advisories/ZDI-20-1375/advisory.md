# ZDI-20-1375: Trend Micro Apex One Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1375
- **ZDI-CAN:** ZDI-CAN-11237
- **Date:** 2020-11-22
- **CVE:** CVE-2020-28576
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Filenotfound
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1375/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Trend Micro Apex One. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web console, which listens on TCP port 4343 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information from the application.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000281949

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-11-22 - Coordinated public release of advisory
