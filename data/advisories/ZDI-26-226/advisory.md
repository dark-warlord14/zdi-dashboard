# ZDI-26-226: (0Day) Microsoft Azure MCP AzureCliService Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-226
- **ZDI-CAN:** ZDI-CAN-28042
- **Date:** 2026-03-24
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Alfredo Oliveira and David Fiser of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Azure. Authentication is not required to exploit this vulnerability. The specific flaw exists within the azure-cli-mcp component. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the MCP server.

## Additional Details

09/10/25 – ZDI submitted the report to the vendor 09/10/25 – the vendor acknowledged the report 10/24/25 – the vendor rated the severity of the vulnerability to be Moderate 03/09/26 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-09-10 - Vulnerability reported to vendor
- 2026-03-24 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
