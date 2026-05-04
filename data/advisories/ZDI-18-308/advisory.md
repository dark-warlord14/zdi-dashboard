# ZDI-18-308: Microsoft Skype URL Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-308
- **ZDI-CAN:** ZDI-CAN-5548
- **Date:** 2018-04-18
- **CVE:** CVE-2018-1000006
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Skype
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-308/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Skype URI handler. A crafted URL can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://electronjs.org/blog/protocol-handler-fix

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-04-18 - Coordinated public release of advisory
- 2018-04-27 - Advisory Updated
