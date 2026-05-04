# ZDI-25-150: Microsoft Windows MSC File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-150
- **ZDI-CAN:** ZDI-CAN-26371
- **Date:** 2025-03-18
- **CVE:** CVE-2025-26633
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Aliakbar Zahravi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-150/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of MSC files. The product does not warn the user before loading an unexpected MSC file. An attacker can leverage this vulnerability to evade file reputation protections and execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-26633

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-03-18 - Coordinated public release of advisory
- 2025-03-18 - Advisory Updated
