# ZDI-24-1209: Microsoft Windows Defender SmartScreen Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1209
- **ZDI-CAN:** ZDI-CAN-23616
- **Date:** 2024-09-11
- **CVE:** CVE-2024-38213
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1209/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the SmartScreen security feature to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of files on WebDAV shares. The issue results from the lack of a security check on files that are delivered over WebDAV. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38213

## Disclosure Timeline

- 2024-03-06 - Vulnerability reported to vendor
- 2024-09-11 - Coordinated public release of advisory
- 2024-09-11 - Advisory Updated
