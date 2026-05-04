# ZDI-24-1694: Microsoft PC Manager MSPCManagerService Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1694
- **ZDI-CAN:** ZDI-CAN-25733
- **Date:** 2024-12-17
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PC Manager
- **Credit:** Amol Dosanjh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1694/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft PC Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the MSPCManagerService. By creating a symbolic link, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2024-12-17 - Coordinated public release of advisory
- 2024-12-17 - Advisory Updated
