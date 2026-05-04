# ZDI-26-270: TrendAI Apex One Console Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-270
- **ZDI-CAN:** ZDI-CAN-27976
- **Date:** 2026-04-15
- **CVE:** CVE-2025-54987
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TrendAI
- **Affected Products:** Apex One
- **Credit:** Charles Yang @ CoreCloud Tech.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-270/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Apex One. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Apex One console, which listens on TCP ports 8080 and 4343 by default. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of IUSR.

## Additional Details

TrendAI has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0022458

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
