# ZDI-25-1099: Microsoft Edge Mark-Of-The-Web Removal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1099
- **ZDI-CAN:** ZDI-CAN-27795
- **Date:** 2025-12-17
- **CVE:** CVE-2025-60711
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of downloaded files. By performing crafted web requests, an attacker can cause the Mark-Of-The-Web to be removed from downloaded files. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-60711

## Disclosure Timeline

- 2025-09-04 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated
