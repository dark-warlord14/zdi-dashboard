# ZDI-23-830: Ashlar-Vellum Cobalt Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-830
- **ZDI-CAN:** ZDI-CAN-18552
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34292
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-830/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X_B or X_T files. The issue results from the lack of proper validation of user-supplied data, which can result in a write before the start of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in 12.0.1204.54

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
