# ZDI-24-367: (Pwn2Own) Google Chrome V8 Enum Cache Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-367
- **ZDI-CAN:** ZDI-CAN-23785
- **Date:** 2024-04-15
- **CVE:** CVE-2024-3159
- **CVSS:** 5.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Edouard Bochin (@le_douds) and Tao Yan (@Ga1ois)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-367/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the enum cache in V8. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2024/04/stable-channel-update-for-desktop.html

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-04-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
