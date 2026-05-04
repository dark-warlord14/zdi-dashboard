# ZDI-16-465: Joyent SmartOS dtrace Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-465
- **ZDI-CAN:** ZDI-CAN-3531
- **Date:** 2016-08-10
- **CVE:** N/A
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Joyent
- **Affected Products:** SmartOS
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-465/
## Vulnerability Details

This vulnerability allows local attackers to disclose information on vulnerable installations of Joyent SmartOS. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the dtrace implementation in SmartOS. A function within this implementation allows for arbitrary reads from kernel space. This allows an attacker to read arbitrary memory from the headnode where the zone resides.

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-08-10 - Coordinated public release of advisory
