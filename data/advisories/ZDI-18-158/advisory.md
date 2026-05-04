# ZDI-18-158: Joyent SmartOS SMB_IOC_SVCENUM Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-158
- **ZDI-CAN:** ZDI-CAN-4983
- **Date:** 2018-02-12
- **CVE:** CVE-2018-1165
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-158/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Joyent SmartOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SMB_IOC_SVCENUM IOCTL. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the host OS.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/hc/en-us/articles/360000124928

## Disclosure Timeline

- 2017-08-16 - Vulnerability reported to vendor
- 2018-02-12 - Coordinated public release of advisory
- 2018-02-12 - Advisory Updated
