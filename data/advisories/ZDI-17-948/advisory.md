# ZDI-17-948: Microsoft Windows JavaScript Array JIT Optimization Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-948
- **ZDI-CAN:** ZDI-CAN-5242
- **Date:** 2017-12-12
- **CVE:** CVE-2017-11901
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-948/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JavaScript. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11901

## Disclosure Timeline

- 2017-10-03 - Vulnerability reported to vendor
- 2017-12-12 - Coordinated public release of advisory
