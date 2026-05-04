# ZDI-25-964: Microsoft Windows LNK File Parsing Improper Input Validation NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-964
- **ZDI-CAN:** ZDI-CAN-28057
- **Date:** 2025-10-27
- **CVE:** CVE-2025-50154
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Miller of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-964/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LNK files. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-50154

## Disclosure Timeline

- 2025-09-10 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
