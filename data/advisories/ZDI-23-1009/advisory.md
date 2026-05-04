# ZDI-23-1009: Canonical Ubuntu OverlayFS File System Missing Authorization Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1009
- **ZDI-CAN:** ZDI-CAN-20913
- **Date:** 2023-07-28
- **CVE:** CVE-2023-2640
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Stonejiajia
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1009/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of attributes. The issue results from missing authorization before allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

https://ubuntu.com/security/notices/USN-6250-1 https://lists.ubuntu.com/archives/kernel-team/2023-July/140923.html

## Disclosure Timeline

- 2023-05-03 - Vulnerability reported to vendor
- 2023-07-28 - Coordinated public release of advisory
