# ZDI-18-1052: Microsoft Windows Jet Database Engine Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1052
- **ZDI-CAN:** ZDI-CAN-6258
- **Date:** 2018-09-14
- **CVE:** CVE-2018-8393
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Lucas Leong (@wmliang) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Jet database engine. Crafted data in a database file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8393

## Disclosure Timeline

- 2018-06-05 - Vulnerability reported to vendor
- 2018-09-14 - Coordinated public release of advisory
- 2018-09-14 - Advisory Updated
