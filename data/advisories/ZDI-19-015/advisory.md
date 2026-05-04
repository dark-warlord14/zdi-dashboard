# ZDI-19-015: Microsoft Visual Studio asm Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-015
- **ZDI-CAN:** ZDI-CAN-7370
- **Date:** 2019-01-10
- **CVE:** CVE-2019-0546
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Simon Zuckerbraun of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-015/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on executables compiled using vulnerable installations of Microsoft Visual Studio. Attack vectors will vary depending on the nature of the executable in question. The specific flaw exists within the compilation of __asm blocks in Visual C++. Incorrect output produced by the compiler can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0546

## Disclosure Timeline

- 2018-10-15 - Vulnerability reported to vendor
- 2019-01-10 - Coordinated public release of advisory
