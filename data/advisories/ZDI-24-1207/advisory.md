# ZDI-24-1207: Microsoft Windows Internet Explorer File Extension Spoofing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1207
- **ZDI-CAN:** ZDI-CAN-24998
- **Date:** 2024-09-10
- **CVE:** CVE-2024-43461
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer prompts the user after a file is downloaded. A crafted file name can cause the true file extension to be hidden, misleading the user into believing that the file type is harmless. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-43461

## Disclosure Timeline

- 2024-07-19 - Vulnerability reported to vendor
- 2024-09-10 - Coordinated public release of advisory
- 2024-09-10 - Advisory Updated
