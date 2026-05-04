# ZDI-25-930: win-cli-mcp-server resolveCommandPath Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-930
- **ZDI-CAN:** ZDI-CAN-27787
- **Date:** 2025-10-03
- **CVE:** CVE-2025-11202
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** win-cli-mcp-server
- **Affected Products:** win-cli-mcp-server
- **Credit:** Peter Girnus (@gothburz) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-930/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of win-cli-mcp-server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the resolveCommandPath method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

win-cli-mcp-server has issued an update to correct this vulnerability. More details can be found at: https://github.com/simon-ami/win-cli-mcp-server/commit/521b4a34190d03bde7d433d213c36357181a6d09

## Disclosure Timeline

- 2025-08-07 - Vulnerability reported to vendor
- 2025-10-03 - Coordinated public release of advisory
- 2025-10-03 - Advisory Updated
