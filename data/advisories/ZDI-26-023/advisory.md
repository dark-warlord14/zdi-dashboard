# ZDI-26-023: (0Day) MCP Manager for Claude Desktop execute-command Command Injection Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-023
- **ZDI-CAN:** ZDI-CAN-27810
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0757
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** MCP Manager for Claude Desktop
- **Affected Products:** MCP Manager for Claude Desktop
- **Credit:** Peter Girnus (@gothburz), Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-023/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the sandbox on affected installations of MCP Manager for Claude Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MCP config objects. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escape the sandbox and execute arbitrary code in the context of the current process at medium integrity.

## Additional Details

07/31/25 – ZDI submitted the reports to the vendor 11/10/25 – ZDI asked for updates 12/16/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-31 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
