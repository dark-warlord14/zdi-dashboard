# ZDI-26-279: Microsoft Windows Snipping Tool Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-279
- **ZDI-CAN:** ZDI-CAN-28793
- **Date:** 2026-04-15
- **CVE:** CVE-2026-32183
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Zeeshan Shaikh (@bugzzzhunter)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-279/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Snipping Tool app. The issue results from improper validation of a parameter. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32183

## Disclosure Timeline

- 2026-03-03 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
