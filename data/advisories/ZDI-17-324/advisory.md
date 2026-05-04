# ZDI-17-324: (Pwn2Own) Microsoft Edge ArrayBuffer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-324
- **ZDI-CAN:** ZDI-CAN-4584
- **Date:** 2017-05-10
- **CVE:** CVE-2017-0234
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Tencent Security Team Ether (Zhanlu Lab)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-324/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ArrayBuffer objects in JavaScript. By performing actions in JavaScript, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0234

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-10 - Coordinated public release of advisory
