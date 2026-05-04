# ZDI-25-221: (Pwn2Own) Lexmark CX331adwe httpd extract-trace Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-221
- **ZDI-CAN:** ZDI-CAN-25849
- **Date:** 2025-04-09
- **CVE:** N/A
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** nella17 (@nella17tw), working with DEVCORE Internship Program, and DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-221/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark CX331adwe printers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the httpd daemon. By creating a symbolic link, an attacker can abuse the service to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fixed in CXLBL.230.408

## Disclosure Timeline

- 2024-12-18 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
