# ZDI-25-362: Trend Micro Apex One Data Loss Prevention Uncontrolled Search Path Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-362
- **ZDI-CAN:** ZDI-CAN-24571
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49155
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Xavier DANEST - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex One Security Agent. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Data Loss Prevention module. The issue results from loading a DLL from an uncontrolled search path. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019917

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
