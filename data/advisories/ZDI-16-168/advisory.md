# ZDI-16-168: Joyent SmartOS dtrace Zone Escape Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-168
- **ZDI-CAN:** ZDI-CAN-3263
- **Date:** 2016-02-18
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-168/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A method within this implementation allows for an integer overflow to occur which results in the allocation of a buffer that is too small which is then overflowed. This allows an attacker to elevate privileges to escape a zone and achieve privileged execution on the global zone.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/98788667-Security-Advisory-ZDI-CAN-3263-ZDI-CAN-3284-and-ZDI-CAN-3364-Vulnerabilities

## Disclosure Timeline

- 2015-09-21 - Vulnerability reported to vendor
- 2016-02-18 - Coordinated public release of advisory
