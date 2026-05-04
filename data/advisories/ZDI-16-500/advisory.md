# ZDI-16-500: Joyent SmartOS dtrace Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-500
- **ZDI-CAN:** ZDI-CAN-3690
- **Date:** 2016-08-29
- **CVE:** N/A
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-500/
## Vulnerability Details

This vulnerability allows attackers to disclose sensitive information on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A function within this implementation allows for arbitrary reads from kernel space. An attacker can leverage this vulnerability to read arbitrary memory from the headnode where the zone resides.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/99083238--UPDATED-Security-Advisory-Docker-DTrace-and-MAC-Protection-Vulnerabilities

## Disclosure Timeline

- 2016-04-14 - Vulnerability reported to vendor
- 2016-08-29 - Coordinated public release of advisory
