# ZDI-21-1077: Microsoft Visual Studio Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1077
- **ZDI-CAN:** ZDI-CAN-14603
- **Date:** 2021-09-16
- **CVE:** CVE-2021-26434
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1077/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Visual Studio. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Visual Studio installer. The issue results from incorrect permissions set on a resource used by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26434

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
