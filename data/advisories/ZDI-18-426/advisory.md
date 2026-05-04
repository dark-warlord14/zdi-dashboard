# ZDI-18-426: Microsoft Teams URL Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-426
- **ZDI-CAN:** ZDI-CAN-5589
- **Date:** 2018-05-14
- **CVE:** CVE-2018-1000006
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-426/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Teams. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the msteams URL handler. When parsing a specially crafted URL, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://electronjs.org/blog/protocol-handler-fix

## Disclosure Timeline

- 2018-01-12 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
