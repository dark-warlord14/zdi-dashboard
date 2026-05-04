# ZDI-20-291: SAP Crystal Reports RPT File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-291
- **ZDI-CAN:** ZDI-CAN-9460
- **Date:** 2020-03-12
- **CVE:** CVE-2020-6208
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** Crystal Reports
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP Crystal Reports. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RPT files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://launchpad.support.sap.com/#/notes/2861301

## Disclosure Timeline

- 2019-11-06 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
