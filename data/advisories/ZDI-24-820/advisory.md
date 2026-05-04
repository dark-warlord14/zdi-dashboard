# ZDI-24-820: Windscribe Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-820
- **ZDI-CAN:** ZDI-CAN-23441
- **Date:** 2024-06-20
- **CVE:** CVE-2024-6141
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Windscribe
- **Affected Products:** Windscribe
- **Credit:** Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-820/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Windscribe. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windscribe Service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Windscribe has issued an update to correct this vulnerability. More details can be found at: https://github.com/Windscribe/Desktop-App/blob/90a5cc3c1f50f6545f83969c2ace6b4ac2c91c4e/client/common/changelog.txt#L23

## Disclosure Timeline

- 2024-05-30 - Vulnerability reported to vendor
- 2024-06-20 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
