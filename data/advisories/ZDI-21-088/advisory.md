# ZDI-21-088: Microsoft Windows Event Tracing Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-088
- **ZDI-CAN:** ZDI-CAN-12674
- **Date:** 2021-01-27
- **CVE:** CVE-2021-1682
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-088/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of Event Tracing for Windows. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1682

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-01-27 - Coordinated public release of advisory
