# ZDI-23-231: Trend Micro TXOne StellarOne Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-231
- **ZDI-CAN:** ZDI-CAN-18848
- **Date:** 2023-03-17
- **CVE:** CVE-2023-25069
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Trend Micro
- **Affected Products:** TXOne StellarOne
- **Credit:** Elias Martinez (filenotfound - https://www.linkedin.com/in/eli-martinez07/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-231/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro TXOne StellarOne. Authentication is required to exploit this vulnerability. The specific flaw exists within the Account endpoint. The issue results from the lack of proper access control. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000292486

## Disclosure Timeline

- 2022-11-04 - Vulnerability reported to vendor
- 2023-03-17 - Coordinated public release of advisory
- 2023-03-17 - Advisory Updated
