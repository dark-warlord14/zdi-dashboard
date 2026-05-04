# ZDI-24-366: (Pwn2Own) Google Chrome WASM Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-366
- **ZDI-CAN:** ZDI-CAN-23792
- **Date:** 2024-04-15
- **CVE:** CVE-2024-2887
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-366/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of WebAssembly. By specifying a large number of structures, an attacker can cause the compiler to emit unsafe code. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2024/03/stable-channel-update-for-desktop_26.html

## Disclosure Timeline

- 2024-03-26 - Vulnerability reported to vendor
- 2024-04-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
