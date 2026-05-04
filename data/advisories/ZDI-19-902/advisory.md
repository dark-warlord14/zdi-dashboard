# ZDI-19-902: Horner Automation Cscape CSP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-902
- **ZDI-CAN:** ZDI-CAN-8444
- **Date:** 2019-10-18
- **CVE:** CVE-2019-13541
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Horner Automation
- **Affected Products:** Cscape
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-902/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Horner Automation Cscape. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CSP files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Horner Automation has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-290-02

## Disclosure Timeline

- 2019-06-07 - Vulnerability reported to vendor
- 2019-10-18 - Coordinated public release of advisory
