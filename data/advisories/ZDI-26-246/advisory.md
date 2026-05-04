# ZDI-26-246: (0Day) aws-mcp-server Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-246
- **ZDI-CAN:** ZDI-CAN-27968
- **Date:** 2026-03-30
- **CVE:** CVE-2026-5058
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** aws-mcp-server
- **Affected Products:** aws-mcp-server
- **Credit:** Alfredo Oliveira and David Fiser of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-246/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of aws-mcp-server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the allowed commands list. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the MCP server.

## Additional Details

09/03/25 – ZDI submitted the report to the vendor 10/27/25 – ZDI asked to confirm the receipt of the report 11/06/25 – ZDI asked for updates 12/14/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory 12/15/25 – The vendor rejected the vulnerability 02/20/26 – ZDI provided more information 03/09/26 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-09-03 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
