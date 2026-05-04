# ZDI-17-469: (Pwn2Own) Microsoft Windows D3DKMTCreateAllocation Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-469
- **ZDI-CAN:** ZDI-CAN-4630
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8579
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-469/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of memory allocations in dxgkrnl.sys. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8579

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
