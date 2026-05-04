# ZDI-21-1554: Microsoft Windows tcpip.sys Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1554
- **ZDI-CAN:** ZDI-CAN-14456
- **Date:** 2021-12-21
- **CVE:** CVE-2021-43247
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Fraunhofer FKIE CA&D
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1554/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the tcpip.sys driver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43247

## Disclosure Timeline

- 2021-09-03 - Vulnerability reported to vendor
- 2021-12-21 - Coordinated public release of advisory
