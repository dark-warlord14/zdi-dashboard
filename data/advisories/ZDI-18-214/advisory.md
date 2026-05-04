# ZDI-18-214: Volkswagen Customer-Link App Protection Mechanism Failure CAN Message Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-214
- **ZDI-CAN:** ZDI-CAN-5264
- **Date:** 2018-02-27
- **CVE:** CVE-2018-1170
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Volkswagen
- **Affected Products:** Customer-Link App
- **Credit:** Aaron Luo Spencer Hsieh (TrendMicro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-214/
## Vulnerability Details

This vulnerability allows adjacent attackers to inject arbitrary Controller Area Network messages on vulnerable installations of Volkswagen Customer-Link App and HTC Customer-Link Bridge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Customer-Link App and Customer-Link Bridge. The issue results from the lack of a proper protection mechanism against unauthorized firmware updates. An attacker can leverage this vulnerability to inject CAN messages.

## Additional Details

Fixed in version 2.08

## Disclosure Timeline

- 2017-10-18 - Vulnerability reported to vendor
- 2018-02-27 - Coordinated public release of advisory
- 2018-02-27 - Advisory Updated
