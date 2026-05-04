# ZDI-25-983: evernote-mcp-server openBrowser Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-983
- **ZDI-CAN:** ZDI-CAN-27913
- **Date:** 2025-10-30
- **CVE:** CVE-2025-12489
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** evernote-mcp-server
- **Affected Products:** evernote-mcp-server
- **Credit:** Peter Girnus (@gothburz) and Brandon Niemczyk of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-983/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of evernote-mcp-server. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the openBrowser function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

evernote-mcp-server has issued an update to correct this vulnerability. More details can be found at: https://github.com/brentmid/evernote-mcp-server/commit/1e66c78c4ce6ea294ac6b0eb289a9eae9c5e9579

## Disclosure Timeline

- 2025-09-23 - Vulnerability reported to vendor
- 2025-10-30 - Coordinated public release of advisory
- 2025-10-30 - Advisory Updated
