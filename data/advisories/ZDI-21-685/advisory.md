# ZDI-21-685: OpenText Brava! Desktop CGM File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-685
- **ZDI-CAN:** ZDI-CAN-12653
- **Date:** 2021-06-15
- **CVE:** CVE-2021-31507
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** OpenText
- **Affected Products:** Brava! Desktop
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-685/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of OpenText Brava! Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CGM files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Cgm2dl 1.9.8.14

## Disclosure Timeline

- 2021-02-10 - Vulnerability reported to vendor
- 2021-06-15 - Coordinated public release of advisory
