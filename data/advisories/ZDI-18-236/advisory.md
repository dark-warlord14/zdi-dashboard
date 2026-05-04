# ZDI-18-236: Joyent SmartOS DTrace DOF Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-236
- **ZDI-CAN:** ZDI-CAN-5106
- **Date:** 2018-03-07
- **CVE:** CVE-2018-1171
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-236/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Joyent SmartOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DTrace DOF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the host OS.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/hc/en-us/articles/360000608188

## Disclosure Timeline

- 2017-10-12 - Vulnerability reported to vendor
- 2018-03-07 - Coordinated public release of advisory
- 2018-03-07 - Advisory Updated
