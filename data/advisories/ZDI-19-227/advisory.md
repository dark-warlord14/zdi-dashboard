# ZDI-19-227: Horner Automation Cscape CSP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-227
- **ZDI-CAN:** ZDI-CAN-7615
- **Date:** 2019-02-20
- **CVE:** CVE-2019-6555
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Horner Automation
- **Affected Products:** Cscape
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-227/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Horner Automation Cscape. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of CSP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Horner Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-050-03

## Disclosure Timeline

- 2018-11-30 - Vulnerability reported to vendor
- 2019-02-20 - Coordinated public release of advisory
