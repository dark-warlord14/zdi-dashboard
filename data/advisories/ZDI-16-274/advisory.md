# ZDI-16-274: Joyent SmartOS dtrace Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-274
- **ZDI-CAN:** ZDI-CAN-3533
- **Date:** 2016-05-04
- **CVE:** N/A
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:H/Au:S/C:C/I:N/A:N
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-274/
## Vulnerability Details

This vulnerability allows local attackers to disclose information on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A function within this implementation allows for arbitrary reads from kernel space. This allows an attacker to read arbitrary memory from the headnode where the zone resides.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/99083238-Security-Advisory-Docker-DTrace-and-MAC-Protection-Vulnerabilities

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-05-04 - Coordinated public release of advisory
