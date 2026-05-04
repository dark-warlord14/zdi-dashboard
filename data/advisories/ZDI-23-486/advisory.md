# ZDI-23-486: (Pwn2Own) Oracle VirtualBox GPA Request Handling Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-486
- **ZDI-CAN:** ZDI-CAN-20723
- **Date:** 2023-04-24
- **CVE:** CVE-2023-21988
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Thomas BOUZERAR (@MajorTomSec) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-486/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of GPA requests. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2023.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
