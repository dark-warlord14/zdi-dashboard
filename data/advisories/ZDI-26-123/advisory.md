# ZDI-26-123: Docker Desktop MCP Server Cleartext Storage of Sensitive Information Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-123
- **ZDI-CAN:** ZDI-CAN-27562
- **Date:** 2026-02-23
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Docker
- **Affected Products:** Desktop
- **Credit:** David Fiser and Alfredo Oliveira of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-123/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Docker Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of the MCP server. The issue results from storing sensitive information in plaintext. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

https://github.com/docker/mcp-gateway/pull/247 According to the vendor, the issue impacts a beta version and a CVE will not be assigned.

## Disclosure Timeline

- 2025-07-09 - Vulnerability reported to vendor
- 2026-02-23 - Coordinated public release of advisory
- 2026-02-23 - Advisory Updated
