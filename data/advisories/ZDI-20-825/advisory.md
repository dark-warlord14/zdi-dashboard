# ZDI-20-825: Phoenix Contact Automationworx PLCOpen XML File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-825
- **ZDI-CAN:** ZDI-CAN-10147
- **Date:** 2020-07-10
- **CVE:** CVE-2020-12497
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** Automationworx
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-825/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Phoenix Contact Automationworx. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLCOpen XML files. When parsing the pou element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-20-191-01

## Disclosure Timeline

- 2020-04-02 - Vulnerability reported to vendor
- 2020-07-10 - Coordinated public release of advisory
