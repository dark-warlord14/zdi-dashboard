# ZDI-25-579: Microsoft PC Manager Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-579
- **ZDI-CAN:** ZDI-CAN-26249
- **Date:** 2025-07-08
- **CVE:** CVE-2025-47993
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** PC Manager
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-579/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft PC Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the MSPCManagerService service. The service loads a file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47993

## Disclosure Timeline

- 2025-03-12 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
