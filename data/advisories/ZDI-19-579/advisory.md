# ZDI-19-579: Phoenix Contact Automationworx BCP File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-579
- **ZDI-CAN:** ZDI-CAN-7781
- **Date:** 2019-06-20
- **CVE:** CVE-2019-12869
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-579/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BCP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en-us/advisories/vde-2019-014

## Disclosure Timeline

- 2019-03-06 - Vulnerability reported to vendor
- 2019-06-20 - Coordinated public release of advisory
