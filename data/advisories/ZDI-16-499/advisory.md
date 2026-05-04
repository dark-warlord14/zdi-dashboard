# ZDI-16-499: Joyent SmartOS dtrace Zone Escape Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-499
- **ZDI-CAN:** ZDI-CAN-3689
- **Date:** 2016-08-29
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-499/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A method within this implementation allows for an arbitrary write to occur which results in code execution. An attacker can leverage this vulnerability to elevate privileges to escape a zone and achieve privileged execution on the headnode.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/99083238--UPDATED-Security-Advisory-Docker-DTrace-and-MAC-Protection-Vulnerabilities

## Disclosure Timeline

- 2016-04-14 - Vulnerability reported to vendor
- 2016-08-29 - Coordinated public release of advisory
