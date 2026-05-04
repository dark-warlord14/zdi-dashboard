# ZDI-22-730: Microsoft Windows Print Spooler Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-730
- **ZDI-CAN:** ZDI-CAN-16229
- **Date:** 2022-05-10
- **CVE:** CVE-2022-29104
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Oliver Lyak (@ly4k_) of Institut For Cyber Risk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-730/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. By creating a symbolic link, an attacker can cause the service to load an arbitrary DLL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-29104

## Disclosure Timeline

- 2022-02-02 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
