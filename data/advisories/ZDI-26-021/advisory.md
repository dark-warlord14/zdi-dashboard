# ZDI-26-021: (0Day) gemini-mcp-tool execAsync Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-021
- **ZDI-CAN:** ZDI-CAN-27783
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0755
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Gemini MCP Tool
- **Affected Products:** gemini-mcp-tool
- **Credit:** Peter Girnus (@gothburz) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of gemini-mcp-tool. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the execAsync method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

07/25/25 – ZDI submitted the reports to the vendor via a third-party platform 11/10/25 – ZDI asked for updates 12/14/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-25 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
