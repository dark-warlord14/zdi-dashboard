# ZDI-22-1409: Microsoft Windows User-Mode Print Driver Insufficient Message Authentication Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1409
- **ZDI-CAN:** ZDI-CAN-17358
- **Date:** 2022-10-14
- **CVE:** CVE-2022-37986
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1409/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute code at low integrity on the target system in order to exploit this vulnerability. The specific flaw exists within the user-mode print driver host process. The issue results from insufficient validation of the origin of commands. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37986

## Disclosure Timeline

- 2022-06-28 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
