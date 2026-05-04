# ZDI-23-825: Ashlar-Vellum Cobalt CO File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-825
- **ZDI-CAN:** ZDI-CAN-17892
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34287
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-825/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CO files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in 12.0.1204.54

## Disclosure Timeline

- 2022-07-27 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
