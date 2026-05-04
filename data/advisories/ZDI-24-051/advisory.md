# ZDI-24-051: Trend Micro Apex Central Cross-Site Scripting Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-051
- **ZDI-CAN:** ZDI-CAN-21447
- **Date:** 2024-01-11
- **CVE:** CVE-2023-52330
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex Central
- **Credit:** Elias Martinez (filenotfound - https://www.linkedin.com/in/eli-martinez07/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-051/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro Apex Central. Authentication is required to exploit this vulnerability. The specific flaw exists within the Policy Management functionality. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000296153?language=en_US

## Disclosure Timeline

- 2023-09-13 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
