# ZDI-26-117: RustDesk Client for Windows Transfer File Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-117
- **ZDI-CAN:** ZDI-CAN-27909
- **Date:** 2026-02-19
- **CVE:** CVE-2026-2490
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** RustDesk
- **Affected Products:** Client for Windows
- **Credit:** mad31k
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-117/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of RustDesk Client for Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Transfer File feature. By uploading a symbolic link, an attacker can abuse the service to read arbitrary files. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

RustDesk has issued an update to correct this vulnerability. More details can be found at: https://github.com/rustdesk/rustdesk/pull/13736

## Disclosure Timeline

- 2025-09-11 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
