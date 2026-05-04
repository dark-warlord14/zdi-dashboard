# ZDI-20-803: Check Point ZoneAlarm Symlink Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-803
- **ZDI-CAN:** ZDI-CAN-10071
- **Date:** 2020-07-02
- **CVE:** CVE-2020-6013
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Check Point
- **Affected Products:** ZoneAlarm
- **Credit:** Glenn Lloyd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-803/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Check Point ZoneAlarm. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ZoneAlarm Service. The issue results from the lack of proper validation of a user-supplied symbolic link prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Check Point has issued an update to correct this vulnerability. More details can be found at: https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk142952

## Disclosure Timeline

- 2020-02-05 - Vulnerability reported to vendor
- 2020-07-02 - Coordinated public release of advisory
