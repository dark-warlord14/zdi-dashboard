# ZDI-19-922: Phoenix Contact Automationworx BCP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-922
- **ZDI-CAN:** ZDI-CAN-7782
- **Date:** 2019-10-29
- **CVE:** CVE-2019-16675
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-922/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BCP files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-302-01

## Disclosure Timeline

- 2019-04-04 - Vulnerability reported to vendor
- 2019-10-29 - Coordinated public release of advisory
