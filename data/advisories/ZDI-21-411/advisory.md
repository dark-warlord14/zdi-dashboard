# ZDI-21-411: (Pwn2Own) Google Chromium V8 XOR Typer Mismatch Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-411
- **ZDI-CAN:** ZDI-CAN-13569
- **Date:** 2021-04-15
- **CVE:** CVE-2021-21220
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chromium
- **Credit:** Dataflow Security - Team Oggetto Contraffatto
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-411/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chromium. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the XOR operation when executed within JIT compiled code. By performing actions in JavaScript, an attacker can trigger a memory access past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2021/04/stable-channel-update-for-desktop.html

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
- 2024-01-08 - Advisory Updated
