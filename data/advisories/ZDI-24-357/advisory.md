# ZDI-24-357: RARLAB WinRAR Mark-Of-The-Web Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-357
- **ZDI-CAN:** ZDI-CAN-23156
- **Date:** 2024-04-01
- **CVE:** CVE-2024-30370
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N
- **Affected Vendors:** RARLAB
- **Affected Products:** WinRAR
- **Credit:** Orange Tsai(@orange.8361) and NiNi (@terrynini38514) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-357/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-Of-The-Web protection mechanism on affected installations of RARLAB WinRAR. User interaction is required to exploit this vulnerability in that the target must perform a specific action on a malicious page. The specific flaw exists within the archive extraction functionality. A crafted archive entry can cause the creation of an arbitrary file without the Mark-Of-The-Web. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

RARLAB has issued an update to correct this vulnerability. More details can be found at: https://www.rarlab.com/rarnew.htm#27.%20Busgs%20fixed

## Disclosure Timeline

- 2024-02-22 - Vulnerability reported to vendor
- 2024-04-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
