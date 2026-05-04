# ZDI-17-475: Microsoft Windows JavaScript super Keyword Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-475
- **ZDI-CAN:** ZDI-CAN-4775
- **Date:** 2017-08-01
- **CVE:** CVE-2017-8598
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** bee13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-475/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the super keyword in JavaScript. By performing actions in script an attacker can trigger access to memory prior to initialization. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8598

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
