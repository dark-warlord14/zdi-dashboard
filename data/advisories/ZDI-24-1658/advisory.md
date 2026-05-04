# ZDI-24-1658: Microsoft Edge File Extension Spoofing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1658
- **ZDI-CAN:** ZDI-CAN-25361
- **Date:** 2024-12-11
- **CVE:** CVE-2024-49041
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Peter Girnus - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1658/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Microsoft Edge prompts the user after a file is downloaded. A crafted file name can cause the true file extension to be hidden, misleading the user into believing that the file type is harmless. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49041

## Disclosure Timeline

- 2024-09-17 - Vulnerability reported to vendor
- 2024-12-11 - Coordinated public release of advisory
- 2024-12-11 - Advisory Updated
