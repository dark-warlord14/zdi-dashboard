# ZDI-13-192: (Pwn2Own) Microsoft Windows Shared Data ASLR Security Feature Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-192
- **ZDI-CAN:** ZDI-CAN-1836
- **Date:** 2013-08-13
- **CVE:** CVE-2013-2556
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows 7
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the existence of KUSER_SHARED_DATA. The issue lies in the ability to predict the address of the structure, which can then be used to leak addresses. An attacker can leverage this to bypass ASLR and DEP on the host.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-063

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
