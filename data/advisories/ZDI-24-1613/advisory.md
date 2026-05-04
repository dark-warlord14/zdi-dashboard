# ZDI-24-1613: Intel Driver & Support Assistant Log Folder Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1613
- **ZDI-CAN:** ZDI-CAN-23927
- **Date:** 2024-11-21
- **CVE:** CVE-2024-36488
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Intel
- **Affected Products:** Driver & Support Assistant
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1613/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Intel Driver & Support Assistant. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Intel Driver & Support Assistant service. By creating a symbolic link, an attacker can abuse the service to create an arbitrary directory with weak permissions. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Intel has issued an update to correct this vulnerability. More details can be found at: https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01200.html

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-11-21 - Coordinated public release of advisory
- 2024-11-21 - Advisory Updated
