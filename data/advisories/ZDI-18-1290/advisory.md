# ZDI-18-1290: Microsoft Visual Studio Code URL Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1290
- **ZDI-CAN:** ZDI-CAN-5567
- **Date:** 2018-10-17
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio Code
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Visual Studio Code. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the vscode URI handler. A crafted URI can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

addressed in 1.19.2 release of Visual Studio

## Disclosure Timeline

- 2018-01-09 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
- 2018-10-17 - Advisory Updated
