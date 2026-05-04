# ZDI-24-365: (Pwn2Own) Microsoft Edge DOMArrayBuffer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-365
- **ZDI-CAN:** ZDI-CAN-23799
- **Date:** 2024-04-15
- **CVE:** CVE-2024-3914
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Seunghyun Lee (@0x10n) of KAIST Hacking Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-365/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the DOMArrayBuffer class in the Chromium Blink rendering engine. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-3914

## Disclosure Timeline

- 2024-03-28 - Vulnerability reported to vendor
- 2024-04-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
