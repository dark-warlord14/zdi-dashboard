# ZDI-24-019: Bentley View SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-019
- **ZDI-CAN:** ZDI-CAN-19067
- **Date:** 2024-01-08
- **CVE:** CVE-2023-44430
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** View
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/advisories/be-2022-0019/

## Disclosure Timeline

- 2022-10-06 - Vulnerability reported to vendor
- 2024-01-08 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
