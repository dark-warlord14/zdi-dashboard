# ZDI-17-478: Microsoft Chakra Typed Array JIT Optimization Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-478
- **ZDI-CAN:** ZDI-CAN-4886
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8601
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Wang Yuan of Nanyang Technological University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-478/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the generation of JIT code for functions that manipulate typed arrays. By performing actions in JavaScript an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8601

## Disclosure Timeline

- 2017-06-07 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
