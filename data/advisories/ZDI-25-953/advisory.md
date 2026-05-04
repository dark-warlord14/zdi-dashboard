# ZDI-25-953: Microsoft Windows TAR File Parsing NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-953
- **ZDI-CAN:** ZDI-CAN-27289
- **Date:** 2025-10-14
- **CVE:** CVE-2025-59284
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Len Sadowski and Oguz Bektas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-953/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TAR files. A crafted hard link in a TAR file can trigger an outgoing SMB request. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-59284

## Disclosure Timeline

- 2025-07-25 - Vulnerability reported to vendor
- 2025-10-14 - Coordinated public release of advisory
- 2025-10-14 - Advisory Updated
