# ZDI-16-007: McAfee Application Control Kernel Driver Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-007
- **ZDI-CAN:** ZDI-CAN-3285
- **Date:** 2016-01-08
- **CVE:** CVE-2016-1715
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:M/Au:S/C:C/I:C/A:C
- **Affected Vendors:** McAfee
- **Affected Products:** Application Control
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-007/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of McAfee Application Control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of syscall 768 in the swin.sys kernel driver. A malicious call can write a 0 to an arbitrary address in kernel memory. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10145

## Disclosure Timeline

- 2015-09-17 - Vulnerability reported to vendor
- 2016-01-08 - Coordinated public release of advisory
