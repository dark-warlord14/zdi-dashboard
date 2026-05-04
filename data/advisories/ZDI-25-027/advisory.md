# ZDI-25-027: (Pwn2Own) Google Chrome VideoFrame Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-027
- **ZDI-CAN:** ZDI-CAN-23793
- **Date:** 2025-01-12
- **CVE:** CVE-2024-2886
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Seunghyun Lee (@0x10n) of KAIST Hacking Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the VideoFrame API. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2024/03/stable-channel-update-for-desktop_26.html

## Disclosure Timeline

- 2024-03-26 - Vulnerability reported to vendor
- 2025-01-12 - Coordinated public release of advisory
- 2025-01-12 - Advisory Updated
