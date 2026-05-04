# ZDI-25-090: Microsoft Edge UI Misrepresentation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-090
- **ZDI-CAN:** ZDI-CAN-25393
- **Date:** 2025-02-24
- **CVE:** CVE-2025-21404
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Simon Zuckerbraun and Peter Girnus - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Microsoft Edge displays a warning about hazardous downloads. A crafted file name can cause the warning message to be displayed incorrectly, misleading the user into believing that the file is harmless. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21404

## Disclosure Timeline

- 2024-09-17 - Vulnerability reported to vendor
- 2025-02-24 - Coordinated public release of advisory
- 2025-02-24 - Advisory Updated
