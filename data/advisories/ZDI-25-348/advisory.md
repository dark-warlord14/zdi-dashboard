# ZDI-25-348: (Pwn2Own) Autel MaxiCharger AC Wallbox Commercial autocharge Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-348
- **ZDI-CAN:** ZDI-CAN-26330
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5829
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autel
- **Affected Products:** Autel MaxiCharger AC Wallbox Commercial
- **Credit:** Tobias Scharnowski, Felix Buchmann, and Kristian Covic of fuzzware.io
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-348/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected affected installations of Autel MaxiCharger AC Wallbox Commercial EV chargers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of JSON messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in American Standard: V1.39.51 and European Standard: V1.56.51

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
