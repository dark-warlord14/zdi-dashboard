# ZDI-21-504: Microsoft Windows splwow64 Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-504
- **ZDI-CAN:** ZDI-CAN-12781
- **Date:** 2021-05-03
- **CVE:** CVE-2021-1648
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Elliot Cao (@iamelli0t) working with Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-504/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the user-mode printer driver host process splwow64.exe. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges from low integrity and execute arbitrary code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1648

## Disclosure Timeline

- 2021-01-05 - Vulnerability reported to vendor
- 2021-05-03 - Coordinated public release of advisory
