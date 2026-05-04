# ZDI-13-170: (Pwn2Own) Microsoft Windows NtUserMessageCall Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-170
- **ZDI-CAN:** ZDI-CAN-1891
- **Date:** 2013-07-26
- **CVE:** CVE-2013-1300
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows 7
- **Credit:** Nils and Jon of MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within NtUserMessageCall. The issue lies in the handling of boolean arguments. An attacker can leverage this vulnerability to raise privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-053

## Disclosure Timeline

- 2013-03-30 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
