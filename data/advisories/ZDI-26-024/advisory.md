# ZDI-26-024: (0Day) mcp-server-siri-shortcuts shortcutName Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-024
- **ZDI-CAN:** ZDI-CAN-27910
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0758
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** mcp-server-siri-shortcuts
- **Affected Products:** mcp-server-siri-shortcuts
- **Credit:** Peter Girnus (@gothburz) and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-024/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of mcp-server-siri-shortcuts. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the shortcutName parameter. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

09/23/25 – ZDI requested the vendor’s PSIRT contacts in a GitHub issue 09/23/25 – the vendor provided their contacts 09/24/25 – ZDI submitted the report to the vendor 11/10/25 – ZDI asked for updates 12/14/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-09-23 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
