# ZDI-24-1210: Microsoft Windows Drag and Drop SmartScreen Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1210
- **ZDI-CAN:** ZDI-CAN-24000
- **Date:** 2024-09-11
- **CVE:** CVE-2024-38213
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun and Peter Girnus (@gothburz) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1210/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the SmartScreen security feature on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the File Explorer user interface. The issue results from the lack of a proper security warning message. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38213

## Disclosure Timeline

- 2024-05-02 - Vulnerability reported to vendor
- 2024-09-11 - Coordinated public release of advisory
- 2024-09-11 - Advisory Updated
