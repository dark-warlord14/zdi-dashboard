# ZDI-16-169: Joyent SmartOS dtrace Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-169
- **ZDI-CAN:** ZDI-CAN-3284
- **Date:** 2016-02-18
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-169/
## Vulnerability Details

This vulnerability allows local attackers to disclose information on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A function within this implementation allows for arbitrary reads from kernel space. This allows an attacker to read arbitrary memory from the global zone where the zone resides.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/entries/98788667-Security-Advisory-ZDI-CAN-3263-ZDI-CAN-3284-and-ZDI-CAN-3364-Vulnerabilities

## Disclosure Timeline

- 2015-09-21 - Vulnerability reported to vendor
- 2016-02-18 - Coordinated public release of advisory
