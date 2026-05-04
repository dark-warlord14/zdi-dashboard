# ZDI-21-242: Siemens JT2Go SGI File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-242
- **ZDI-CAN:** ZDI-CAN-12176
- **Date:** 2021-02-24
- **CVE:** CVE-2020-26995
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-242/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SGI files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-012-03

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
