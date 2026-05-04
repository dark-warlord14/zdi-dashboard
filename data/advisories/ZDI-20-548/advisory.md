# ZDI-20-548: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway DNP3 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-548
- **ZDI-CAN:** ZDI-CAN-10300
- **Date:** 2020-04-16
- **CVE:** CVE-2020-10613
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Tobias Scharnowski, Niklas Breitfeld, and Ali Abbasi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-548/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Triangle MicroWorks SCADA Data Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists with the handling of data set descriptors. The issue results from the lack of proper validation of user-supplied data which can result in a read past the end of an allocated structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-105-03

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
