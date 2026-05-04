# ZDI-26-020: (0Day) Ollama MCP Server execAsync Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-020
- **ZDI-CAN:** ZDI-CAN-27683
- **Date:** 2026-01-09
- **CVE:** CVE-2025-15063
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ollama MCP Server
- **Affected Products:** Ollama MCP Server
- **Credit:** Peter Girnus (@gothburz) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ollama MCP Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the execAsync method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

07/31/25 – ZDI requested the vendor’s PSIRT contacts 11/10/25 – ZDI asked for updates 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-22 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
