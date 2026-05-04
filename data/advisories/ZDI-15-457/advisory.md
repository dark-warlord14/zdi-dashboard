# ZDI-15-457: (Pwn2Own) Microsoft Windows secdrv.sys Uninitialized Buffer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-457
- **ZDI-CAN:** ZDI-CAN-2835
- **Date:** 2015-10-07
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-457/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the secdrv.sys driver. The issue lies in the failure to initialize a buffer prior to using it. An attacker can leverage this vulnerability to achieve code execution at SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-097.aspx

## Disclosure Timeline

- 2015-03-19 - Vulnerability reported to vendor
- 2015-10-07 - Coordinated public release of advisory
