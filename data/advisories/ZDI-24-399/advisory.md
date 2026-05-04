# ZDI-24-399: Microsoft Windows MHT File Mark-Of-The-Web Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-399
- **ZDI-CAN:** ZDI-CAN-22547
- **Date:** 2024-04-25
- **CVE:** CVE-2024-29991
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-399/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-Of-The-Web security feature to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of .MHT files. The issue results from the lack of a security check on .MHT files located in shared folders. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-29991

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-04-25 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
