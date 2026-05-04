# ZDI-21-678: Vector 35 Binary Ninja BNDB File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-678
- **ZDI-CAN:** ZDI-CAN-13668
- **Date:** 2021-06-10
- **CVE:** CVE-2021-31515
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Vector 35
- **Affected Products:** Binary Ninja
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-678/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Vector 35 Binary Ninja. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BNDB files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Vector 35 has issued an update to correct this vulnerability. More details can be found at: https://binary.ninja/2021/06/03/2.4-release.html#security-advisories

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-06-10 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
