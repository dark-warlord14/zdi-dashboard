# ZDI-23-1595: Ashlar-Vellum Cobalt Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1595
- **ZDI-CAN:** ZDI-CAN-21540
- **Date:** 2023-11-14
- **CVE:** CVE-2023-44437
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Sean de Regge
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1595/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of various file types. The process loads a library from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 12.0.1204.78

## Disclosure Timeline

- 2023-08-01 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
