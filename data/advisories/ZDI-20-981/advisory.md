# ZDI-20-981: Canonical Ubuntu Virtualization Library Arbitrary File Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-981
- **ZDI-CAN:** ZDI-CAN-11561
- **Date:** 2020-08-11
- **CVE:** CVE-2020-15708
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Trent Shea
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-981/
## Vulnerability Details

This vulnerability allows local attackers to write arbitrary files on affected installations of Libvirt. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the libvirt service. The issue results from improper access control when handling the vol-upload command, which allows an arbitrary file write with attacker controlled data. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/notices/USN-4452-1

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-08-11 - Coordinated public release of advisory
