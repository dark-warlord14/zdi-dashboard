# ZDI-16-464: Joyent SmartOS dtrace Zone Escape Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-464
- **ZDI-CAN:** ZDI-CAN-3532
- **Date:** 2016-08-10
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-464/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A method within this implementation allows for an arbitrary write to occur from an out of bounds indexing issue which results in code execution. This allows an attacker to elevate privileges to escape a zone and achieve privileged execution on the headnode.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/99083238--UPDATED-Security-Advisory-Docker-DTrace-and-MAC-Protection-Vulnerabilities

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-08-10 - Coordinated public release of advisory
