# ZDI-23-1154: SonicWALL GMS Virtual Appliance Syslog Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1154
- **ZDI-CAN:** ZDI-CAN-20914
- **Date:** 2023-08-21
- **CVE:** CVE-2023-34129
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** Alex Birnberg of Zymo Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SonicWALL GMS Virtual Appliance. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the InboundSyslogFile class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2023-0010

## Disclosure Timeline

- 2023-06-13 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
