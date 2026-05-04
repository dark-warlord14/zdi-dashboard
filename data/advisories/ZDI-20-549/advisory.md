# ZDI-20-549: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway DNP3 Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-549
- **ZDI-CAN:** ZDI-CAN-10301
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10611
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Tobias Scharnowski, Niklas Breitfeld, and Ali Abbasi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-549/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of data set elements. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-105-03

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
