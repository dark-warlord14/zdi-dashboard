# ZDI-20-826: Phoenix Contact Automationworx PC WORX MWE File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-826
- **ZDI-CAN:** ZDI-CAN-10586
- **Date:** 2020-07-10
- **CVE:** CVE-2020-12498
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** mdm
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-826/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MWE files by the PC WORX and PC WORX Express executables. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-191-01

## Disclosure Timeline

- 2020-04-09 - Vulnerability reported to vendor
- 2020-07-10 - Coordinated public release of advisory
