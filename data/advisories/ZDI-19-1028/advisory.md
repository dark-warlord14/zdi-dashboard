# ZDI-19-1028: Parallels Desktop Command Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1028
- **ZDI-CAN:** ZDI-CAN-8685
- **Date:** 2019-12-20
- **CVE:** CVE-2019-17148
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Juno Im (@junorouse) from Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1028/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Parallels Service. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Fixed in version 15.1.1

## Disclosure Timeline

- 2019-07-22 - Vulnerability reported to vendor
- 2019-12-20 - Coordinated public release of advisory
