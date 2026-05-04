# ZDI-16-284: (Pwn2Own) Microsoft Windows dxgkrnl Kernel Driver Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-284
- **ZDI-CAN:** ZDI-CAN-3627
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0176
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Hlavaty Daniel King of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-284/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the DirtyRegions structure. A buffer overflow vulnerability occurs when NumRects is larger than D3DKMT_MAX_PRESENT_HISTORY_RECTS. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-052.aspx

## Disclosure Timeline

- 2016-03-12 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
