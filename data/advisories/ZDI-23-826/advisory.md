# ZDI-23-826: Ashlar-Vellum Cobalt XE File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-826
- **ZDI-CAN:** ZDI-CAN-17966
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34288
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-826/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XE files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in 12.0.1204.54

## Disclosure Timeline

- 2022-07-27 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
