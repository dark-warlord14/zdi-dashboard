# ZDI-17-916: Microsoft Windows VBScript Join Function Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-916
- **ZDI-CAN:** ZDI-CAN-5112
- **Date:** 2017-11-20
- **CVE:** CVE-2017-11869
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-916/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the Join function in VBScript. By performing actions in VBScript, an attacker can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-11869

## Disclosure Timeline

- 2017-09-01 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
