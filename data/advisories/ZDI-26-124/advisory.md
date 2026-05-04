# ZDI-26-124: claude-hovercraft executeClaudeCode Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-124
- **ZDI-CAN:** ZDI-CAN-27785
- **Date:** 2026-02-25
- **CVE:** CVE-2025-15060
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** claude-hovercraft
- **Affected Products:** claude-hovercraft
- **Credit:** Peter Girnus (@gothburz) of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of claude-hovercraft. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the executeClaudeCode method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

The affected repo was removed

## Disclosure Timeline

- 2025-10-06 - Vulnerability reported to vendor
- 2026-02-25 - Coordinated public release of advisory
- 2026-02-25 - Advisory Updated
