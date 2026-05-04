# ZDI-22-378: ICONICS GENESIS64 DWG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-378
- **ZDI-CAN:** ZDI-CAN-14059
- **Date:** 2022-02-18
- **CVE:** CVE-2021-27040
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-378/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of ICONICS GENESIS64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-21-294-01

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2022-02-18 - Coordinated public release of advisory
