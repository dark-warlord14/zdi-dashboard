# ZDI-19-723: Microsoft Windows jscript9 RegExp.input Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-723
- **ZDI-CAN:** ZDI-CAN-8609
- **Date:** 2019-08-16
- **CVE:** CVE-2019-0988
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-723/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the JIT compiler handles the RegExp.input property in jscript9.dll. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0988

## Disclosure Timeline

- 2019-05-29 - Vulnerability reported to vendor
- 2019-08-16 - Coordinated public release of advisory
