# ZDI-25-921: Razer Synapse 3 RazerPhilipsHueUninstall Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-921
- **ZDI-CAN:** ZDI-CAN-26375
- **Date:** 2025-09-30
- **CVE:** CVE-2025-9870
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Razer
- **Affected Products:** Synapse 3
- **Credit:** 0x_alibabas (x.com/0x_alibabas)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-921/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Razer Synapse 3. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Philips HUE module installer. By creating a symbolic link, an attacker can abuse the installer to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 3.10.730.71519

## Disclosure Timeline

- 2025-03-30 - Vulnerability reported to vendor
- 2025-09-30 - Coordinated public release of advisory
- 2025-09-30 - Advisory Updated
