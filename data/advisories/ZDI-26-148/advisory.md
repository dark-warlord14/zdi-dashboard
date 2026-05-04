# ZDI-26-148: Trend Micro Apex Central Improper Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-148
- **ZDI-CAN:** ZDI-CAN-26039
- **Date:** 2026-03-03
- **CVE:** CVE-2025-71209
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Elias Martinez (filenotfound - https://www.linkedin.com/in/eli-martinez07/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-148/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the management console. The issue results from incorrect implementation of the authentication algorithm. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0022071

## Disclosure Timeline

- 2025-03-19 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
