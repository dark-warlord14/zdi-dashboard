# ZDI-16-170: Joyent SmartOS Linux Zone Escape SS Exception Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-170
- **ZDI-CAN:** ZDI-CAN-3364
- **Date:** 2016-02-18
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-170/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Joyent SmartOS. An attacker must be logged in as a user on the system in order to execute the attack. The specific flaw exists within the handling of an SS Exception. The stack segment fault handling code allows for a GS register to be user controlled. This allows an attacker to elevate privileges to escape a Linux zone and achieve privileged execution on the global zone.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/98788667-Security-Advisory-ZDI-CAN-3263-ZDI-CAN-3284-and-ZDI-CAN-3364-Vulnerabilities

## Disclosure Timeline

- 2015-11-04 - Vulnerability reported to vendor
- 2016-02-18 - Coordinated public release of advisory
