# ZDI-22-1050: Foxit PDF Editor JavaScript Optimization Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1050
- **ZDI-CAN:** ZDI-CAN-16867
- **Date:** 2022-08-05
- **CVE:** CVE-2022-37378
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Editor
- **Credit:** DoHyun Lee(@l33d0hyun) of DNSLab, Korea University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the optimization of JavaScript functions. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2022-03-25 - Vulnerability reported to vendor
- 2022-08-05 - Coordinated public release of advisory
