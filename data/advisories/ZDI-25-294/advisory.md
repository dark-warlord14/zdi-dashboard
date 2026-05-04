# ZDI-25-294: Microsoft PC Manager MSPCManagerService Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-294
- **ZDI-CAN:** ZDI-CAN-26137
- **Date:** 2025-05-21
- **CVE:** CVE-2025-29975
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PC Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-294/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft PC Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the MSPCManagerService. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-29975

## Disclosure Timeline

- 2025-03-12 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
