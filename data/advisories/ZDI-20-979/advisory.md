# ZDI-20-979: Canonical Ubuntu apport Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-979
- **ZDI-CAN:** ZDI-CAN-11234
- **Date:** 2020-08-11
- **CVE:** CVE-2020-15702
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-979/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the apport package. The issue results from the lack of proper locking when performing operations on a file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/notices/USN-4449-1

## Disclosure Timeline

- 2020-07-01 - Vulnerability reported to vendor
- 2020-08-11 - Coordinated public release of advisory
