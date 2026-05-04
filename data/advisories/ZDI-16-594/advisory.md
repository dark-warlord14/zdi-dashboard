# ZDI-16-594: Microsoft Windows NtUserMagSetContextInformation Kernel State Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-594
- **ZDI-CAN:** ZDI-CAN-4020
- **Date:** 2016-11-08
- **CVE:** CVE-2016-7246
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-594/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the NtUserMagSetContextInformation system call. By supplying specific arguments, an attacker can cause corruption of kernel state. An attacker can leverage this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-135

## Disclosure Timeline

- 2016-09-16 - Vulnerability reported to vendor
- 2016-11-08 - Coordinated public release of advisory
