# ZDI-17-480: Microsoft Chakra Array JIT Optimization Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-480
- **ZDI-CAN:** ZDI-CAN-4894
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8601
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** AE2BAC2E4B4DA805D01B2952D7E35BA4
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-480/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JavaScript. By performing actions in JavaScript an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8601

## Disclosure Timeline

- 2017-06-12 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
