# ZDI-25-842: (Pwn2Own) Microsoft Windows Exposed Dangerous Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-842
- **ZDI-CAN:** ZDI-CAN-27171
- **Date:** 2025-08-14
- **CVE:** CVE-2025-53156
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Angelboy (@scwuaptx) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-842/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Storage Port Driver. The issue results from an exposed dangerous function. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53156

## Disclosure Timeline

- 2025-06-12 - Vulnerability reported to vendor
- 2025-08-14 - Coordinated public release of advisory
- 2025-08-14 - Advisory Updated
