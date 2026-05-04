# ZDI-25-582: Microsoft Windows Startup Folder SmartScreen Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-582
- **ZDI-CAN:** ZDI-CAN-27246
- **Date:** 2025-07-08
- **CVE:** CVE-2025-49740
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun - Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-582/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the SmartScreen security feature on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of executables in the user's Startup folder. When automatically launching executables from the Startup folder, Windows does not apply the SmartScreen security feature. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49740

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
