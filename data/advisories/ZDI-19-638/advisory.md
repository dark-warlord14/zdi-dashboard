# ZDI-19-638: Microsoft Windows ADODB Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-638
- **ZDI-CAN:** ZDI-CAN-7854
- **Date:** 2019-07-08
- **CVE:** CVE-2019-0920
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-638/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within msado15.dll. By performing actions in script, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0920

## Disclosure Timeline

- 2019-01-25 - Vulnerability reported to vendor
- 2019-07-08 - Coordinated public release of advisory
