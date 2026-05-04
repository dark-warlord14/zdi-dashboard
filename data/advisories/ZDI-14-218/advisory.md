# ZDI-14-218: (Pwn2Own) Microsoft On-Screen Keyboard Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-218
- **ZDI-CAN:** ZDI-CAN-2224
- **Date:** 2014-07-09
- **CVE:** CVE-2014-2781
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** lokihardt@asrt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-218/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the On-Screen Keyboard. The issue lies in the ability to send input to the On-Screen Keyboard from a low integrity process. An attacker can leverage this vulnerability to elevate privileges and execute code under the context of the On-Screen Keyboard process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-039.aspx

## Disclosure Timeline

- 2014-03-11 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
