# ZDI-21-568: Siemens Tecnomatix Plant Simulation SPP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-568
- **ZDI-CAN:** ZDI-CAN-13279
- **Date:** 2021-05-13
- **CVE:** CVE-2021-27396
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Tecnomatix Plant Simulation
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-568/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Tecnomatix Plant Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SPP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-131-08 https://cert-portal.siemens.com/productcert/pdf/ssa-983548.pdf

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
