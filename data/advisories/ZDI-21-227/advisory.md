# ZDI-21-227: Siemens JT2Go PAR File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-227
- **ZDI-CAN:** ZDI-CAN-12041
- **Date:** 2021-02-24
- **CVE:** CVE-2020-27001
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-227/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-695540.pdf https://us-cert.cisa.gov/ics/advisories/icsa-21-147-04

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-06-08 - Advisory Updated
