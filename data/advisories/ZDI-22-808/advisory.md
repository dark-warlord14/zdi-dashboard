# ZDI-22-808: Microsoft Windows DiagTrack Service Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-808
- **ZDI-CAN:** ZDI-CAN-15973
- **Date:** 2022-06-01
- **CVE:** CVE-2022-24479
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea with THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-808/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DiagTrack service. By creating a symbolic link, an attacker can abuse the service to overwrite arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24479

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-06-01 - Coordinated public release of advisory
