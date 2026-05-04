# ZDI-25-1197: Framelink Figma MCP Server fetchWithRetry Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1197
- **ZDI-CAN:** ZDI-CAN-27877
- **Date:** 2025-12-29
- **CVE:** CVE-2025-15061
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Framelink
- **Affected Products:** Figma MCP Server
- **Credit:** Peter Girnus (@gothburz) and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Framelink Figma MCP Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the fetchWithRetry method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Framelink has issued an update to correct this vulnerability. More details can be found at: https://github.com/GLips/Figma-Context-MCP/security/advisories/GHSA-gxw4-4fc5-9gr5

## Disclosure Timeline

- 2025-10-07 - Vulnerability reported to vendor
- 2025-12-29 - Coordinated public release of advisory
- 2025-12-29 - Advisory Updated
