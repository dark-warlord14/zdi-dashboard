# ZDI-17-1016: Microsoft Chakra Typed Array JIT Optimization Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-1016
- **ZDI-CAN:** ZDI-CAN-5321
- **Date:** 2018-04-16
- **CVE:** CVE-2017-11889
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Chakra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-1016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Chakra. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the generation of JIT code for functions that manipulate typed arrays. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11889

## Disclosure Timeline

- 2017-11-07 - Vulnerability reported to vendor
- 2018-04-16 - Coordinated public release of advisory
- 2018-04-16 - Advisory Updated
