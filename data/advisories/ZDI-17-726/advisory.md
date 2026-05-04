# ZDI-17-726: Microsoft Internet Explorer JavaScript WeakMap Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-726
- **ZDI-CAN:** ZDI-CAN-4985
- **Date:** 2017-09-15
- **CVE:** CVE-2017-8750
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** likemeng of Baidu Security Lab(Baidu Security Lab is linked to the site :xlab.baidu.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-726/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WeakMap objects in JavaScript. By performing actions in JavaScript an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8750

## Disclosure Timeline

- 2017-07-10 - Vulnerability reported to vendor
- 2017-09-15 - Coordinated public release of advisory
