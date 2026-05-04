# ZDI-21-398: Phoenix Contact Automationworx XML File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-398
- **ZDI-CAN:** ZDI-CAN-12244
- **Date:** 2021-03-31
- **CVE:** CVE-2020-12497
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-398/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XML files. When parsing the name attribute of a pou element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-20-191-01 https://cert.vde.com/en-us/advisories/vde-2020-023

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-03-31 - Coordinated public release of advisory
- 2021-04-16 - Advisory Updated
