# ZDI-24-293: Microsoft Skype Protection Mechanism Failure Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-293
- **ZDI-CAN:** ZDI-CAN-22552
- **Date:** 2024-03-13
- **CVE:** CVE-2024-21411
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Skype
- **Credit:** Discovered by: Hector Peralta (@hperalta89) and Nicolás Armua
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Today tab. The issue results from the lack of context isolation. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21411

## Disclosure Timeline

- 2023-12-13 - Vulnerability reported to vendor
- 2024-03-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
