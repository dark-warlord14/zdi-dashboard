# ZDI-18-1349: Microsoft Windows VBScript Class_Terminate Scripting.Dictionary Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1349
- **ZDI-CAN:** ZDI-CAN-6749
- **Date:** 2018-11-21
- **CVE:** CVE-2018-8544
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1349/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows VBScript. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Class_Terminate methods when used together with the Scripting.Dictionary component. By performing actions in VBScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8544

## Disclosure Timeline

- 2018-07-14 - Vulnerability reported to vendor
- 2018-11-21 - Coordinated public release of advisory
