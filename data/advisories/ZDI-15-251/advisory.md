# ZDI-15-251: (Pwn2Own) Microsoft Internet Explorer Protocol Handler Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-251
- **ZDI-CAN:** ZDI-CAN-2832
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1748
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-251/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of res:// and Windows Help Engine. By running specially crafted JavaScript, a 32-bit medium integrity process can be spawned. By injecting privileged javascript into this process, an attacker can leverage this vulnerability to execute code under the context of a medium integrity process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
