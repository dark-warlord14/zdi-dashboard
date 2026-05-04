# ZDI-23-1555: Microsoft Windows DirectX GpuMmu Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1555
- **ZDI-CAN:** ZDI-CAN-21605
- **Date:** 2023-10-11
- **CVE:** CVE-2023-38159
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1555/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of GPU mapped memory. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38159

## Disclosure Timeline

- 2023-07-20 - Vulnerability reported to vendor
- 2023-10-11 - Coordinated public release of advisory
