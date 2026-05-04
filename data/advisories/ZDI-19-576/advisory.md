# ZDI-19-576: Phoenix Contact Automationworx BCP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-576
- **ZDI-CAN:** ZDI-CAN-7785
- **Date:** 2019-06-20
- **CVE:** CVE-2019-12871
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-576/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BCP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en-us/advisories/vde-2019-014

## Disclosure Timeline

- 2019-02-21 - Vulnerability reported to vendor
- 2019-06-20 - Coordinated public release of advisory
