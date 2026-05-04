# ZDI-24-1657: Microsoft Windows Directory Traversal Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1657
- **ZDI-CAN:** ZDI-CAN-24583
- **Date:** 2024-12-11
- **CVE:** CVE-2024-49082
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** st4nly0n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1657/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files or disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of filenames. The issue results from the lack of proper validation of filenames originating from untrusted sources, which may contain path traversal characters. An attacker can leverage this vulnerability to delete files or disclose information in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49082

## Disclosure Timeline

- 2024-08-09 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
